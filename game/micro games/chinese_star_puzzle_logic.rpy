init python:
    import math
    import random

    class MouseHandler(renpy.display.core.Displayable):
        """自定义 Displayable 用于处理鼠标拖拽事件"""
        def __init__(self, game, width=800, height=800, **properties):
            super(MouseHandler, self).__init__(**properties)
            self.game = game
            self.width = width
            self.height = height

        def event(self, ev, x, y, st):
            import pygame
            # 直接使用屏幕绝对坐标
            mx, my = renpy.get_mouse_pos()
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.game.start_drag(mx, my)
            elif ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                self.game.stop_drag()
            elif ev.type == pygame.MOUSEMOTION:
                if self.game.dragging:
                    self.game.drag_disk(mx, my)
                    renpy.restart_interaction()
            return None

        def render(self, width, height, st, at):
            # 渲染一个透明的可交互区域
            render = renpy.display.render.Render(self.width, self.height)
            return render

    class CircleOutline(renpy.display.core.Displayable):
        def __init__(self, color="#FFFFFF", radius=50, thickness=2, alpha=1.0, **properties):
            super(CircleOutline, self).__init__(**properties)
            self.color = color
            self.radius = radius
            self.thickness = thickness
            self.alpha = alpha

        def render(self, width, height, st, at):
            size = self.radius * 2 + self.thickness * 2
            render = renpy.display.render.Render(size, size)
            import pygame
            surf = pygame.Surface((size, size), pygame.SRCALPHA)
            pygame.draw.circle(surf, self.color, (self.radius + self.thickness, self.radius + self.thickness), self.radius, max(1, self.thickness))
            render.blit(surf, (0, 0))
            return render

    class Line(renpy.display.core.Displayable):
        def __init__(self, start=(0, 0), end=(100, 100), color="#FFFFFF", thickness=1, **properties):
            super(Line, self).__init__(**properties)
            self.start = start
            self.end = end
            self.color = color
            self.thickness = thickness

        def render(self, width, height, st, at):
            x1, y1 = self.start
            x2, y2 = self.end
            # 计算线条的边界框
            min_x = min(x1, x2) - self.thickness
            min_y = min(y1, y2) - self.thickness
            max_x = max(x1, x2) + self.thickness
            max_y = max(y1, y2) + self.thickness
            size_x = max(1, int(max_x - min_x))
            size_y = max(1, int(max_y - min_y))
            render = renpy.display.render.Render(size_x, size_y)
            import pygame
            surf = pygame.Surface((size_x, size_y), pygame.SRCALPHA)
            # 在 Surface 内绘制线条（相对于边界框）
            pygame.draw.line(surf, self.color, 
                (int(x1 - min_x), int(y1 - min_y)), 
                (int(x2 - min_x), int(y2 - min_y)), 
                max(1, self.thickness))
            render.blit(surf, (0, 0))
            return render

        def get_placement(self):
            x1, y1 = self.start
            x2, y2 = self.end
            min_x = min(x1, x2) - self.thickness
            min_y = min(y1, y2) - self.thickness
            # 返回位置偏移 (x, y, anchor_x, anchor_y, xoffset, yoffset, subpixel)
            return (min_x, min_y, 0, 0, 0, 0, False)

    # 全局画布统一配置，与屏幕分辨率 1920x1080 对齐
    CANVAS_WIDTH = 1920
    CANVAS_HEIGHT = 1080
    CX = CANVAS_WIDTH // 2  # 960
    CY = CANVAS_HEIGHT // 2 # 540

    # 颜色配置
    STAR_COLORS = {
        'BACKGROUND': '#0A0A12',
        'GOLD': '#FFD700',
        'CYAN': '#00D4FF',
        'MAGENTA': '#FF00AA',
        'WHITE': '#FFFFFF',
        'GRAY': '#808080',
    }

    # 圆盘尺寸配置
    DISK_CONFIG = {
        'ORBIT_RADIUS': 180,
        'TARGET_RADIUS': 200,
        'WIN_THRESHOLD': 15,
        'DISK_RADIUS': 60,
        'CYAN_SCALE': 4.5,
        'MAGENTA_SCALE': 5.25,
    }

    # 恒星目标坐标（相对中心CX/CY）
    # 蓝色圆盘目标（轨道半径180）
    STAR_TARGETS = {
        0: (-156, 90),
        1: (-156, -90),
        2: (156, -90),
    }
    # 红色圆盘目标（轨道半径210）
    STAR_TARGETS_2 = {
        3: (182, 105),
        4: (0, 210),
        5: (-182, 105),
    }
    ALL_STAR_TARGETS = {}
    ALL_STAR_TARGETS.update(STAR_TARGETS)
    ALL_STAR_TARGETS.update(STAR_TARGETS_2)

    class StarPuzzleGame:
        def __init__(self):
            self.reset_game()

        def reset_game(self):
            # 圆盘初始旋转角度
            self.disk1_angle = math.radians(-83)
            self.disk2_angle = math.radians(147)
            # 目标角度（阻尼追踪：实际角度每帧向目标逼近）
            self.disk1_target = self.disk1_angle
            self.disk2_target = self.disk2_angle
            self.stars = []
            # 蓝色圆盘恒星 0/1/2
            blue_base = [5*math.pi/6, 7*math.pi/6, 11*math.pi/6]
            for idx, base_a in enumerate(blue_base):
                self.stars.append({
                    "id": idx,
                    "disk": 1,
                    "base_angle": base_a,
                    "current_angle": base_a - self.disk1_angle,
                    "orbit_radius": DISK_CONFIG["ORBIT_RADIUS"],
                    "target_x": STAR_TARGETS[idx][0],
                    "target_y": STAR_TARGETS[idx][1],
                })
            # 红色圆盘恒星 3/4/5
            red_base = [math.pi/6, math.pi/2, 5*math.pi/6]
            for idx, base_a in enumerate(red_base):
                sid = idx + 3
                self.stars.append({
                    "id": sid,
                    "disk": 2,
                    "base_angle": base_a,
                    "current_angle": base_a - self.disk2_angle,
                    "orbit_radius": DISK_CONFIG["ORBIT_RADIUS"] + 30,
                    "target_x": STAR_TARGETS_2[sid][0],
                    "target_y": STAR_TARGETS_2[sid][1],
                })
            self.selected_disk = None
            self.won = False
            self.dragging = False
            self.last_mouse_angle = 0

        def get_star_position(self, star):
            ang = star["current_angle"]
            r = star["orbit_radius"]
            x = CX + r * math.cos(ang)
            y = CY + r * math.sin(ang)
            return x, y

        def update_star_angles(self):
            for s in self.stars:
                if s["disk"] == 1:
                    s["current_angle"] = s["base_angle"] - self.disk1_angle
                else:
                    s["current_angle"] = s["base_angle"] - self.disk2_angle

        def select_disk_at(self, mx, my):
            dx = mx - CX
            dy = my - CY
            dist = math.hypot(dx, dy)
            cyan_outer = DISK_CONFIG["DISK_RADIUS"] * DISK_CONFIG["CYAN_SCALE"]
            cyan_inner = cyan_outer * 6 / 7
            mag_outer = DISK_CONFIG["DISK_RADIUS"] * DISK_CONFIG["MAGENTA_SCALE"]
            mag_inner = mag_outer * 6 / 7

            if cyan_inner - 10 <= dist <= cyan_outer + 10:
                self.selected_disk = 1
                return
            if mag_inner - 10 <= dist <= mag_outer + 10:
                self.selected_disk = 2
                return
            self.selected_disk = None

        def start_drag(self, mx, my):
            if self.won:
                return
            # 每次点击都重新选择圆盘
            self.select_disk_at(mx, my)
            if self.selected_disk is None:
                return
            self.dragging = True
            dx = mx - CX
            dy = my - CY
            self.last_mouse_angle = math.atan2(dy, dx)

        def drag_disk(self, mx, my):
            if not self.dragging or self.selected_disk is None or self.won:
                return
            dx = mx - CX
            dy = my - CY
            curr_ang = math.atan2(dy, dx)
            # 中心死区：鼠标太靠近盘心时 atan2 角度不可靠，只重新锚定不旋转，
            # 避免扫过中心时盘面/恒星剧烈摆动
            if math.hypot(dx, dy) < 40:
                self.last_mouse_angle = curr_ang
                return
            # 角增量归一化到 (-π, π]：防止鼠标跨 ±180° 边界时盘面瞬间跳转一圈
            delta_ang = (curr_ang - self.last_mouse_angle + math.pi) % (2 * math.pi) - math.pi
            # 灵敏度：盘目标角增量 = 鼠标角增量 * 灵敏度（调低 = 转动更不灵敏）
            sensitivity = 0.45
            if self.selected_disk == 1:
                self.disk1_target += delta_ang * sensitivity
            else:
                self.disk2_target += delta_ang * sensitivity
            self.last_mouse_angle = curr_ang

        def update(self):
            """阻尼推进：实际角度每帧向目标角度按比例逼近（由渲染层每帧调用）。

            damping 为单帧收敛比例，越小盘越"重"、跟随越滞后。
            """
            damping = 0.18
            for axis in ("disk1", "disk2"):
                target = getattr(self, axis + "_target")
                current = getattr(self, axis + "_angle")
                diff = target - current
                if abs(diff) < 1e-4:
                    setattr(self, axis + "_angle", target)
                else:
                    setattr(self, axis + "_angle", current + diff * damping)
            self.update_star_angles()
            self.check_win()

        def stop_drag(self):
            self.dragging = False
            # 松手时一次收敛剩余差值，保证胜利判定立即生效
            self.disk1_angle = self.disk1_target
            self.disk2_angle = self.disk2_target
            self.update_star_angles()
            self.check_win()

        def check_win(self):
            for star in self.stars:
                sx, sy = self.get_star_position(star)
                tx = CX + star["target_x"]
                ty = CY + star["target_y"]
                dist = math.hypot(sx - tx, sy - ty)
                if dist > DISK_CONFIG["WIN_THRESHOLD"]:
                    self.won = False
                    return
            self.won = True

        def get_star_distance(self, star):
            sx, sy = self.get_star_position(star)
            tx = CX + star["target_x"]
            ty = CY + star["target_y"]
            return math.hypot(sx - tx, sy - ty)

        def reset_level(self):
            self.reset_game()
