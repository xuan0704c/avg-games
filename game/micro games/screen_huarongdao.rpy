init python:
    import pygame

    def _huarong_hex(hex_color):
        """'#RRGGBB' -> (R, G, B) 元组，供 pygame.draw 使用"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


    # 跨 interaction 复用的 displayable 实例（拖拽/动画状态不因 screen 重建而丢失）
    huarong_displayable = None


    class HuarongDisplayable(renpy.Displayable):
        """华容道 渲染+输入层。

        逻辑层（HuarongDaoGame）保留，这里只负责：
        - render()：pygame 一次绘制 棋盘/方块/出口 + 滑动动画插值 + 每帧强制重绘
        - event()：鼠标按住方块拖拽滑动（沿主导方向滑到尽头），松手落格
        键盘移动（方向键/WASD）保留在 screen 层。
        """

        def __init__(self, game, **properties):
            super(HuarongDisplayable, self).__init__(**properties)
            self.game = game
            self.width = 1920
            self.height = 1080
            self.grid_start_x = 600
            self.grid_start_y = 200
            self.cell_size = 100

            # 拖拽状态
            self.drag_block = None        # 正在拖拽的 block
            self.drag_start_pos = (0, 0)  # 拖拽起点（块起始格坐标）
            self.drag_target = None       # (gx, gy) 拖拽目标格

            # 滑动动画：id(block) -> [display_x, display_y]（向逻辑位置指数收敛）
            self.anim = {}

            # 方块名字字体（系统字体；加载失败则只画色块）
            self.font = None
            for fp in ("C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/simhei.ttf",
                       "C:/Windows/Fonts/simsun.ttc"):
                try:
                    self.font = pygame.font.Font(fp, 18)
                    break
                except Exception:
                    continue

        # ---------- 渲染 ----------
        def render(self, width, height, st, at):
            gsx, gsy, cs = self.grid_start_x, self.grid_start_y, self.cell_size
            bw, bh = BOARD_WIDTH, BOARD_HEIGHT
            surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            surf.fill(_huarong_hex(HUARONG_COLORS['background']))

            # 棋盘底 + 边框
            pygame.draw.rect(surf, _huarong_hex(HUARONG_COLORS['border']),
                             (gsx - 12, gsy - 12, bw * cs + 24, bh * cs + 24))
            pygame.draw.rect(surf, _huarong_hex(HUARONG_COLORS['board']),
                             (gsx - 6, gsy - 6, bw * cs + 12, bh * cs + 12))
            # 格子线
            for i in range(bw + 1):
                pygame.draw.line(surf, _huarong_hex(HUARONG_COLORS['border']),
                                 (gsx - 6 + i * cs, gsy - 6), (gsx - 6 + i * cs, gsy + bh * cs + 6), 1)
            for j in range(bh + 1):
                pygame.draw.line(surf, _huarong_hex(HUARONG_COLORS['border']),
                                 (gsx - 6, gsy - 6 + j * cs), (gsx + bw * cs + 6, gsy - 6 + j * cs), 1)

            # 出口标记（底部 2 格宽）
            exit_y = gsy + bh * cs
            pygame.draw.rect(surf, _huarong_hex(HUARONG_COLORS['exit']),
                             (gsx + cs, exit_y - 8, cs * 2, 8))
            if self.font:
                try:
                    lbl = self.font.render("出口", True, _huarong_hex(HUARONG_COLORS['exit']))
                    surf.blit(lbl, (int(gsx + cs * 2 - lbl.get_width() / 2), int(exit_y + 10)))
                except Exception:
                    pass

            # 方块（含滑动动画插值）
            for block in self.game.blocks:
                px, py = self._block_display_pos(block)
                w = block.width * cs - 4
                h = block.height * cs - 4
                col = _huarong_hex(block.color)
                pygame.draw.rect(surf, col, (int(px + 2), int(py + 2), w, h))
                # 边框：选中金边，否则深色
                bc = (255, 215, 0) if block.selected else _huarong_hex(HUARONG_COLORS['border'])
                pygame.draw.rect(surf, bc, (int(px + 2), int(py + 2), w, h), 2)
                # 名字
                if self.font:
                    try:
                        label = self.font.render(block.name, True, (255, 255, 255))
                        surf.blit(label, (int(px + 2 + w / 2 - label.get_width() / 2),
                                          int(py + 2 + h / 2 - label.get_height() / 2)))
                    except Exception:
                        pass

            # 每帧强制重绘
            renpy.redraw(self, 0)

            rv = renpy.Render(self.width, self.height)
            rv.blit(surf, (0, 0))
            return rv

        def _block_display_pos(self, block):
            """方块显示位置：拖拽中跟手到目标格，否则向逻辑位置指数收敛（滑动动画）"""
            cs = self.cell_size
            gsx = self.grid_start_x
            gsy = self.grid_start_y

            if block is self.drag_block and self.drag_target is not None:
                gx, gy = self.drag_target
                return gsx + gx * cs, gsy + gy * cs

            key = id(block)
            if key not in self.anim:
                self.anim[key] = [float(block.x), float(block.y)]
            dx, dy = self.anim[key]
            # 指数趋近（0.3/帧 ≈ 0.15s 完成一格滑动）
            nx = dx + (block.x - dx) * 0.3
            ny = dy + (block.y - dy) * 0.3
            if abs(block.x - nx) < 0.01 and abs(block.y - ny) < 0.01:
                nx, ny = float(block.x), float(block.y)
            self.anim[key] = [nx, ny]
            return gsx + nx * cs, gsy + ny * cs

        # ---------- 输入 ----------
        def event(self, ev, x, y, st):
            gsx, gsy, cs = self.grid_start_x, self.grid_start_y, self.cell_size

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if self.game.won:
                    return None
                gx = int((x - gsx) / cs)
                gy = int((y - gsy) / cs)
                for block in self.game.blocks:
                    if block.contains_point(gx, gy):
                        self.game.select_block_at(gx, gy)
                        self.drag_block = block
                        self.drag_start_pos = (block.x, block.y)
                        self.drag_target = (block.x, block.y)
                        break

            elif ev.type == pygame.MOUSEMOTION:
                if self.drag_block is not None:
                    gx = int((x - gsx) / cs)
                    gy = int((y - gsy) / cs)
                    sx, sy = self.drag_start_pos
                    dx = gx - sx
                    dy = gy - sy
                    # 主导方向
                    if abs(dx) >= abs(dy):
                        d = (1 if dx > 0 else -1 if dx < 0 else 0, 0)
                    else:
                        d = (0, 1 if dy > 0 else -1 if dy < 0 else 0)
                    if d != (0, 0):
                        steps = self._max_steps(self.drag_block, d[0], d[1])
                        self.drag_target = (sx + d[0] * steps, sy + d[1] * steps)

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                if self.drag_block is not None:
                    sx, sy = self.drag_start_pos
                    tx, ty = self.drag_target
                    dx = tx - sx
                    dy = ty - sy
                    steps = max(abs(dx), abs(dy))
                    if steps > 0:
                        # 落格：逐格滑动并计数（moves + 胜利判定在逻辑层完成）
                        if abs(dx) >= abs(dy):
                            self.game.move_block_steps(1 if dx > 0 else -1, 0, steps)
                        else:
                            self.game.move_block_steps(0, 1 if dy > 0 else -1, steps)
                        # 刷新 screen 文本（步数/胜利界面）—— 仅松手一次，不卡
                        renpy.restart_interaction()
                    # 清理拖拽
                    self.drag_block = None
                    self.drag_target = None

            return None

        def _max_steps(self, block, dx, dy):
            """沿方向最多能滑动的格数（逐格用 can_move 校验，不真正落格）"""
            n = 0
            while self.game.can_move(block, dx, dy):
                n += 1
                block.x += dx
                block.y += dy
            block.x -= dx * n
            block.y -= dy * n
            return n


    def huarong_move(game, dx, dy):
        """键盘移动一格，并强制刷新界面"""
        game.move_block(dx, dy)
        renpy.restart_interaction()


    def huarong_reset(game):
        """重置当前关卡，并强制刷新界面"""
        game.reset_level()
        renpy.restart_interaction()


screen huarongdao_game(game=None):
    zorder 200
    modal True

    default local_game = game

    # 复用 displayable 实例（拖拽/动画状态保留）
    python:
        if huarong_displayable is None or huarong_displayable.game is not local_game:
            huarong_displayable = HuarongDisplayable(local_game)
        local_game._displayable = huarong_displayable

    add huarong_displayable pos (0, 0)

    text "第[local_game.current_level + 1]关 - [HUARONG_LEVELS[local_game.current_level]['name']]" size 50 color "#8B4513" xalign 0.5 ypos 30

    # 步数信息
    vbox:
        pos (1400, 300)
        spacing 15
        text "步数: [local_game.moves]" size 35 color "#8B4513"
        if HUARONG_LEVELS[local_game.current_level].get('best_moves'):
            text "最佳: [HUARONG_LEVELS[local_game.current_level]['best_moves']]步" size 30 color "#8B4513"

    # 操作说明
    vbox:
        pos (1400, 500)
        spacing 10
        text "操作说明:" size 28 color "#8B4513"
        text "按住方块拖拽滑动" size 24 color "#503C28"
        text "方向键/WASD也可移动" size 24 color "#503C28"
        text "将真武殿移至出口" size 24 color "#503C28"
        text "R键重置 | ESC返回" size 24 color "#503C28"

    # 键盘控制
    key "K_UP" action Function(huarong_move, local_game, 0, -1)
    key "K_DOWN" action Function(huarong_move, local_game, 0, 1)
    key "K_LEFT" action Function(huarong_move, local_game, -1, 0)
    key "K_RIGHT" action Function(huarong_move, local_game, 1, 0)
    key "w" action Function(huarong_move, local_game, 0, -1)
    key "W" action Function(huarong_move, local_game, 0, -1)
    key "s" action Function(huarong_move, local_game, 0, 1)
    key "S" action Function(huarong_move, local_game, 0, 1)
    key "a" action Function(huarong_move, local_game, -1, 0)
    key "A" action Function(huarong_move, local_game, -1, 0)
    key "d" action Function(huarong_move, local_game, 1, 0)
    key "D" action Function(huarong_move, local_game, 1, 0)
    key "r" action Function(huarong_reset, local_game)
    key "R" action Function(huarong_reset, local_game)
    key "K_ESCAPE" action Return("back")

    # 胜利界面
    if local_game.won:
        frame:
            xfill True
            yfill True
            background "#0008"
            modal True

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 20

                text "恭喜通关！" size 70 color "#FFD700"
                text "总步数: [local_game.moves]" size 40 color "#FFFFFF"

                textbutton "再来一关":
                    text_size 35
                    background "#006400"
                    hover_background "#008000"
                    action Return("replay")

                textbutton "继续剧情":
                    text_size 30
                    background "#B49678"
                    hover_background "#C8AA86"
                    action Return("success")
