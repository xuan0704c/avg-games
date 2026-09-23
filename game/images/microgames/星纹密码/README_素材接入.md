# 星纹密码 · PNG 素材接入说明

> 供迁移工作环境后 agent 快速接入用。改代码前先读这个文件。

## 一、素材文件

位置：`game/images/microgames/星纹密码/`

| 文件 | 基础尺寸 | 出图尺寸(2x) | 对应形状 | 内容 |
|---|---|---|---|---|
| `pat_shape_l_480x320.png` | 240×160 | 480×320 | L形 | 电工折刀 |
| `pat_shape_z_480x320.png` | 240×160 | 480×320 | Z形 | 电烙铁 |
| `pat_shape_t_480x320.png` | 240×160 | 480×320 | T形 | 羊角锤 |
| `pat_shape_square_320x320.png` | 160×160 | 320×320 | 田字形 | 钢丝钳 |
| `pat_shape_bar_640x160.png` | 320×80 | 640×160 | 长条形 | 螺丝刀 |
| `pat_board_960x960.png` | 480×480 | 960×960 | 棋盘底板（**已弃用**） | 木门棋盘 |

全部 PNG，RGBA 透明底，新海诚赛璐璐手绘风。底板已弃用（网格改由程序绘制），文件保留但不加载。

## 二、涉及的代码文件

1. **逻辑层**：`game/micro games/star_pattern_puzzle logic.rpy`
2. **渲染层**：`game/micro games/screen star_pattern_puzzle.rpy`

## 三、逻辑层改动点

### 3.1 SHAPE_IMAGES 映射（文件顶部）

```python
SHAPE_IMAGES = {
    "L形":   "images/microgames/星纹密码/pat_shape_l_480x320.png",
    "Z形":   "images/microgames/星纹密码/pat_shape_z_480x320.png",
    "T形":   "images/microgames/星纹密码/pat_shape_t_480x320.png",
    "田字形": "images/microgames/星纹密码/pat_shape_square_320x320.png",
    "长条形": "images/microgames/星纹密码/pat_shape_bar_640x160.png",
}
```

路径相对 `game/` 目录，文件名必须和实际文件一致。

### 3.2 placed_blocks 列表

`__init__` 里新增 `self.placed_blocks = []`，记录已放置块：

```python
{"name": "L形", "gx": 0, "gy": 0, "rotation": 0, "cells": [...]}
```

- `gx, gy`：基准格坐标（cells 中 (0,0) 对应的网格位置）
- `rotation`：0/1/2/3，顺时针旋转 90° 的次数
- `cells`：旋转后的格子坐标（碰撞检测用）

### 3.3 各方法改动

| 方法 | 改动 |
|---|---|
| `start_dragging` | deepcopy 后加 `self.dragging_shape["rotation"] = 0` |
| `rotate_shape` | 末尾加 `self.dragging_shape["rotation"] = (rotation + 1) % 4` |
| `place_shape` | 放置成功后 append 到 `placed_blocks` |
| `__init__`（重置） | `placed_blocks = []` 自动清空 |

**不变的部分**：`grid` 数组（碰撞检测仍写 color）、`can_place_shape`、`check_victory`、`cancel_dragging`——全不动。

## 四、渲染层改动点

### 4.1 __init__ → _load_images()

用 `renpy.load_surface()` 加载 PNG，`pygame.transform.smoothscale()` 缩到基础尺寸：

```python
base_sizes = {
    "L形":   (3*80, 2*80),   # 240×160
    "Z形":   (3*80, 2*80),
    "T形":   (3*80, 2*80),
    "田字形": (2*80, 2*80),  # 160×160
    "长条形": (4*80, 1*80),  # 320×80
}
```

底板加载已注释掉。

### 4.2 _rotated_image() 旋转缓存

```python
def _rotated_image(self, name, rotation):
    # rotation 0/1/2/3
    # angle = -rotation * 90（pygame 逆时针为正，顺时针 90° = -90°）
    # 用字典缓存避免每帧重复旋转
```

### 4.3 render() 绘制顺序

1. **网格**：程序画，深色半透明填充 + 灰线
2. **已放置块**：遍历 `placed_blocks`，按 rotation 取旋转图，blit 到 `(gsx + gx*cs, gsy + gy*cs)` 居中
3. **左侧可用块**：blit 原始 PNG 到 slot 位置
4. **拖拽中块**：
   - 放置预览：绿/红半透明格（保留）
   - 工具 PNG 跟鼠标，中心对齐 `(mx, my)`

### 4.4 旋转后居中计算

```python
orig = self.shape_images[name]
# 基准格左上角 + 原始中心 = 旋转中心
base_x = gsx + gx * cs + orig.get_width() // 2
base_y = gsy + gy * cs + orig.get_height() // 2
# 旋转后左上角 = 旋转中心 - 旋转图尺寸/2
bx = base_x - img.get_width() // 2
by = base_y - img.get_height() // 2
```

拖拽中简化：`blit(img, (mx - w/2, my - h/2))`。

## 五、注意事项

- **碰撞检测不变**：`grid` 数组 + `cells` 坐标仍走原逻辑，视觉层不影响逻辑
- **图片路径**：中文目录名 `星纹密码`，Ren'Py 的 `renpy.load_surface()` 支持，不用改
- **重置游戏**：`star_pattern_reset` 调 `puzzle.__init__(6,6)`，`placed_blocks` 自动清空
- **底板 PNG**：`pat_board_960x960.png` 文件保留但不加载，需要时取消注释 `_load_images` 里的底板代码并在 render() 里 blit
- **2x 超采样**：出图尺寸是基础尺寸的 2 倍，运行时缩到基础尺寸，高分屏不糊

## 六、验证清单

- [ ] 左侧五件工具正确显示（折刀/电烙铁/羊角锤/钢丝钳/螺丝刀）
- [ ] 拖拽跟手，R 键旋转 90° 后工具方向正确
- [ ] 放置到网格后工具位置和格子对齐
- [ ] 重置后棋盘清空、placed_blocks 清空
- [ ] 胜利判定正常（grid 填满即完成）
