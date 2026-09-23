init python:
    import math
    import pygame

    def _disk_hex_rgb(hex_color):
        """'#RRGGBB' -> (R, G, B) 元组，供 pygame.draw 使用"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


    class StarDiskDisplayable(renpy.Displayable):
        """星空圆盘 渲染+输入层（单 displayable 整幅绘制）。

        逻辑层（StarPuzzleGame）不动：点击选盘、拖拽旋转、胜利判定全部走原逻辑。
        替换原 screen 中 110+ 个独立 displayable（Solid/CircleOutline/Line）拼图，
        一次 pygame Surface 绘制完成 + 每帧强制重绘，根治拖拽卡顿。
        """

        def __init__(self, game, **properties):
            super(StarDiskDisplayable, self).__init__(**properties)
            self.game = game
            self.width = CANVAS_WIDTH
            self.height = CANVAS_HEIGHT
            # 背景图（chapter1/11.png，1920x1080，与画布同尺寸）
            self.bg_image = pygame.transform.smoothscale(
                renpy.load_surface("images/chapter1/11.png"), (self.width, self.height))

            # 圆盘半径（环带不随盘旋转，软边圆环只需预计算一次）
            cyan_outer = DISK_CONFIG['DISK_RADIUS'] * DISK_CONFIG['CYAN_SCALE']      # 270
            cyan_inner = cyan_outer * 6 / 7                                          # ~231
            mag_outer = DISK_CONFIG['DISK_RADIUS'] * DISK_CONFIG['MAGENTA_SCALE']    # 315
            mag_inner = mag_outer * 6 / 7                                            # 270
            self.cyan_inner, self.cyan_outer = int(cyan_inner), int(cyan_outer)
            self.mag_inner, self.mag_outer = int(mag_inner), int(mag_outer)
            self.cyan_ring = self._make_soft_ring(
                self.cyan_inner, self.cyan_outer, _disk_hex_rgb(STAR_COLORS['CYAN']))
            self.magenta_ring = self._make_soft_ring(
                self.mag_inner, self.mag_outer, _disk_hex_rgb(STAR_COLORS['MAGENTA']))

            # 恒星移动特效：每颗星的位置历史（id -> [(x, y), ...]，最新在后）
            self._star_hist = {}

        def _make_soft_ring(self, inner, outer, rgb):
            """生成软边纯色圆环 Surface：alpha 沿半径从内/外边缘(0)向环带中间(255)渐变。

            用 1px 同心圆按渐变 alpha 堆叠（pygame C 速绘制），仅初始化时调用一次。
            """
            size = outer * 2 + 4
            surf = pygame.Surface((size, size), pygame.SRCALPHA)
            c = size // 2
            mid = (inner + outer) / 2.0
            half = max(1.0, (outer - inner) / 2.0)
            for r in range(inner, outer + 1):
                a = int(255 * (1.0 - abs(r - mid) / half))
                if a > 0:
                    pygame.draw.circle(surf, rgb + (a,), (c, c), r, 1)
            return surf

        # ---------- 渲染 ----------
        def render(self, width, height, st, at):
            g = self.game
            # 阻尼推进：每帧向目标角度逼近（拖拽跟手带惯性感）
            g.update()
            surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            # 背景图
            surf.blit(self.bg_image, (0, 0))

            # 蓝色/红色圆盘：软边纯色圆环（初始化时预计算，直接 blit）
            surf.blit(self.cyan_ring, (CX - self.cyan_ring.get_width() // 2,
                                       CY - self.cyan_ring.get_height() // 2))
            surf.blit(self.magenta_ring, (CX - self.magenta_ring.get_width() // 2,
                                          CY - self.magenta_ring.get_height() // 2))

            # 刻度线（蓝盘 / 红盘各 12 条，随盘旋转）
            for i in range(12):
                a1 = 2 * math.pi * i / 12 + g.disk1_angle
                x1 = int(CX + self.cyan_inner * math.cos(a1))
                y1 = int(CY + self.cyan_inner * math.sin(a1))
                x2 = int(CX + self.cyan_outer * math.cos(a1))
                y2 = int(CY + self.cyan_outer * math.sin(a1))
                pygame.draw.line(surf, _disk_hex_rgb(STAR_COLORS['CYAN']), (x1, y1), (x2, y2), 1)
            for i in range(12):
                a2 = 2 * math.pi * i / 12 + g.disk2_angle
                x1 = int(CX + self.mag_inner * math.cos(a2))
                y1 = int(CY + self.mag_inner * math.sin(a2))
                x2 = int(CX + self.mag_outer * math.cos(a2))
                y2 = int(CY + self.mag_outer * math.sin(a2))
                pygame.draw.line(surf, _disk_hex_rgb(STAR_COLORS['MAGENTA']), (x1, y1), (x2, y2), 1)

            # 中心点
            pygame.draw.rect(surf, _disk_hex_rgb(STAR_COLORS['WHITE']), (CX - 3, CY - 3, 6, 6))

            # 目标位置提示圈（每局随恒星随机布局生成）
            for star in g.stars:
                pygame.draw.circle(surf, _disk_hex_rgb(STAR_COLORS['GRAY']),
                                   (CX + int(star['target_x']), CY + int(star['target_y'])), 12, 2)

            # 恒星（主体 + 光晕 + 移动特效 + 选中/接近高亮）
            gold = _disk_hex_rgb(STAR_COLORS['GOLD'])
            for star in g.stars:
                fx, fy = g.get_star_position(star)
                sx, sy = int(fx), int(fy)
                dist = g.get_star_distance(star)
                sid = star['id']

                # ---- 移动特效 ----
                hist = self._star_hist.setdefault(sid, [])
                speed = math.hypot(fx - hist[-1][0], fy - hist[-1][1]) if hist else 0.0
                moving = speed > 0.5
                if moving:
                    hist.append((fx, fy))
                    if len(hist) > 10:
                        hist.pop(0)
                    # 彗尾：沿历史轨迹渐隐渐细
                    n = len(hist)
                    for i in range(n - 1):
                        ta = int(110 * (i + 1) / n)
                        if ta <= 2:
                            continue
                        pygame.draw.line(surf, gold + (ta,),
                                         (int(hist[i][0]), int(hist[i][1])),
                                         (int(hist[i + 1][0]), int(hist[i + 1][1])), 2)
                    # 四芒星闪光：长度随速度与时间轻微脉动
                    flare = (6 + min(speed, 24)) * (1.0 + 0.25 * math.sin(st * 8 + sid))
                    fa = int(150 * min(1.0, speed / 12.0))
                    if fa > 2:
                        for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            pygame.draw.line(surf, gold + (fa,),
                                             (sx + ddx * 9, sy + ddy * 9),
                                             (sx + int(ddx * flare), sy + int(ddy * flare)), 1)
                elif hist:
                    hist.pop(0)  # 停止时尾巴逐帧收回

                # 移动中的柔光填充
                if moving:
                    pygame.draw.circle(surf, gold + (60,), (sx, sy), 12)

                # 光晕环（接近目标越亮）
                if dist < 100:
                    pygame.draw.circle(surf, gold, (sx, sy), 20, 2)
                else:
                    pygame.draw.circle(surf, gold, (sx, sy), 16, 1)
                # 主体
                pygame.draw.rect(surf, gold, (sx - 7, sy - 7, 14, 14))
                # 选中盘恒星：金圈
                if g.selected_disk == star['disk']:
                    pygame.draw.circle(surf, gold, (sx, sy), 10, 2)

            # 每帧强制重绘（官方持续动画模式）
            renpy.redraw(self, 0)

            rv = renpy.Render(self.width, self.height)
            rv.blit(surf, (0, 0))
            return rv

        # ---------- 输入 ----------
        def event(self, ev, x, y, st):
            # x/y 是相对 displayable 左上角的坐标；displayable 全屏，等同屏幕坐标
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                # 点击选盘 + 开始拖拽（不 restart，拖拽靠每帧 redraw 渲染，避免打断）
                self.game.start_drag(x, y)
            elif ev.type == pygame.MOUSEMOTION:
                if self.game.dragging:
                    self.game.drag_disk(x, y)
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                was_dragging = self.game.dragging
                self.game.stop_drag()
                if was_dragging:
                    # 松手后刷新一次 screen 文本 / 胜利界面（仅此一次，不卡）
                    renpy.restart_interaction()
            return None


    # 跨 interaction 复用的 displayable 实例（构造较重：背景缩放+软边圆环预计算，
    # 避免每次 restart_interaction 重建造成的卡顿/跳动）
    star_disk_displayable = None


    def star_disk_reset(game):
        """重置星空圆盘并强制刷新界面"""
        game.reset_level()
        renpy.restart_interaction()


screen chinese_star_puzzle_game(game=None):
    zorder 200
    modal True

    default local_game = game

    # 复用全局实例：同一局游戏不重建，避免松手 restart_interaction 时重建卡顿
    python:
        if star_disk_displayable is None or star_disk_displayable.game is not local_game:
            star_disk_displayable = StarDiskDisplayable(local_game)

    # 整幅游戏渲染 + 输入（单 displayable，状态全在 game 逻辑层）
    add star_disk_displayable pos (0, 0)

    text "星空圆盘" size 60 color STAR_COLORS['WHITE'] xalign 0.5 ypos 20

    # 游戏说明
    vbox:
        pos (50, 200)
        spacing 15
        text "游戏目标:" size 30 color STAR_COLORS['GOLD']
        text "将所有恒星旋转到" size 24 color STAR_COLORS['WHITE']
        text "灰色圆圈标记的目标位置" size 24 color STAR_COLORS['WHITE']
        text "" size 20
        text "操作方法:" size 30 color STAR_COLORS['GOLD']
        text "1. 点击选择圆盘" size 22 color STAR_COLORS['CYAN']
        text "2. 拖拽旋转圆盘" size 22 color STAR_COLORS['MAGENTA']
        text "3. ESC返回菜单" size 22 color STAR_COLORS['WHITE']
        text "   按R重置游戏 " size 22 color STAR_COLORS['GRAY']

    # 选中的圆盘高亮
    if local_game.selected_disk == 1:
        text "蓝色圆盘已选中" size 24 color STAR_COLORS['CYAN'] pos (50, 600)
    elif local_game.selected_disk == 2:
        text "红色圆盘已选中" size 24 color STAR_COLORS['MAGENTA'] pos (50, 600)

    # 胜利检测
    if local_game.won:
        frame:
            xfill True
            yfill True
            background "#0008"
            modal True

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 30

                text "恭喜通关！" size 70 color STAR_COLORS['GOLD']
                text "所有恒星已到达目标位置" size 35 color STAR_COLORS['WHITE']

                textbutton "继续剧情":
                    text_size 35
                    background "#006400"
                    hover_background "#008000"
                    action Return("success")

                textbutton "再来一次":
                    text_size 35
                    background "#006400"
                    hover_background "#008000"
                    action [Function(local_game.reset_level), Return("replay")]

                textbutton "返回菜单":
                    text_size 35
                    background "#C0392B"
                    hover_background "#A93226"
                    action Return("back")

    # 键盘控制
    key "K_ESCAPE" action Return("back")
    key "r" action Function(star_disk_reset, local_game)
    key "R" action Function(star_disk_reset, local_game)


screen chinese_star_puzzle_menu(game=None):
    zorder 200
    modal True

    default local_game = game

    add STAR_COLORS['BACKGROUND']

    text "星空圆盘" size 70 color STAR_COLORS['WHITE'] xalign 0.5 ypos 50

    # 背景星空（覆盖整个屏幕）
    for i in range(80):
        $ import random
        $ random.seed(i*17)
        $ sx = random.randint(0, 1920)
        $ sy = random.randint(0, 1080)
        $ size = random.randint(1, 3)
        add Solid("#FFFFFF", xsize=size, ysize=size) pos (sx, sy)

    frame:
        xalign 0.5
        yalign 0.5
        padding (60, 40)
        background "#1A1A2E"

        vbox:
            spacing 30
            xalign 0.5

            text "游戏说明" size 45 color STAR_COLORS['GOLD']

            vbox:
                spacing 15
                text "目标：将所有恒星旋转到灰色圆圈标记的位置" size 28 color STAR_COLORS['WHITE']
                text "" size 15
                text "操作方法：" size 30 color STAR_COLORS['GOLD']
                text "1. 点击选择圆盘（蓝色或红色）" size 24 color STAR_COLORS['WHITE']
                text "2. 按住并拖拽旋转圆盘" size 24 color STAR_COLORS['WHITE']
                text "3. 蓝色圆盘控制内圈3颗恒星" size 24 color STAR_COLORS['CYAN']
                text "4. 红色圆盘控制外圈3颗恒星" size 24 color STAR_COLORS['MAGENTA']
                text "" size 15
                text "R键重置 | ESC返回" size 24 color STAR_COLORS['GRAY']

            textbutton "开始游戏":
                text_size 40
                background "#084f08"
                hover_background "#008000"
                xsize 300
                xalign 0.5
                action Return("start")

            textbutton "退出":
                text_size 35
                background "#e15b4c"
                hover_background "#A93226"
                xsize 300
                xalign 0.5
                action Return("quit")
