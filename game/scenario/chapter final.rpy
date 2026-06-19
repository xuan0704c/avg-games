# 终章
# Final Chapter

# 角色定义
define p1 = Character("小远")  # 主角
define narrator = Character("")

# 场景：终章 - 笔尖下的传承
label chapter_final:

    scene black
    with fade

    # a1s1: 笔尖写字声 → "你拿起笔，在下面添了一行字"
    play sound "audio/sound/Chapter final/a1s1.mp3" fadeout 0.3

    narrator "你拿起笔，在下面添了一行字"

    # 淡出音效，准备旁白
    scene black
    with fade

    # 终章旁白内容
    narrator "三盏灯，亮了。一块碑，补了。"

    narrator "三百年前，贾永春把玉佩藏在神像背后，把念想留给后人。"

    narrator "七十年前，你爷爷站在永春楼下，对着窗户作了一个长揖。"

    narrator "如今，你站在二郎庙里，把二器一一归位。"

    narrator "古堡的魂，在一代又一代人的手里，从来不曾断过。"

    # 结束画面
    scene black
    with fade

    narrator "—— 终章 · 完 ——"

    # 淡出至黑屏
    scene black
    with fade

return
