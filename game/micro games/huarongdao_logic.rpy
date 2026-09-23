init python:
    import json
    import os
    import random

    # 颜色定义 - 张壁古堡风格配色
    HUARONG_COLORS = {
        'background': '#8B7765',
        'board': '#A08C78',
        'border': '#503C28',
        'cao_cao': '#B22222',
        'guan_yu': '#DAF520',
        'general': '#6B8E23',
        'soldier': '#A9A9A9',
        'text': '#FFFFFF',
        'exit': '#006400',
        'title': '#8B4513',
        'locked': '#646464',
        'unlocked': '#009600',
        'button': '#B49678',
        'button_hover': '#C8AA86',
    }

    # 游戏设置
    BOARD_WIDTH = 4
    BOARD_HEIGHT = 5
    CELL_SIZE = 100

    # 方块类型定义
    BLOCK_TYPES = {
        'main': {'width': 2, 'height': 2, 'color': HUARONG_COLORS['cao_cao']},
        'gate': {'width': 2, 'height': 1, 'color': HUARONG_COLORS['guan_yu']},
        'general_v': {'width': 1, 'height': 2, 'color': HUARONG_COLORS['general']},
        'general_h': {'width': 2, 'height': 1, 'color': HUARONG_COLORS['general']},
        'soldier': {'width': 1, 'height': 1, 'color': HUARONG_COLORS['soldier']},
    }

    # 关卡数据 —— 重新设计：4 个简单关卡，BFS 验证最短解 3/5/6/5 步，均 <=10 步
    HUARONG_LEVELS = [
        {
            'id': 1,
            'name': '轻装简行',
            'description': '真武殿一路向下，3步直达出口',
            'blocks': [
                {'type': 'main', 'name': '真武殿', 'x': 1, 'y': 0},
                {'type': 'general_v', 'name': '魁星楼', 'x': 0, 'y': 0},
                {'type': 'soldier', 'name': '琉璃碑', 'x': 3, 'y': 0},
                {'type': 'soldier', 'name': '古槐', 'x': 0, 'y': 2},
                {'type': 'soldier', 'name': '地道口', 'x': 3, 'y': 2},
                {'type': 'soldier', 'name': '南门楼', 'x': 0, 'y': 4},
                {'type': 'soldier', 'name': '古堡墙', 'x': 3, 'y': 4},
            ],
            'completed': False,
            'best_moves': None,
            'locked': False,
        },
        {
            'id': 2,
            'name': '双卒挡道',
            'description': '两个士兵挡路，移开即可，5步通关',
            'blocks': [
                {'type': 'main', 'name': '真武殿', 'x': 1, 'y': 0},
                {'type': 'soldier', 'name': '琉璃碑', 'x': 1, 'y': 2},
                {'type': 'soldier', 'name': '古槐', 'x': 2, 'y': 2},
                {'type': 'general_v', 'name': '魁星楼', 'x': 0, 'y': 0},
                {'type': 'soldier', 'name': '南门楼', 'x': 0, 'y': 4},
                {'type': 'soldier', 'name': '古堡墙', 'x': 3, 'y': 4},
            ],
            'completed': False,
            'best_moves': None,
            'locked': False,
        },
        {
            'id': 3,
            'name': '三卒列阵',
            'description': '三兵分散挡路，依次移开，6步通关',
            'blocks': [
                {'type': 'main', 'name': '真武殿', 'x': 1, 'y': 0},
                {'type': 'soldier', 'name': '琉璃碑', 'x': 1, 'y': 2},
                {'type': 'soldier', 'name': '古槐', 'x': 2, 'y': 3},
                {'type': 'soldier', 'name': '地道口', 'x': 1, 'y': 3},
                {'type': 'general_v', 'name': '魁星楼', 'x': 3, 'y': 0},
                {'type': 'soldier', 'name': '南门楼', 'x': 0, 'y': 4},
            ],
            'completed': False,
            'best_moves': None,
            'locked': False,
        },
        {
            'id': 4,
            'name': '将挡之路',
            'description': '将军竖挡去路，移开它，5步通关',
            'blocks': [
                {'type': 'main', 'name': '真武殿', 'x': 1, 'y': 0},
                {'type': 'general_v', 'name': '古地道', 'x': 1, 'y': 2},
                {'type': 'soldier', 'name': '琉璃碑', 'x': 2, 'y': 2},
                {'type': 'general_v', 'name': '魁星楼', 'x': 3, 'y': 0},
                {'type': 'soldier', 'name': '南门楼', 'x': 0, 'y': 4},
                {'type': 'soldier', 'name': '古堡墙', 'x': 3, 'y': 4},
            ],
            'completed': False,
            'best_moves': None,
            'locked': False,
        },
    ]

    PROGRESS_FILE = 'game/huarongdao_progress.json'


    class HuarongBlock:
        """华容道方块类"""
        def __init__(self, name, x, y, width, height, color):
            self.name = name
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
            self.selected = False

        def contains_point(self, px, py):
            """检查点(px, py)是否在方块范围内"""
            return self.x <= px < self.x + self.width and self.y <= py < self.y + self.height


    class HuarongDaoGame:
        """华容道游戏类"""
        def __init__(self):
            self.current_level = 0
            self.blocks = []
            self.selected_block = None
            self.moves = 0
            self.won = False
            self.load_progress()

        def load_progress(self):
            """加载游戏进度"""
            if os.path.exists(PROGRESS_FILE):
                try:
                    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                        progress = json.load(f)
                        for i, level in enumerate(HUARONG_LEVELS):
                            if i < len(progress):
                                level['completed'] = progress[i].get('completed', False)
                                level['best_moves'] = progress[i].get('best_moves', None)
                except:
                    pass

        def save_progress(self):
            """保存游戏进度"""
            progress = []
            for level in HUARONG_LEVELS:
                progress.append({
                    'completed': level.get('completed', False),
                    'best_moves': level.get('best_moves', None),
                })
            try:
                with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
                    json.dump(progress, f)
            except:
                pass

        def init_blocks(self, level_idx):
            """初始化关卡方块"""
            self.current_level = level_idx
            self.blocks = []
            self.moves = 0
            self.won = False
            self.selected_block = None

            level = HUARONG_LEVELS[level_idx]
            for block_data in level['blocks']:
                block_type = BLOCK_TYPES.get(block_data['type'], BLOCK_TYPES['soldier'])
                self.blocks.append(HuarongBlock(
                    block_data['name'],
                    block_data['x'],
                    block_data['y'],
                    block_type['width'],
                    block_type['height'],
                    block_type['color']
                ))

        def get_occupied_cells(self, exclude_block=None):
            """获取被占用的格子坐标集合"""
            occupied = set()
            for block in self.blocks:
                if block != exclude_block:
                    for dx in range(block.width):
                        for dy in range(block.height):
                            occupied.add((block.x + dx, block.y + dy))
            return occupied

        def can_move(self, block, dx, dy):
            """检查方块是否可以移动"""
            new_x = block.x + dx
            new_y = block.y + dy

            # 检查边界
            if new_x < 0 or new_x + block.width > BOARD_WIDTH:
                return False
            if new_y < 0 or new_y + block.height > BOARD_HEIGHT:
                return False

            # 检查是否被其他方块阻挡
            occupied = self.get_occupied_cells(block)
            for x in range(new_x, new_x + block.width):
                for y in range(new_y, new_y + block.height):
                    if (x, y) in occupied:
                        return False

            return True

        def move_block(self, dx, dy):
            """移动选中的方块"""
            if not self.selected_block or self.won:
                return

            if self.can_move(self.selected_block, dx, dy):
                self.selected_block.x += dx
                self.selected_block.y += dy
                self.moves += 1
                self.check_win()

        def move_block_steps(self, dx, dy, steps):
            """沿方向滑动 steps 格（逐格校验，返回实际移动格数；供拖拽落格使用）"""
            if not self.selected_block or self.won:
                return 0
            moved = 0
            for _ in range(steps):
                if self.can_move(self.selected_block, dx, dy):
                    self.selected_block.x += dx
                    self.selected_block.y += dy
                    moved += 1
                else:
                    break
            if moved:
                self.moves += moved
                self.check_win()
            return moved

        def check_win(self):
            """检查是否获胜 - 真武殿到达出口位置(1,3)"""
            if len(self.blocks) == 0:
                return

            main_temple = self.blocks[0]
            if main_temple.x == 1 and main_temple.y == 3:
                self.won = True
                level = HUARONG_LEVELS[self.current_level]
                level['completed'] = True
                if level['best_moves'] is None or self.moves < level['best_moves']:
                    level['best_moves'] = self.moves
                self.save_progress()

        def select_block_at(self, grid_x, grid_y):
            """在指定网格位置选择方块"""
            for block in self.blocks:
                if block.contains_point(grid_x, grid_y):
                    if self.selected_block == block:
                        # 取消选择
                        self.selected_block.selected = False
                        self.selected_block = None
                    else:
                        # 取消之前的选择
                        if self.selected_block:
                            self.selected_block.selected = False
                        # 选中新方块
                        self.selected_block = block
                        block.selected = True
                    return
            # 点击空白处，取消选择
            if self.selected_block:
                self.selected_block.selected = False
                self.selected_block = None
            return

        def reset_level(self):
            """重置当前关卡"""
            self.init_blocks(self.current_level)

        def start_random_level(self):
            """随机选择一关开始（4 个简单关卡，均 10 步内可解）"""
            idx = random.randint(0, len(HUARONG_LEVELS) - 1)
            self.init_blocks(idx)

        def get_next_level(self):
            """获取下一个可用的关卡索引"""
            next_level = self.current_level + 1
            if next_level < len(HUARONG_LEVELS):
                next_level_data = HUARONG_LEVELS[next_level]
                if not next_level_data.get('locked', False):
                    return next_level
            return None

        def handle_board_click(self, grid_start_x, grid_start_y, cell_size):
            """处理棋盘点击事件"""
            mouse_x, mouse_y = renpy.get_mouse_pos()
            grid_x = int((mouse_x - grid_start_x) / cell_size)
            grid_y = int((mouse_y - grid_start_y) / cell_size)
            self.select_block_at(grid_x, grid_y)
