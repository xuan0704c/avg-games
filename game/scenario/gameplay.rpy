# ============================================================
# 小游戏01：星空圆盘
label microgame01:
    "测试星空圆盘小游戏..."
    $ star_puzzle_game = StarPuzzleGame()
    show screen debug_info

label chinese_star_puzzle_loop:
    call screen chinese_star_puzzle_menu(game=star_puzzle_game)
    $ result = _return

    if result == "quit":
        "退出星空圆盘游戏。"
        return
    elif result == "start":
        call screen chinese_star_puzzle_game(game=star_puzzle_game)
        $ game_result = _return
        if game_result == "back":
            jump chinese_star_puzzle_loop
        elif game_result == "replay":
            $ star_puzzle_game.reset_level()
            call screen chinese_star_puzzle_game(game=star_puzzle_game)
            $ game_result2 = _return
            if game_result2 == "back":
                jump chinese_star_puzzle_loop
        elif game_result == "success":
            jump microgame01_end

    jump microgame01_end
# ============================================================
# 小游戏02：星纹锁
label microgame02:
    "在清理过程中，你发现灯座后盖的锁具上，刻着一个奇特的星纹图案，似乎需要解开它才能打开。"
    # 创建拼图实例
    $ puzzle_instance = StarPatternPuzzle()

    # 【关键修改】使用 call screen 而不是 show screen + pause
    # 注意：debug_info 屏幕可以单独show，因为它不影响主流程
    show screen debug_info(puzzle=puzzle_instance)

    # 调用拼图屏幕并等待返回结果
    call screen star_pattern_puzzle (puzzle=puzzle_instance)
    $ result = _return
    # 面板切回无状态版，保持常驻（不关闭）
    show screen debug_info

    # 根据屏幕返回的结果决定后续流程
    if result == "success":
        jump after_star_puzzle_success
    elif result == "quit":
        jump after_star_puzzle_quit
    else:
        # 理论上不会执行到这里，但为了完整性保留
        "发生了意外情况。"
        "result是[result]"
        return

label after_star_puzzle_success:
    hide screen star_pattern_puzzle
    jump microgame02_end
    return

label after_star_puzzle_quit:
    hide screen star_pattern_puzzle
    "你暂时放弃了研究这个复杂的星纹锁。也许需要更安静的时候再来尝试。"
    "result是[result]"
    return
# ============================================================
# 小游戏03：华容道（随机选关直接开始，4 个简单关卡均 10 步内可解）
label microgame03:
    "测试华容道小游戏..."
    $ huarongdao_game = HuarongDaoGame()
    show screen debug_info
    # 随机选择一关直接开始（不再有选关菜单）
    $ huarongdao_game.start_random_level()

label huarongdao_game_loop:
    call screen huarongdao_game(game=huarongdao_game)
    $ result = _return

    if result == "replay":
        # 再来一关：随机新关
        $ huarongdao_game.start_random_level()
        jump huarongdao_game_loop
    elif result == "success":
        jump microgame03_end
    else:
        # back / 其他：返回剧情
        jump microgame03_end
# ============================================================