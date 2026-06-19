# 第二章：可罕庙·高台藏忠

# 角色定义
define p1 = Character("小远")  # 主角
define p2 = Character("爷爷")  # 张明月（只在日记/回忆中出现）
define p3 = Character("村支书")  # 张建国
define guardian = Character("守护灵")  # 古堡守护之灵
define professor = Character("王教授")  # 文物局专家
define narrator = Character("")

# 【未找到第二章对应场景图片，使用c1s1代替】
init:
    image bg chapter2 = "chapter1/c1s1.png"

# ============================================================
# 第一幕：高台上的守望
# ============================================================
label chapter2_act1:
    scene black
    narrator "时间：暑假清晨"
    narrator "地点：可罕庙山门外"
    narrator "音效：鸡鸣声、喘气声、石阶脚步声"

    show bg chapter2 at Position(xfill=True, yfill=True)

    # 鸡鸣声
    play sound "audio/sound/Chapter 2/a1s1 (2).mp3" fadeout 0.3
    narrator "晨雾渐散，可罕庙的青砖高台从薄雾中显露。"

    # 村支书喘气走上来
    play sound "audio/sound/Chapter 2/a1s2 (2).mp3" fadeout 0.3
    narrator "村支书喘着气走上来，手里拎着两袋油条。"

    show p3 at Position(xpos=0.5, ypos=0.95, yanchor=1.0)
    p3 "小远，你真想亲眼看看可罕庙？"

    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    p1 "嗯，爷爷的日记里老提到这里，我一直想来。"

    hide p1
    p3 "这可罕庙啊，修在三丈高墙上，南缘凸出堡墙外，位置特殊得很。"

    # 爷爷日记（回忆）
    show p2 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    narrator "爷爷的日记里写道："
    p2 "可罕庙是古堡的眼睛，站在高台上能看到四十里外的敌情。"

    narrator "另一页写道："
    p2 "可罕是谁，不重要。重要的是，汉人给他烧了三百年的香。"

    hide p2
    p3 "这香火啊，不在乎是汉是胡，只在乎有没有庇佑一方。"

    narrator "古堡的胸怀比城墙更宽广。"

    p3 "来，先吃根油条，我带你进去。正殿里有块碑，你爷爷生前研究过。"

    # 石阶脚步声
    play sound "audio/sound/Chapter 2/a4s1.mp3" fadeout 0.3
    narrator "跟着村支书踏上石阶。"

    hide p3
    hide p1

    jump chapter2_act2


# ============================================================
# 第二幕：碑文里的答案
# ============================================================
label chapter2_act2:
    scene black
    narrator "地点：可罕庙·正殿前"
    narrator "音效：梁柱轻微回响"

    show bg chapter2 at Position(xfill=True, yfill=True)

    # 梁柱轻微回响
    play sound "audio/sound/Chapter 2/a3s1 (2).mp3" fadeout 0.3
    narrator "正殿前石碑斑驳，碑文模糊。"

    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    narrator "小远拂去尘土，辨认碑文。"

    # 【GAME触发】碑文填空游戏
    pass  # 【游戏触发预留位置：碑文填空游戏】

    narrator "念出碑文："
    narrator "「有其举之，莫敢废也」"

    show p5 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    guardian "这句话的意思是——既然立了庙供了神，就不能废。"

    guardian "融合不是写在圣旨里，是烧在香火里的。"

    narrator "【获得道具】爷爷的日记《张壁往事·二》"

    menu:
        "询问守护灵可罕庙的军事作用":
            jump chapter2_act3a
        "问村支书庙里还有什么线索":
            jump chapter2_act3b

    jump chapter2_act3


# ============================================================
# 第三幕：正殿里的军机
# ============================================================
label chapter2_act3:
    scene black
    narrator "地点：可罕庙·正殿"
    narrator "音效：梁柱轻微回响"

    show bg chapter2 at Position(xfill=True, yfill=True)

    play sound "audio/sound/Chapter 2/a3s1 (2).mp3" fadeout 0.3
    narrator "正殿内供奉可罕像，身披甲胄，目光如炬。"

    guardian "这便是可罕像，既是神，也是将。"

    guardian "殿内的立柱排列得极为规整，间距相等。"

    guardian "你可知道，这正是军事指挥中枢的布局？"

    guardian "柱身凹槽是架设指挥台的卡口。"

    # 【GAME触发】地图探索游戏（左左右前等方向移动）
    pass  # 【游戏触发预留位置：地图探索游戏】

    narrator "【获得道具】正殿军事布局图"

    menu:
        "询问守护灵民族融合与军事的关系":
            jump chapter2_act4a
        "继续观察殿内军事设施":
            jump chapter2_act4b

    jump chapter2_act4


label chapter2_act3a:
    show p5 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    guardian "军事与融合，从不是对立之事。"
    guardian "守土者不论汉胡，百姓要的只是安居乐业。"
    jump chapter2_act4

label chapter2_act3b:
    show p3 at Position(xpos=0.5, ypos=0.95, yanchor=1.0)
    p3 "对了，后墙根那边还有些碑刻，王教授正在那边研究呢。"
    jump chapter2_act4


# ============================================================
# 第四幕：墙根的碑刻
# ============================================================
label chapter2_act4:
    scene black
    narrator "地点：可罕庙·正殿后墙碑刻群"
    narrator "音效：脚步声"

    show bg chapter2 at Position(xfill=True, yfill=True)

    # 脚步声
    play sound "audio/sound/Chapter 2/a4s1.mp3" fadeout 0.3
    narrator "正殿后墙根，青石碑刻一字排开。"

    narrator "反复提到「可罕佑之」。"

    show professor at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    narrator "王教授头发花白，胸前挂着工作牌。"

    professor "这些碑文记载很有意思——明万历大旱、康熙蝗灾、民国战乱，每次灾难后百姓都重修庙宇。"

    professor "可罕庙历经数次重修，始终香火不断。"

    # 【GAME触发】翻牌记忆游戏（6组12张卡片，连珠纹配对）
    pass  # 【游戏触发预留位置：翻牌记忆游戏】

    narrator "【获得道具】碑刻拓片集·可罕庙卷"

    menu:
        "继续研读碑文中的军事记载":
            jump chapter2_act5a
        "询问王教授可罕身份之谜":
            jump chapter2_act5b

    jump chapter2_act5


label chapter2_act4a:
    show professor at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    professor "碑文里确实记载了一些军事布防的信息，但大多已经模糊。"
    professor "不过有一点很清楚——这里是重要的防御节点。"
    jump chapter2_act5

label chapter2_act4b:
    show professor at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    professor "可罕是谁？这个问题学界也有争议。"
    professor "但比起'可罕是谁'，或许更应该问——'为什么三百年来百姓要祭拜他'。"
    jump chapter2_act5


# ============================================================
# 第五幕：高台上的答案
# ============================================================
label chapter2_act5:
    scene black
    narrator "地点：可罕庙·庙前高台"
    narrator "音效：远眺风声、吸气声"

    show bg chapter2 at Position(xfill=True, yfill=True)

    # 远眺风声
    play sound "audio/sound/Chapter 2/a5s1.mp3" fadeout 0.3
    narrator "夕阳西下，余晖染成金色。"

    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    narrator "你站在高台上，眺望远方。"

    show p5 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    guardian "守的是那些村庄、田地、烟火。"

    guardian "你爷爷从来没说过这些事。"

    p1 "……"

    guardian "有些话不必说出口。"

    guardian "答案刻在碑文里、藏在柱子里、留在香火里。"

    # 吸气声
    play sound "audio/sound/Chapter 2/a5s2.mp3" fadeout 0.3
    narrator "你深吸一口气。"

    narrator "有其举之，莫敢废也。"

    hide p5
    narrator "守护灵消失，只余暮色中的可罕庙。"

    jump chapter2_end


label chapter2_act5a:
    professor "碑文记载的多是军民共建的防御工事信息。"
    professor "可见当年可罕庙不仅是祭祀之地，也是军事协调之所。"
    jump chapter2_act5

label chapter2_act5b:
    professor "不管可罕是历史人物还是传说形象，"
    professor "他已经成为民族融合的象征，这就足够了。"
    jump chapter2_act5


# ============================================================
# 章节结束
# ============================================================
label chapter2_end:
    narrator "第二章 完"

    scene black with fade
    
    # 跳转至第三章
    call chapter3
