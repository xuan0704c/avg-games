# 游戏入口脚本
# 张壁古堡 - 星象启秘

init python:
    config.version = "1.0.0"

# 开始游戏
label start:
    play music "audio/VN Intro.mp3"
    scene black with fade
    # 游戏标题画面
    show text "张壁古堡·星象启秘" at Position(xpos=0.5, ypos=0.4, xanchor=0.5)
    with fade
    
    pause 2

    hide text
    scene black with fade
    
    # 进入第一章
    call chapter1_act1
    
    return
