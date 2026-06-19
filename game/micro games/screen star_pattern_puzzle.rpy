screen star_pattern_puzzle(puzzle=None):
    zorder 200
    modal True

    # 【关键修改1】将传入的参数固定为屏幕局部变量，确保状态稳定
    default local_puzzle = puzzle

    add "#0008"

    text "星纹密码" size 70 color "#fff" xalign 0.5 ypos 20

    if local_puzzle.game_complete:
        text "拼图完成！星纹密码已解开。" size 50 color "#0f0" xalign 0.5 yalign 0.5
        timer 2.0 action Return("success")

    $ grid_start_x = 800
    $ grid_start_y = 200
    $ cell_size = 80

    # --- 绘制6x6游戏网格 ---
    for y in range(local_puzzle.grid_height):
        for x in range(local_puzzle.grid_width):
            $ pos_x = grid_start_x + x * cell_size
            $ pos_y = grid_start_y + y * cell_size

            # 格子背景
            if local_puzzle.grid[y][x] == 0:
                add Solid("#2C3E50", xsize=cell_size-2, ysize=cell_size-2) pos (pos_x+1, pos_y+1)
            else:
                add Solid("#34495E", xsize=cell_size-2, ysize=cell_size-2) pos (pos_x+1, pos_y+1)

            # 绘制格子边框
            add Solid("#7F8C8D", xsize=cell_size, ysize=1) pos (pos_x, pos_y)
            add Solid("#7F8C8D", xsize=cell_size, ysize=1) pos (pos_x, pos_y+cell_size-1)
            add Solid("#7F8C8D", xsize=1, ysize=cell_size) pos (pos_x, pos_y)
            add Solid("#7F8C8D", xsize=1, ysize=cell_size) pos (pos_x+cell_size-1, pos_y)

    # --- 绘制可用图形块区域 ---
    text "可用的星纹图形:" size 35 color "#BDC3C7" pos (80, 50)

    for index, shape in enumerate(local_puzzle.available_shapes):
        $ shape_start_x = 100
        $ shape_start_y = 100 + index * 180
        $ shape_number_start_x = shape_start_x + 250
        $ shape_number_start_y = shape_start_y + 130
        $ have_shape_number = shape["amount"]
        # 绘制每个图形块的缩略图
        for (dx, dy) in shape["cells"]:
            add Solid(shape["color"], xsize=cell_size-4, ysize=cell_size-4) pos (shape_start_x + dx*cell_size, shape_start_y + dy*cell_size)

        # 图形块的可拖拽按钮
        button:
            xysize (240, 160)
            pos (shape_start_x, shape_start_y)
            background None
            hover_background None
            action Function(local_puzzle.start_dragging, index)
            hovered [Show("shape_hint", message="点击并拖拽此图形")]
            unhovered [Hide("shape_hint")]

        # 图形块的剩余数量
        vbox:
            pos (shape_number_start_x , shape_number_start_y )
            spacing 10
            text "[have_shape_number]" size 35 color "#BDC3C7"




    # --- 绘制当前正在拖拽的图形块（跟随鼠标）---
    if local_puzzle.dragging_shape:
        $ mouse_pos = renpy.get_mouse_pos()
        $ grid_x = int((mouse_pos[0] - grid_start_x) / cell_size)
        $ grid_y = int((mouse_pos[1] - grid_start_y) / cell_size)

        for (dx, dy) in local_puzzle.dragging_shape["cells"]:
            $ preview_x = mouse_pos[0] + dx * cell_size
            $ preview_y = mouse_pos[1] + dy * cell_size
            if local_puzzle.can_place_shape(grid_x, grid_y):
                add Solid("#27AE60", xsize=cell_size-4, ysize=cell_size-4) pos (preview_x, preview_y)
            else:
                add Solid("#E74C3C", xsize=cell_size-4, ysize=cell_size-4) pos (preview_x, preview_y)

        # 键盘按键：R键旋转图形块
        key "R" action Function(local_puzzle.rotate_shape)
        key "C" action Function(local_puzzle.cancel_dragging)
        # 左键点击放置图形块
        button:
            xfill True
            yfill True
            background None
            hover_background None
            action Function(local_puzzle.place_shape, grid_x, grid_y)



    # --- 操作说明 ---
    vbox:
        pos (1400, 500)
        spacing 10
        text "操作说明:" size 24 color "#BDC3C7"
        text "1. 点击左侧的星纹图形，然后移动鼠标到右侧网格中。" size 20 color "#95A5A6"
        text "2. 按 R 键可旋转图形。" size 20 color "#95A5A6"
        text "3. 左键点击网格区域放置图形。" size 20 color "#95A5A6"
        text "4. 右键点击可取消当前拖拽。" size 20 color "#95A5A6"
        text "目标: 用所有图形块填满6x6网格，不留空格。" size 20 color "#F1C40F"

    # 重置按钮
    textbutton "重置游戏":
        pos (1400, 750)
        action Function(local_puzzle.__init__, 6, 6)
        background "#34495E"
        hover_background "#2C3C4D"
    
    # 退出按钮
    textbutton "退出":
        pos (1600, 750)
        # 【关键修改3】退出时返回"quit"标识，而不是直接Jump
        action Return("quit")
        background "#C0392B"
        hover_background "#A93226"

# 提示屏幕
screen shape_hint(message="点击并拖拽"):
    zorder 100
    frame:
        pos renpy.get_mouse_pos()
        background "#000C"
        padding (10, 5)
        text message size 16 color "#FFF"

# debug窗口
screen debug_info(puzzle=None):
    zorder 1000  # 设置较高的zorder，确保在最上层显示
    modal False  # 非模态，不会阻止交互

    if puzzle:  # 只在有拼图实例时显示
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


    # 添加关闭调试信息的按钮
    textbutton "关闭调试":
        pos (1400, 180)
        action Hide("debug_info")
        background "#333"
        hover_background "#555"