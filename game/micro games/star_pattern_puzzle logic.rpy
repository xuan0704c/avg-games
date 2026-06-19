init python:
    import copy

    # 定义几种经典的"星纹"图形块
    SHAPE_DEFINITIONS = {
        "L形": [(0, 0), (1, 0), (2, 0), (2, 1)],
        "Z形": [(0, 0), (1, 0), (1, 1), (2, 1)],
        "T形": [(0, 0), (1, 0), (2, 0), (1, 1)],
        "田字形": [(0, 0), (1, 0), (0, 1), (1, 1)],
        "长条形": [(0, 0), (1, 0), (2, 0), (3, 0)],
    }

    class StarPatternPuzzle:
        def __init__(self, grid_width=6, grid_height=6):
            self.grid_width = grid_width
            self.grid_height = grid_height
            self.grid = [[0 for _ in range(grid_width)] for __ in range(grid_height)]

            self.available_shapes = [
                {"name": "L形", "cells": SHAPE_DEFINITIONS["L形"], "color": "#FF6B6B","amount":6},
                {"name": "Z形", "cells": SHAPE_DEFINITIONS["Z形"], "color": "#4ECDC4","amount":6},
                {"name": "T形", "cells": SHAPE_DEFINITIONS["T形"], "color": "#FFD166","amount":6},
                {"name": "田字形", "cells": SHAPE_DEFINITIONS["田字形"], "color": "#06D6A0","amount":6},
                {"name": "长条形", "cells": SHAPE_DEFINITIONS["长条形"], "color": "#118AB2","amount":6},
            ]

            self.dragging_shape = None
            self.game_complete = False  # 已正确初始化

        def start_dragging(self, shape_index):
            """开始拖拽一个图形块 - 简化版"""
            if shape_index < len(self.available_shapes):
                shape = self.available_shapes[shape_index]
                self.dragging_shape = copy.deepcopy(shape)
                # 从可用列表中移除
                self.available_shapes[shape_index]["amount"] -= 1
                if self.available_shapes[shape_index]["amount"] == 0:
                    self.available_shapes.pop(shape_index)
                return
            return

        def rotate_shape(self):
            """旋转当前拖拽中的图形块 90度"""
            if not self.dragging_shape:
                return
            rotated_cells = [(-y, x) for (x, y) in self.dragging_shape["cells"]]
            min_x = min(c[0] for c in rotated_cells)
            min_y = min(c[1] for c in rotated_cells)
            normalized_cells = [(x - min_x, y - min_y) for (x, y) in rotated_cells]
            self.dragging_shape["cells"] = normalized_cells

        def can_place_shape(self, grid_x, grid_y):
            """判断当前拖拽的图形块是否能放置在网格的(grid_x, grid_y)位置"""
            if not self.dragging_shape:
                return
            for (dx, dy) in self.dragging_shape["cells"]:
                x, y = grid_x + dx, grid_y + dy
                if x < 0 or x >= self.grid_width or y < 0 or y >= self.grid_height:
                    return
                if self.grid[y][x] != 0:
                    return
            return True

        def place_shape(self, grid_x, grid_y):
            """将当前拖拽的图形块放置到网格上"""
            if not self.can_place_shape(grid_x, grid_y):
                return

            for (dx, dy) in self.dragging_shape["cells"]:
                x, y = grid_x + dx, grid_y + dy
                self.grid[y][x] = 1
            #放置成功清除拖拽状态
            self.dragging_shape = None
            # 放置后检查胜利条件
            self.check_victory()
            return

        def check_victory(self):
            """检查是否所有格子都被填满（胜利条件）"""

            # 检查是否还有空格子
            for row in self.grid:
                if 0 in row:  # 如果这一行还有空格
                    self.game_complete = False
                    return

            # 如果没有空格子，且没有可用图形块
#             if len(self.available_shapes) == 0:
                self.game_complete = True
#             else:
#                 self.game_complete = False

        def cancel_dragging(self):
            """取消当前拖拽，将图形块放回可用列表"""
            if not self.dragging_shape:
                return

            shape_name = self.dragging_shape["name"]
            # 在 available_shapes 中查找同名的图形
            found = False
            for shape in self.available_shapes:
                if shape["name"] == shape_name:
                    shape["amount"] += 1
                    found = True
                    break
            # 如果没有找到（说明之前数量为0被移除了），则重新创建一个条目
            if not found:
                # 从 SHAPE_DEFINITIONS 获取原始图形定义
                original_shape = {
                    "name": shape_name,
                    "cells": SHAPE_DEFINITIONS[shape_name],
                    "color": self.dragging_shape["color"],
                    "amount": 1
                }
                self.available_shapes.append(original_shape)

            # 清除拖拽状态
            self.dragging_shape = None