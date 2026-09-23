init python:
    import pygame

    def _hex_to_rgb(hex_color):
        """'#RRGGBB' -> (R, G, B) 元组，供 pygame.draw 使用"""
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


    def _white_to_transparent(surf):
        """把白底照片的背景抠成透明（素材组交付的是白色背景工具图）。

        对接近纯白的像素（RGB 均 > 250）写入 alpha=0，再交给 smoothscale
        缩放时做平滑过渡，避免放置后棋盘上出现白色底块。
        """
        surf = surf.convert_alpha()
        w, h = surf.get_size()
        for y in range(h):
            for x in range(w):
                r, g, b, a = surf.get_at((x, y))
                if r > 250 and g > 250 and b > 250:
                    surf.set_at((x, y), (r, g, b, 0))
        return surf


    class StarPatternDisplayable(renpy.Displayable):
        """星纹密码 渲染+输入层。

        逻辑层（StarPatternPuzzle）不动，这里只负责：
        - render()：用 pygame Surface 每帧绘制网格、可用图形块、拖拽块（跟鼠标）、放置预览
        - event()：左键拿起/松手放置、右键取消、拖拽跟手
        采用官方 Custom Displayable 机制，替代原 ui.timer 每 16ms 强刷整屏的做法。
        """

        def __init__(self, puzzle, **properties):
            super(StarPatternDisplayable, self).__init__(**properties)
            self.puzzle = puzzle

            # 布局参数（与原 screen 保持一致）
            self.grid_start_x = 800
            self.grid_start_y = 200
            self.cell_size = 80

            self.shapes_start_x = 100
            self.shapes_start_y = 100
            self.slot_width = 240
            self.slot_height = 160
            self.slot_gap = 180

            # 鼠标位置（拖拽跟手用，跨 interaction 保留在实例里）
            self.mouse_x = 0
            self.mouse_y = 0

            # 加载 PNG 素材（缩放至基础尺寸）
            self.shape_images = {}
            self._load_images()

        def __getstate__(self):
            """存档/重载时：pygame Surface 不可序列化，只保留逻辑状态，加载后重建图片"""
            state = self.__dict__.copy()
            state['shape_images'] = {}
            state['_rot_cache'] = {}
            return state

        def __setstate__(self, state):
            self.__dict__.update(state)
            self.shape_images = {}
            self._rot_cache = {}
            self._load_images()

        def _load_images(self):
            """加载工具 PNG：白底抠透明后缩放到基础尺寸（240x160 / 160x160 / 320x80）"""
            cs = self.cell_size
            base_sizes = {
                "L形":   (3 * cs, 2 * cs),
                "Z形":   (3 * cs, 2 * cs),
                "T形":   (3 * cs, 2 * cs),
                "田字形": (2 * cs, 2 * cs),
                "长条形": (4 * cs, 1 * cs),
            }
            for name, path in SHAPE_IMAGES.items():
                surf = _white_to_transparent(renpy.load_surface(path))
                tw, th = base_sizes[name]
                self.shape_images[name] = pygame.transform.smoothscale(surf, (tw, th))

            # 底板暂不使用，网格由程序绘制
            # board = renpy.load_surface("images/microgames/星纹密码/pat_board_960x960.png")
            # self.board_image = pygame.transform.smoothscale(board,
            #     (self.puzzle.grid_width * cs, self.puzzle.grid_height * cs))

        def _rotated_image(self, name, rotation):
            """按旋转次数返回旋转后的 surface（缓存）"""
            key = (name, rotation)
            if not hasattr(self, "_rot_cache"):
                self._rot_cache = {}
            if key not in self._rot_cache:
                orig = self.shape_images[name]
                angle = -rotation * 90  # pygame 逆时针为正，顺时针 90° = -90°
                self._rot_cache[key] = pygame.transform.rotate(orig, angle)
            return self._rot_cache[key]

        # ---------- 渲染 ----------
        def render(self, width, height, st, at):
            cs = self.cell_size
            gsx = self.grid_start_x
            gsy = self.grid_start_y

            surf = pygame.Surface((width, height), pygame.SRCALPHA)

            # 1. 6x6 网格（程序画，无底图）：已占用格子金色高亮，未占用深蓝
            occupied = set()
            for block in self.puzzle.placed_blocks:
                gx, gy = block["gx"], block["gy"]
                for (dx, dy) in block["cells"]:
                    occupied.add((gx + dx, gy + dy))
            for y in range(self.puzzle.grid_height):
                for x in range(self.puzzle.grid_width):
                    px = gsx + x * cs
                    py = gsy + y * cs
                    if (x, y) in occupied:
                        # 已占用：金色底，与未占用格子明显区分
                        pygame.draw.rect(surf, (255, 200, 40, 220), (px + 1, py + 1, cs - 2, cs - 2))
                    else:
                        pygame.draw.rect(surf, (44, 62, 80, 200), (px + 1, py + 1, cs - 2, cs - 2))
                    pygame.draw.rect(surf, (127, 140, 141, 160), (px, py, cs, cs), 1)

            # 2. 已放置的块（blit 工具 PNG，按旋转后几何中心对齐）
            for block in self.puzzle.placed_blocks:
                name = block["name"]
                rot = block["rotation"]
                gx, gy = block["gx"], block["gy"]
                img = self._rotated_image(name, rot)
                # 用旋转后 cells 的几何中心对齐（与拖拽预览一致，避免旋转后偏移）
                cells = block["cells"]
                xs = [c[0] for c in cells]
                ys = [c[1] for c in cells]
                gcx = (min(xs) + max(xs) + 1) / 2.0
                gcy = (min(ys) + max(ys) + 1) / 2.0
                cx_px = gsx + (gx + gcx) * cs
                cy_px = gsy + (gy + gcy) * cs
                bx = cx_px - img.get_width() / 2
                by = cy_px - img.get_height() / 2
                surf.blit(img, (int(bx), int(by)))

            # 3. 左侧可用图形块列表（blit PNG）
            for index, shape in enumerate(self.puzzle.available_shapes):
                slot_x = self.shapes_start_x
                slot_y = self.shapes_start_y + index * self.slot_gap
                name = shape["name"]
                img = self.shape_images[name]
                surf.blit(img, (int(slot_x), int(slot_y)))

            # 4. 拖拽中的图形块 + 放置预览
            if self.puzzle.dragging_shape:
                shape = self.puzzle.dragging_shape
                cells = shape["cells"]
                mx = self.mouse_x
                my = self.mouse_y

                # 4a. 网格上的放置预览（绿=可放 / 红=越界或撞块）
                gx, gy, in_grid = self._hover_grid(mx, my)
                if in_grid:
                    can = bool(self.puzzle.can_place_shape(gx, gy))
                    prev_color = (39, 174, 96, 120) if can else (231, 76, 60, 120)
                    for (dx, dy) in cells:
                        px = gsx + (gx + dx) * cs
                        py = gsy + (gy + dy) * cs
                        if 0 <= gx + dx < self.puzzle.grid_width and 0 <= gy + dy < self.puzzle.grid_height:
                            pygame.draw.rect(surf, prev_color, (px + 1, py + 1, cs - 2, cs - 2))
                            pygame.draw.rect(surf, (255, 255, 255, 180), (px, py, cs, cs), 1)

                # 4b. 跟随鼠标的工具 PNG（按旋转角度旋转，中心对齐鼠标）
                name = shape["name"]
                rot = shape.get("rotation", 0)
                img = self._rotated_image(name, rot)
                surf.blit(img, (int(mx - img.get_width() / 2), int(my - img.get_height() / 2)))

            rv = renpy.Render(width, height)
            rv.blit(surf, (0, 0))
            # 每帧强制重绘
            renpy.redraw(self, 0)
            return rv

        # ---------- 输入 ----------
        def event(self, ev, x, y, st):
            import pygame

            # 官方建议：优先使用相对坐标（相对本 displayable 左上角）
            self.mouse_x = x
            self.mouse_y = y

            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                # 左键：命中左侧图形块即拿起
                idx = self._hit_shape_slot(x, y)
                if idx is not None:
                    self.puzzle.start_dragging(idx)
                    _play_star_sound()  # 拾起播音效
                    renpy.redraw(self, 0)

            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 3:
                # 右键：取消拖拽（归还图形块）
                if self.puzzle.dragging_shape:
                    self.puzzle.cancel_dragging()
                    renpy.redraw(self, 0)

            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                # 松手：放置到当前吸附格
                if self.puzzle.dragging_shape:
                    gx, gy, in_grid = self._hover_grid(x, y)
                    if in_grid:
                        self.puzzle.place_shape(gx, gy)
                        # 放置成功（拖拽状态被清除）才播音效；失败/越界不播
                        if self.puzzle.dragging_shape is None:
                            _play_star_sound()
                    else:
                        # 拖到网格外松手 = 取消
                        self.puzzle.cancel_dragging()
                    renpy.redraw(self, 0)
                    # 放置/取消后重启交互：刷新 screen 数量文本 + 胜利判定
                    renpy.restart_interaction()

            elif ev.type == pygame.MOUSEMOTION:
                # 拖拽跟手：强制下一帧重绘
                if self.puzzle.dragging_shape:
                    renpy.redraw(self, 0)

            return None

        # ---------- 工具 ----------
        def _hover_grid(self, mx, my):
            """鼠标位置 -> 网格基准格（中心跟随：让形状覆盖鼠标所在格并尽量居中）"""
            cs = self.cell_size
            hx = int((mx - self.grid_start_x) / cs)
            hy = int((my - self.grid_start_y) / cs)
            if hx < 0 or hx >= self.puzzle.grid_width or hy < 0 or hy >= self.puzzle.grid_height:
                return 0, 0, False

            shape = self.puzzle.dragging_shape
            if not shape:
                return hx, hy, True

            xs = [c[0] for c in shape["cells"]]
            ys = [c[1] for c in shape["cells"]]
            w = max(xs) - min(xs) + 1
            h = max(ys) - min(ys) + 1
            gx = hx - w // 2
            gy = hy - h // 2
            return gx, gy, True

        def _hit_shape_slot(self, mx, my):
            """按图形块本身在屏幕上的实际格子位置判断命中（不再用矩形框）"""
            for index, shape in enumerate(self.puzzle.available_shapes):
                slot_x = self.shapes_start_x
                slot_y = self.shapes_start_y + index * self.slot_gap
                for (dx, dy) in shape["cells"]:
                    px = slot_x + dx * self.cell_size
                    py = slot_y + dy * self.cell_size
                    if px <= mx < px + self.cell_size and py <= my < py + self.cell_size:
                        return index
            return None


    # 跨 interaction 复用的 displayable 实例（拖拽状态不因 screen 重建而丢失）
    star_pattern_displayable = None


    def _force_redraw(puzzle):
        """强制 Custom Displayable 下一帧重绘。

        从 puzzle 对象上取 displayable 引用（screen 的 python 块会把实例挂到
        puzzle._displayable 上），不依赖全局变量，避免作用域坑。
        """
        disp = getattr(puzzle, "_displayable", None)
        if disp is not None:
            renpy.redraw(disp, 0)


    def _play_star_sound():
        """播放星纹拾起/放置音效：先停再播，避免连续操作时音效重叠"""
        renpy.sound.stop(channel="sound")
        renpy.sound.play("audio/star_pattern_tap.mp3", channel="sound", loop=False)


    def star_pattern_rotate(puzzle):
        """旋转当前拖拽的图形块，并强制刷新画面（直接传 puzzle，不依赖全局引用）"""
        puzzle.rotate_shape()
        _force_redraw(puzzle)
        renpy.restart_interaction()


    def star_pattern_cancel(puzzle):
        """取消当前拖拽，并强制刷新画面"""
        puzzle.cancel_dragging()
        _force_redraw(puzzle)
        renpy.restart_interaction()


    def star_pattern_reset(puzzle):
        """重置拼图（清空棋盘），并强制刷新画面"""
        puzzle.__init__(6, 6)
        _force_redraw(puzzle)
        empty = sum(row.count(0) for row in puzzle.grid)
        renpy.notify("重置完成：空格数={}".format(empty))
        renpy.restart_interaction()


screen star_pattern_puzzle(puzzle=None):
    zorder 200
    modal True

    default local_puzzle = puzzle

    # 复用全局实例：同一局游戏不重建，拖拽状态保留
    python:
        if star_pattern_displayable is None or star_pattern_displayable.puzzle is not local_puzzle:
            star_pattern_displayable = StarPatternDisplayable(local_puzzle)
        # 把显示层实例挂到 puzzle 上，供动作函数强制重绘（不依赖全局作用域）
        local_puzzle._displayable = star_pattern_displayable

    add "#0008"

    text "星纹密码" size 70 color "#fff" xalign 0.5 ypos 20

    if local_puzzle.game_complete:
        text "拼图完成！星纹密码已解开。" size 50 color "#0f0" xalign 0.5 yalign 0.5
        timer 2.0 action Return("success")

    # 渲染 + 鼠标输入
    add star_pattern_displayable pos (0, 0)

    # 左侧图形块剩余数量（与 displayable 内槽位对齐）
    for index in range(len(local_puzzle.available_shapes)):
        text "[local_puzzle.available_shapes[index]['amount']]" size 35 color "#BDC3C7":
            pos (100 + 250, 100 + index * 180 + 130)

    # 键盘控制（旋转/取消后强制刷新画面）
    key "r" action Function(star_pattern_rotate, local_puzzle)
    key "R" action Function(star_pattern_rotate, local_puzzle)
    key "c" action Function(star_pattern_cancel, local_puzzle)
    key "C" action Function(star_pattern_cancel, local_puzzle)
    key "K_ESCAPE" action Return("quit")

    # 操作说明
    vbox:
        pos (1400, 500)
        spacing 10
        text "操作说明:" size 24 color "#BDC3C7"
        text "1. 左键按住图形，拖到网格松手放置。" size 20 color "#95A5A6"
        text "2. 拖拽中按 R 或右键旋转。" size 20 color "#95A5A6"
        text "3. 右键取消当前拖拽。" size 20 color "#95A5A6"
        text "目标: 用所有图形块填满6x6网格。" size 20 color "#F1C40F"

    # 重置按钮
    textbutton "重置游戏":
        pos (1400, 750)
        action Function(star_pattern_reset, local_puzzle)
        background "#34495E"
        hover_background "#2C3C4D"

    # 退出按钮
    textbutton "退出":
        pos (1600, 750)
        action Return("quit")
        background "#C0392B"
        hover_background "#A93226"


screen debug_info(puzzle=None):
    zorder 1000  # 设置较高的zorder，确保在最上层显示
    modal False  # 非模态，不会阻止交互

    # 星纹拼图状态（仅在星纹锁关卡传入 puzzle 时显示）
    if puzzle:
        frame:
            pos (1400, 20)
            background "#000C"
            padding (10, 10)
            vbox:
                spacing 5
                text "调试信息:" color "#FFF" size 20 bold True
                text "game_complete: [puzzle.game_complete]" color "#FFF" size 18
                text "可用图形块: [len(puzzle.available_shapes)]" color "#FFF" size 18
                # 修正：避免直接显示字典
                $ dragging_name = puzzle.dragging_shape['name'] if puzzle.dragging_shape else '无'
                text "拖拽中: [dragging_name]" color "#FFF" size 18
                $ empty_count = sum(row.count(0) for row in puzzle.grid)
                text "空格数量: [empty_count]" color "#FFF" size 18

    # 快速跳转小游戏（免去过剧情；有拼图时放下方，否则放顶部）
    vbox:
        pos (1400, 280 if puzzle else 20)
        spacing 8
        text "快速跳转:" color "#FFD700" size 18 bold True
        textbutton "小游戏01 星空圆盘":
            action Jump("microgame01")
            background "#333"
            hover_background "#555"
            text_size 18
        textbutton "小游戏02 星纹锁":
            action Jump("microgame02")
            background "#333"
            hover_background "#555"
            text_size 18
        textbutton "小游戏03 华容道":
            action Jump("microgame03")
            background "#333"
            hover_background "#555"
            text_size 18

    # 添加关闭调试信息的按钮
    textbutton "关闭调试":
        pos (1400, 180)
        action Hide("debug_info")
        background "#333"
        hover_background "#555"
