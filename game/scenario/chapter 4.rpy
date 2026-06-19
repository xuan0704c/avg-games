# 第四章：龙鹤福·守口如瓶
# 【未找到第四章完整剧情文本，根据音效标注推测场景】

# 角色定义
define p1 = Character("小远")  # 主角
define p3 = Character("村支书")  # 张建国
define narrator = Character("")

# 场景1：晨光中的古堡石板路
label chapter4_start:
    scene black
    with fade

    # a1s3: 石板路上的脚步声 → "晨光洒在古堡的石板路上"
    play sound "audio/sound/Chapter 4/a1s3.MP3" fadeout 0.3

    narrator "晨光洒在古堡的石板路上"

    # a1s1: 搪瓷杯轻放桌面的碰撞声 → "村支书端着搪瓷杯"
    play sound "audio/sound/Chapter 4/a1s1.MP3" fadeout 0.3

    narrator "村支书端着搪瓷杯，从屋内走出，在石桌前坐下。"

    p3 "小远啊，来，坐。"

    narrator "他将搪瓷杯轻轻放在桌上，杯中的水还冒着热气。"

    # a1s2: 翻笔记本的沙沙声 → "你翻开笔记本"
    play sound "audio/sound/Chapter 4/a1s2.MP3" fadeout 0.3

    narrator "你翻开笔记本，纸页已经有些泛黄。"

    p1 "张叔，这笔记本里……记的都是什么？"

    p3 "都是些老黄历了。村里的事儿，一笔一笔都记着。"

    narrator "他的目光落在笔记本上，神情有些恍惚。"

# 场景2：发现纸条与刻痕
    # a3s1: 纸张展开的轻响 → "笔记里夹着一张泛黄的小纸条"
    play sound "audio/sound/Chapter 4/a3s1.MP3" fadeout 0.3

    narrator "笔记里夹着一张泛黄的小纸条，边缘已经卷曲。"

    p1 "这是……？"

    p3 "……那是当年留下的。"

    narrator "你小心翼翼地将纸条展开，上面的字迹已经模糊不清。"

    # a3s2: 指尖抚摸砖缝的摩擦声 → "轻轻抚摸着那两道几乎看不见的刻痕"
    play sound "audio/sound/Chapter 4/a3s2.MP3" fadeout 0.3

    narrator "轻轻抚摸着那两道几乎看不见的刻痕，指尖传来砖缝的粗糙感。"

    narrator "那是两个简单的符号，像是某种标记，又像是某种约定。"

    p1 "张叔，这些刻痕……是什么意思？"

    p3 "……"

    narrator "村支书沉默了。"

# 场景3：递纸条与长叹
    # a4s1: 纸张翻动的沙沙声 → "你递过纸条"
    play sound "audio/sound/Chapter 4/a4s1.MP3" fadeout 0.3

    narrator "你递过纸条。"

    # a4s1: 叹气声 → "村支书长叹一声"
    play sound "audio/sound/Chapter 4/a4s1.MP3" fadeout 0.3

    narrator "村支书长叹一声。"

    p3 "有些事，埋了太久了……"

    narrator "他接过纸条，浑浊的眼睛里闪过一丝复杂的光。"

    p3 "你知道龙鹤福吗？"

    p1 "……龙鹤福？"

    p3 "那是当年这古堡里住着的一户人家。"

    narrator "他抬起头，望向远处的山影。"

    p3 "他们留下的东西……不该被找到。"

    narrator "风吹过古堡的废墟，卷起几片枯叶。"

    pass  # 【游戏触发预留位置：此处可能触发记忆碎片小游戏或剧情选择】

    narrator "纸条在他手中微微颤抖。"

    p3 "守口如瓶……当年他们就是这么说的。"

    narrator "他将纸条小心翼翼地折好，放回笔记本中。"

    p3 "小远，有些秘密，埋着比挖出来好。"

    narrator "他站起身，端起搪瓷杯，向屋内走去。"

    p1 "张叔——"

    p3 "去吧。"

    narrator "他的背影消失在门后。"

    # 【游戏触发预留位置：此处可能触发记忆拼图或对话选择】

    scene black with fade
    
    # 跳转至第五章
    call chapter5_start
