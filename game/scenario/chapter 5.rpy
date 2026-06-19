# 第五章：永春楼·月影守诺
# 【未找到第五章完整剧情文本，根据音效标注构建场景】

# 角色定义
define p1 = Character("小远")  # 主角
define narrator = Character("")

# 场景1：永春楼·风铃轻响
label chapter5_start:
    scene black
    with fade

    # a1s1: 风铃的轻响声 → "风铃轻响"
    play sound "audio/sound/Chapter 5/a1s1.mp3" fadeout 0.3

    narrator "风铃轻响，清脆的声音在夜风中回荡。"

    # a1s2: 走路声 → "你低头看向脚下的青石板"
    play sound "audio/sound/Chapter 5/a1s2.mp3" fadeout 0.3

    narrator "你低头看向脚下的青石板，月光将你的影子拉得很长。"

    narrator "永春楼的轮廓在夜色中若隐若现，飞檐翘角上挂着的风铃正轻轻摇曳。"

    narrator "你握着玉佩，从永春楼里出来。"

# 场景2：发现机关
    # a2s1: 砖石摩擦轻响+轻微磕碰声 → "你试着撬动那块砖"
    play sound "audio/sound/Chapter 5/a2s1.mp3" fadeout 0.3

    narrator "你试着撬动那块砖，指尖感受到砖石冰冷的触感。"

    narrator "砖块松动了一下，发出轻微的磕碰声。"

    # a2s2: 老旧木楼梯吱呀声 → "楼梯在脚下吱呀作响"
    play sound "audio/sound/Chapter 5/a2s2.mp3" fadeout 0.3

    narrator "你沿着老旧的木楼梯向上走去，楼梯在脚下吱呀作响。"

    # a2s3: 机关卡扣弹开的咔哒声 → "那块木料陷了下去露出一个巴掌大的暗格"
    play sound "audio/sound/Chapter 5/a2s3.mp3" fadeout 0.3

    narrator "你按下一处看似普通的木纹，那块木料陷了下去，露出一个巴掌大的暗格。"

    narrator "机关卡扣弹开，发出一声清脆的咔哒声。"

    narrator "暗格中静静躺着一枚泛黄的纸卷。"

# 场景3：月下承诺
    # a3s1: 轻而干脆的拍肩声 → "他站起身，拍了拍你的肩"
    play sound "audio/sound/Chapter 5/a3s1.mp3" fadeout 0.3

    narrator "他站起身，拍了拍你的肩。"

    # a3s2: 模糊，嘈杂的背景音 → "窗外人声鼎沸"
    play sound "audio/sound/Chapter 5/a3s2.mp3" fadeout 0.3

    narrator "窗外人声鼎沸，灯火阑珊处是永春楼特有的热闹。"

    narrator "月光透过雕花窗棂洒进来，在地上投下斑驳的光影。"

    # a3s3: 刻刀划过木头的沙沙声 → "在木料上刻下一行字"
    play sound "audio/sound/Chapter 5/a3s3.mp3" fadeout 0.3

    narrator "你拿起刻刀，在木料上刻下一行字。"

    narrator "刻刀划过木头，发出沙沙的声响。"

    narrator "那一行字迹，是一个尘封多年的承诺。"

    # a3s4: 急促脚步声 → "你冲到窗前"
    play sound "audio/sound/Chapter 5/a3s4.mp3" fadeout 0.3

    narrator "你冲到窗前，望向楼下的街道。"

# 场景4：暗夜追踪
    # a3s5: 微弱风声，远处虫鸣 → "周围一片漆黑。只有微弱的月光"
    play sound "audio/sound/Chapter 5/a3s5.mp3" fadeout 0.3

    narrator "周围一片漆黑。只有微弱的月光从云层后透出。"

    narrator "远处传来虫鸣，风声呜咽。"

    # a3s6: 压低的脚步声+布料摩擦声 → "几十个人影贴着墙根移动"
    play sound "audio/sound/Chapter 5/a3s6.mp3" fadeout 0.3

    narrator "几十个人影贴着墙根移动，脚步声压得很低。"

    narrator "布料摩擦的声音在寂静中格外清晰。"

    narrator "你屏住呼吸，注视着那些黑影的动向。"

# 场景5：晨曦初现
    # a3s7: 温暖的鸟鸣声 → "阳光明媚"
    play sound "audio/sound/Chapter 5/a3s7.mp3" fadeout 0.3

    narrator "阳光明媚，温暖的阳光驱散了夜晚的寒意。"

    # a3s8: 风吹树叶的轻响 → (part of a3s9+a3s11)
    play sound "audio/sound/Chapter 5/a3s8.mp3" fadeout 0.3

    # a3s9: 风吹树叶的轻响 → "阳光明媚"
    play sound "audio/sound/Chapter 5/a3s9.mp3" fadeout 0.3

    narrator "阳光洒在永春楼的青瓦上，折射出柔和的光晕。"

    # a3s11: 温暖的鸟鸣声+风吹树叶的轻响 → "阳光明媚"
    play sound "audio/sound/Chapter 5/a3s11.mp3" fadeout 0.3

    narrator "鸟鸣声清脆悦耳，风吹过树叶发出轻响。"

    narrator "新的一天开始了，而你手中的玉佩似乎在微微发热。"

    pass  # 【游戏触发预留位置：此处可能触发解谜小游戏或剧情对话】

# 场景6：崩塌
    # a3s12: 低沉，轻微的崩塌声 → "周围的一切开始崩塌"
    play sound "audio/sound/Chapter 5/a3s12.mp3" fadeout 0.3

    narrator "周围的一切开始崩塌。"

    narrator "永春楼的梁柱发出不堪重负的呻吟，灰尘簌簌落下。"

    narrator "你握紧玉佩，在崩塌中寻找出路……"

    pass  # 【游戏触发预留位置：此处可能触发逃脱小游戏或关键选择】

# 支线：槐抱柳
label chapter5_sidequest_start:
    scene black
    with fade

    # a3s9: 风吹树叶的沙沙声+清脆的鸟鸣 → "清晨的阳光洒在这棵古老的树上"
    play sound "audio/sound/Chapter 5S/a3s9.mp3" fadeout 0.3

    narrator "清晨的阳光洒在这棵古老的槐树上，金色的光芒穿过枝叶的缝隙。"

    # a3s11: 风吹树叶的沙沙声+清脆的鸟鸣 → "清晨的阳光洒在这棵古老的树上"
    play sound "audio/sound/Chapter 5S/a3s11.mp3" fadeout 0.3

    narrator "槐树粗壮的枝干上缠绕着一株古柳，柳丝垂落，形成独特的奇观。"

    narrator "这就是传说中的\"槐抱柳\"。"

    # a3s13: 麻雀的细碎，短促的啾鸣声 → "几只麻雀在枝头跳来跳去"
    play sound "audio/sound/Chapter 5S/a3s13.mp3" fadeout 0.3

    narrator "几只麻雀在枝头跳来跳去，发出细碎的啾鸣声。"

    narrator "阳光温暖，空气清新，一切都显得那么宁静祥和。"

    # a3s14: 沉稳的折扇合盖声 → "守护灵合上折扇"
    play sound "audio/sound/Chapter 5S/a3s14.mp3" fadeout 0.3

    narrator "守护灵合上折扇，微笑地看着你。"

    narrator "这棵树，已经守望了三百多年了。"

    # 支a3s1: 手指摩擦粗糙树干的粗粝触感声 → "伸手摸了摸树干"
    play sound "audio/sound/Chapter 5S/支a3s1.mp3" fadeout 0.3

    narrator "你伸手摸了摸树干，粗糙的树皮在指尖留下粗粝的触感。"

    narrator "那些凹凸不平的纹路，仿佛在诉说着岁月的沧桑。"

    narrator "守护灵轻摇折扇，目光悠远。"

    narrator "当年，这里曾有一对恋人在此定情……"

    narrator "他顿了顿，眼中闪过一丝怀念。"

    narrator "他们约定，每年槐花开时，都要在此相见。"

    narrator "风穿过槐柳的枝叶，发出轻柔的沙沙声。"

    pass  # 【游戏触发预留位置：此处可能触发记忆场景或对话选择】

    # 支a4s1: 木牌的晃动声 → "把木牌挂在槐树的枝头"
    play sound "audio/sound/Chapter 5S/支a4s1.mp3" fadeout 0.3

    narrator "你把木牌挂在槐树的枝头，木牌在风中轻轻晃动。"

    narrator "阳光透过树叶的缝隙洒在木牌上，那上面刻着的字迹清晰可见。"

    narrator "这是你对那段往事的见证，也是对未来的承诺。"

    narrator "守护灵看着木牌微微点头，眼中满是欣慰。"

    narrator "槐抱柳下，往事如风，但有些承诺，却会一直守望下去。"

    pass  # 【游戏触发预留位置：支线任务完成，奖励结算】

    scene black with fade
    
    # 跳转至第六章
    call chapter6_act1
