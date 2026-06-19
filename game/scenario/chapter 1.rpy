# 第一章：星象启秘
# Chapter 1: Star Secret Revelation

# 角色定义
define p1 = Character("小远")  # 主角，我
define p2 = Character("爷爷")  # 张明月，古堡守护人
define p3 = Character("村支书")  # 张建国，50余岁
define p4 = Character("电工老李")  # 电工师傅
define guardian = Character("守护灵")  # 古堡守护之灵，说书人形象
define narrator = Character("")

# 图片定义
image bg c1s1 = "chapter1/c1s1.png"
image bg c1s2 = "chapter1/c1s2.png"
image bg c1s2s1 = "chapter1/c1s2s1.png"
image bg c1s2s2 = "chapter1/c1s2s2.jpg"
image bg c1s2s3 = "chapter1/c1s2s3.jpg"
image bg c1s3 = "chapter1/c1s3.jpg"
image p1 = "chapter1/p1.png"
image p2 = "chapter1/p2.png"  
image p3 = "chapter1/p3.png"  
image p4 = "p4.png"
image p5 = "p5.png"  # 守护灵立绘

# ============================================================
# 第一幕：遗物归乡
# ============================================================
label chapter1_act1:
    # 场景：第一章第一幕场景
    show bg c1s1 at Position(xfill=True,yfill=True)

    # 推开那扇榆木旧门
    play sound "audio/sound/Chapter 1/a1s1.mp3" fadeout 0.3
    narrator "推开那扇榆木旧门，屋内陈设极简，土坯墙挂着一帧帧泛黄老照：爷爷二十岁穿粗布军装守堡的模样，鬓角斑白时戴着'古堡终身守护人'奖章在魁星楼前笑的瞬间，还有他牵着孩童的手，在古碑前讲星宿故事的合影。"

    narrator "靠墙的老榆木柜上，一沓笔记本码得整整齐齐，封皮都覆着薄布。"

    # 显示小远立绘
    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    with dissolve

    narrator "你立在屋中，指尖抚过墙面上微凉的相框，心中五味杂陈。爷爷走了半年，学业的忙碌让你迟迟没机会回来好好收拾，这次暑假，父母嘱你把老宅归置清楚，也替他们陪陪守了一辈子古堡的老人。"

    narrator "走到榆木柜前，掀开覆着的粗布，最上面那本笔记本露了出来，封皮上手写的《张壁往事·一》被磨得微微发毛，却是熟悉的笔锋。"

    # 翻开第一页
    play sound "audio/sound/Chapter 1/a1s2.mp3" fadeout 0.3
    narrator "翻开第一页，爷爷的字迹跃入眼帘："

    # 显示爷爷立绘
    show p2 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    p2 "这古堡，我守了一辈子，以后你替我去看，替我记。"

    # 隐藏爷爷立绘
    hide p2
    with dissolve
    narrator "儿时的画面突然涌来：夏夜的古堡广场，爷爷搬着竹椅坐在你身边，指着天上的星星说'那是奎宿，守着咱们古堡的文运'，你嫌他唠叨，扒拉着冰棍敷衍两句，就跑去和小伙伴追着灯笼跑。"

    # 你轻轻叹了口气
    play sound "audio/sound/Chapter 1/a1s3.mp3" fadeout 0.3
    narrator "如今捧着这本沉甸甸的日记，你轻轻叹了口气，才发现自己从未真正读懂过爷爷，读懂过他口中那'藏着星星的古堡'。"

    # 屋内一缕微凉的穿堂风拂过
    play sound "audio/sound/Chapter 1/a1s4.mp3" fadeout 0.3
    narrator "忽然，屋内一缕微凉的穿堂风拂过，烛台上的残蜡轻轻晃动，一个低沉、沧桑的声音仿佛从榆木柜的木纹里渗出来，又像从遥远的星空中飘来："

    # 显示守护灵立绘
    show p5 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    guardian "这日记，是你爷爷用一辈子的光阴写的。如今你翻开它，古堡的事，就该你接着记了。"

    # 隐藏守护灵立绘
    hide p5
    with dissolve
    narrator "你猛地抬头，屋内空无一人，只有窗棂外的槐树叶轻轻晃动。"

    # 窗外槐树叶轻轻晃动
    play sound "audio/sound/Chapter 1/a1s5.mp3" fadeout 0.3

    # 门外传来急促的脚步声
    play sound "audio/sound/Chapter 1/a1s6.mp3" fadeout 0.3
    narrator "正愣神时，门外传来急促的脚步声，石板路被踩得'噔噔'响。"

    # 显示村支书立绘
    show p3 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    p3 "小远！小远在屋里吗？"

    narrator "你打开门，村支书满头大汗，粗布褂子被汗浸湿了一大片，站在门口急得直搓手。"

    # 村支书说话带喘气声
    play sound "audio/sound/Chapter 1/a1s7.mp3" fadeout 0.3
    p3 "古堡里好几盏路灯全灭了！老李查了两天两夜，线路全查遍了，愣是找不出毛病！老人们晚上不敢出门，游客也怕摔着，这古堡的夜路，离了灯可不行啊。你爷爷以前最懂这些，堡里的灯都是他安的、守的，我就想着，你回来了，能不能帮着看看？"

    # 小远说话时显示小远立绘
    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    with dissolve
    p1 "我……我是学数学的，压根不懂电路啊。"

    # 村支书立绘仍在
    p3 "你爷爷那日记里肯定记着啥！他那人，心细，古堡的一草一木、一灯一线，都往本子上写。你翻翻，说不定能找到线索，这堡里的东西，就数他最清楚。"

    # 翻开日记
    play sound "audio/sound/Chapter 1/a1s2.mp3" fadeout 0.3
    narrator "你半信半疑翻开日记，指尖随意一翻，正好停在一页画着星图的页面，星图旁用红笔标注着几个古堡位置，正是路灯故障的地方。"

    p1 "还真有……建国叔，古堡的这些路灯，是谁安的？"

    p3 "那还是你爷爷二十多岁的时候，八十年代初，他和村里几个老匠人一起安的。后来修修补补，也都是他亲自盯着，旁人想碰，他都不让。我们都笑他，说几盏破灯，有啥好盯的，他却板着脸说，灯的位置不能乱动，动了就对不上星星了，动了古堡的'脉'就断了。那时候我们都当他是老糊涂了，现在想来，他怕是早有安排。"

    p1 "对不上星星……"

    p3 "我是不懂这些星啊脉的，你慢慢看。老李在魁星楼那边等着，我先过去招呼着，你一会儿过来找找我们啊。"

    # 隐藏村支书立绘
    hide p3
    with dissolve
    narrator "村支书的身影消失在古巷尽头，皮鞋踩在石板地上的'咯噔'声渐渐远去。"

    # 皮鞋踩石板地
    play sound "audio/sound/Chapter 1/a1s8.mp3" fadeout 0.3

    # 隐藏小远立绘
    hide p1
    with dissolve
    narrator "你站在原地，看着日记里那张星图，星点与古堡的建筑位置交错，又抬头望向魁星楼的方向，暮色中，那座三层小楼的轮廓像一颗立在古堡东南的星，静静等着。"

    # 【获得道具】（获得道具：爷爷的日记《张壁往事》第一册）
    narrator "{color=#0000ffff}*获得道具：爷爷的日记《张壁往事·一》*{/color}"

    jump chapter1_act2

# ============================================================
# 第二幕：星脉寻踪
# ============================================================
label chapter1_act2:
    # 场景：第一章第二幕场景
    show bg c1s2 at Position(xfill=True,yfill=True)

    # 显示小远立绘
    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    with dissolve

    narrator "从爷爷旧屋出来，沿着青石板古巷向东走，夕阳的最后一抹金芒镀在楼身上，飞檐翘角的剪影刻在渐暗的天幕上，像从星图里拓下来的模样，檐角的铜铃被风吹得轻轻晃动，叮铃作响。"

    # 铜铃轻响
    play sound "audio/sound/Chapter 1/a2s1.mp3" fadeout 0.3

    # 你拾级而上
    play sound "audio/sound/Chapter 1/a2s2.mp3" fadeout 0.3
    narrator "你拾级而上，走到魁星楼下，翻开日记，其中一页画着魁星楼的精细简图，旁边用红笔写着："

    # 显示爷爷立绘（日记内容）
    show p2 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    p2 "魁星楼，古堡之眼。登楼可望全堡，夜可观星。楼内楼外共有三盏引路灯，各应星宿，星灯相照，堡脉方通。"

    # 隐藏爷爷立绘
    hide p2
    with dissolve
    narrator "你抬头望向魁星楼，指尖抚过楼身的青砖，上面似乎有淡淡的星纹刻痕，轻声自语："

    p1 "爷爷说的'各应星宿'，到底是什么意思？星灯相照，又照的是哪颗星？"

    # 显示守护灵立绘
    show p5 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    guardian "魁星楼乃古堡文运之核，三盏灯各应星辰，一盏照张宿，一盏映奎宿，一盏守壁宿。循星脉而行，顺星轨而接，自见分晓。"

    p1 "你到底是谁？为何一直跟着我？"

    guardian "我是这《张壁往事》的守护灵，是你爷爷用一生的执念、用对古堡的深情凝结而成的星灵。他守了一辈子张壁古堡，这日记藏着他的心血，藏着古堡的星脉，所以我应运而生，等着一个能读懂他、能守古堡的人。"

    p1 "原来是这样……爷爷他，到底藏了多少秘密。"

    # 隐藏守护灵立绘
    hide p5
    hide p1
    with dissolve

    jump chapter1_act2_scene1

# ============================================================
# 分场景一：魁星楼一楼·门洞内侧
# ============================================================
label chapter1_act2_scene1:
    # 场景：第一章第二幕分场景一
    show bg c1s2s1 at Position(xfill=True,yfill=True)

    # 显示小远立绘
    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    with dissolve

    narrator "走进魁星楼一楼，天井里长着一株老石榴树，枝桠伸到门洞前。门洞内侧的青砖墙上，嵌着一盏古旧的铸铁壁灯，铁质灯罩爬满锈迹，蒙着厚厚的灰尘，灯座下方的青砖上，刻着一个小小的星形刻痕，刻得很深。"

    # 电工老李在场
    show p4 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve

    narrator "电工老李（四十多岁，精瘦黝黑，手指粗糙带着厚茧，指缝里嵌着铜锈）正蹲在壁灯旁抽烟，烟圈绕着壁灯飘开，看见你来，立马站起身，掐灭了烟。"

    p4 "小远来了？你建国叔说让你来看看，我算是没辙了。楼上楼下查了个底朝天，线路都是通的，线接好后灯就是不亮，邪门得很，活了半辈子，从没见过这情况。"

    narrator "你走到壁灯前，蹲下身子，指尖轻轻拂过灯座下的星形刻痕，触感微凉，这刻痕与日记里画的星标一模一样。翻开日记对照，爷爷的字迹清晰可见："

    # 显示爷爷立绘（日记内容）
    show p2 at Position(xpos=0.5, ypos=0.95, yanchor=1.0)
    with dissolve
    p2 "魁星楼一楼灯位，对应二十八星宿之'张宿'。张宿为南方朱雀第五宿，七星连珠，主昌盛、主文运。灯亮则古堡文运昌，灯灭则文运晦。此灯年久失修，线非断而乱，需按星轨重接，方得光亮。"

    # 隐藏爷爷立绘
    hide p2
    with dissolve
    # 你抬手打开灯座后盖
    play sound "audio/sound/Chapter 1/a2s3.mp3" fadeout 0.3
    narrator "你抬手打开灯座后盖，里面的电线果然凌乱缠绕，几根线头断在外面，即便接好，也是胡乱拼凑，红的接黄的，蓝的接绿的，像一团扯不开的乱麻，完全没有章法。"

    p4 "这儿我们查了三遍，线断了接上就行，可接完还是不亮，我都怀疑是不是撞邪了。"

    narrator "你盯着日记上的张宿星图——七颗星辰由细红笔连线，从西南到东北，形成一个弯弯的弧状，星轨顺序清晰可见。忽然想起爷爷日记里反复圈画的一句话，被红笔描了三遍："

    show p2 at Position(xpos=0.5, ypos=0.95, yanchor=1.0)
    with dissolve
    p2 "'星脉之连，非直而通，需循星轨，顺星而行，方合天道。'"

    hide p2
    with dissolve
    p1 "所以不是简单接上就行，得按星星的连接顺序接，顺着张宿的星轨来，才能通脉亮灯。"

    # 你让老李递来剥线钳
    play sound "audio/sound/Chapter 1/a2s4.mp3" fadeout 0.3
    narrator "你让老李递来剥线钳，按照星图上张宿七星的连线顺序，一根根整理线头，红对红、蓝对蓝，顺着星轨的弧度将电线接好，当最后一根线接好，轻轻扣上灯座后盖的瞬间，"

    # 壁灯'啪'地亮起
    play sound "audio/sound/Chapter 1/a2s5.mp3" fadeout 0.3
    narrator "壁灯'啪'地亮起。"

    # 【游戏触发预留位置】星团拼图游戏关卡一
    pass # 【游戏触发预留位置】星团拼图游戏关卡一（张宿七星连珠）

    show p5 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    guardian "张宿主昌盛，灯亮则文运兴。小子，你接对了，接的不只是线，是古堡的星脉。"

    p4 "嘿，还真亮了！你爷爷这笔记也太神了！这哪里是记日记，这是藏着宝贝啊！"

    p1 "原来爷爷说的'循星轨'，是这个意思。他守的从来不是灯，是古堡的星脉。"

    # 隐藏所有立绘
    hide p5
    hide p4
    hide p1
    with dissolve

    jump chapter1_act2_scene2

# ============================================================
# 分场景二：魁星楼二楼·凭栏处
# ============================================================
label chapter1_act2_scene2:
    # 场景：切换到二楼场景
    show bg c1s2s2 at Position(xfill=True,yfill=True)

    # 显示小远立绘
    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    with dissolve

    # 踩着木质楼梯登上二楼
    play sound "audio/sound/Chapter 1/a2s2.mp3" fadeout 0.3
    narrator "踩着木质楼梯登上二楼，楼梯板发出轻微的'吱呀'声，像岁月的低语。二楼的凭栏处视野开阔，能远眺古堡的全景。"

    narrator "凭栏旁立着一盏复古高杆灯，灯杆底部的青石基座上，有一个小小的凹槽，凹槽里积着厚厚的尘土，像是藏着什么东西。"

    narrator "你走到这盏高杆灯前，目光落在灯杆底部的凹槽上，伸手拂去尘土，里面嵌着一块黑漆漆的碎片，碎片上有淡淡的星纹，摸起来冰凉坚硬，像是玉石，又像是陨石。你小心地抠出碎片，拿在手里端详，星纹在微光下若隐若现，与日记里的星纹如出一辙。"

    narrator "翻开日记，爷爷的字迹带着一丝郑重："

    show p2 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    p2 "魁星楼二楼灯位，对应二十八星宿之'奎宿'。奎为天之武库，七星相贯，主文运，亦主兵事，乃古堡星象阵的核心星宿。此灯最要紧，不可灭，藤缠灯则光蔽，星脉堵；除尽野藤，扫尽尘垢，方得天光入，星脉通。"

    hide p2
    with dissolve
    narrator "看着爷爷写下的内容，你想到了什么。于是你决定："

    menu:
        "借来电工刀，亲手割断藤蔓":
            jump chapter1_act2_scene2_choice_a
        "让电工老李用专业工具清理":
            jump chapter1_act2_scene2_choice_b
        "先仔细观察，看看有没有更省力的办法":
            jump chapter1_act2_scene2_choice_c

label chapter1_act2_scene2_choice_a:
    p1 "我来试试，这藤缠了灯这么久，该清了。"

    # 一刀一刀割着枯藤
    play sound "audio/sound/Chapter 1/a2s6.mp3" fadeout 0.3
    narrator "你握住刀柄，一刀一刀割着枯藤，藤条又粗又韧，刀刃有些钝，割起来格外费力，每割一下，都要使出不小的力气。你的手心被刀柄磨得发红，汗水顺着额头滴落，滴在青石地上，晕开小小的湿痕。但每割断一根，路灯就露出一分，灯杆上的铜皮也渐渐显露，星纹似乎也亮了一分。"

    # 【游戏触发预留位置】星纹密码游戏
    pass # 【游戏触发预留位置】星纹密码游戏（选项A）

    jump chapter1_act2_scene2_continue

label chapter1_act2_scene2_choice_b:
    show p4 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    p1 "李叔，你工具全，手艺也好，还是你来吧，我怕笨手笨脚弄坏了灯杆，反倒误事。"

    p4 "行，看我的，这点藤，分分钟的事。"

    # 园艺剪声
    play sound "audio/sound/Chapter 1/a2s7.mp3" fadeout 0.3
    narrator "他从工具箱里拿出重型园艺剪，'咔嚓咔嚓'几剪子下去，粗韧的枯藤应声而落，干脆利落，没用几分钟，缠在灯杆上的枯藤就被清理得干干净净。你在一旁看着，不得不佩服他的手艺，连灯杆缝隙里的细藤，都被他用小钳子挑了出来。"

    # 【游戏触发预留位置】打开老李的工具箱游戏
    pass # 【游戏触发预留位置】打开老李的工具箱游戏（选项B）

    hide p4
    with dissolve
    jump chapter1_act2_scene2_continue

label chapter1_act2_scene2_choice_c:
    p1 "等等，我先看看，这藤枯了这么久，说不定有窍门。"

    narrator "你发现几根主藤的根部已经枯死松动，与灯杆分离，只要找准这些主根位置，轻轻一扯，就能带下一大片缠藤。你顺着主根的方向，先扯断几根主藤，再用手掰掉细藤，没一会儿，大部分藤蔓就被清理干净，剩下的零星细藤，用手指就能掐断。"

    # 【游戏触发预留位置】寻找位置游戏
    pass # 【游戏触发预留位置】寻找位置游戏（选项C）

    show p4 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    p4 "嘿，你小子还挺会找窍门！不愧是你爷爷的孙子，骨子里带着心细。"

    hide p4
    with dissolve
    jump chapter1_act2_scene2_continue

label chapter1_act2_scene2_continue:
    narrator "无论选择哪个，最终枯藤都被清理干净，高杆灯露出全貌，灯杆上的铜皮星纹在微光下清晰可见。"

    # 打开灯座后盖
    play sound "audio/sound/Chapter 1/a2s3.mp3" fadeout 0.3
    narrator "你打开灯座后盖，里面的线路与一楼一样，错乱缠绕，完全偏离了星轨。你按照日记里奎宿的星图，七星从西北到东南，呈'S'形连线，顺着奎宿的星轨，一点点整理电线，将错乱的线头重新对接。当最后一根线接好的瞬间，高杆灯骤然亮起，照亮了整片凭栏处，也照亮了远处的古堡街巷，奎宿的星轨在灯光下隐约浮现。"

    # 灯亮
    play sound "audio/sound/Chapter 1/a2s5.mp3" fadeout 0.3

    p1 "这是什么？质地冰凉，还有星纹，怎么会嵌在灯杆的凹槽里？"

    show p5 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    guardian "奎宿重光，星脉初显。此乃古堡星象阵的星石，是开启星阵的钥匙，缺一不可。"

    narrator "你低头看向灯杆底部的青石基座，清理完尘土后，基座上刻着一个小小的'奎'字，笔迹苍劲，与爷爷的字迹有几分相似，又比爷爷的字迹更古老，像是几十年前刻的，被岁月磨得微微发毛。"

    narrator "{color=#0000ffff}*获得道具：星石残片（1/3）*{/color}"

    # 隐藏立绘
    hide p5
    hide p1
    with dissolve

    jump chapter1_act2_scene3

# ============================================================
# 分场景三：魁星楼外·台阶下
# ============================================================
label chapter1_act2_scene3:
    # 场景：切换到三楼场景
    show bg c1s2s3 at Position(xfill=True,yfill=True)

    # 显示小远立绘
    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    with dissolve

    narrator "从魁星楼下来，青石台阶旁是一小块青石板铺就的空地。空地边立着一盏孤零零的矮杆路灯，是游客和村民晚上上下魁星楼的指引灯，灯体朴素，却立得笔直。灯旁立着一块半人高的石碑，碑上刻着'魁星引途'四个篆字。"

    narrator "你走到最后这盏灯前，这是魁星楼三盏引路灯的最后一盏，位置最偏，却被爷爷在日记里用红笔圈了重点，标注了三遍。翻开日记，爷爷的字迹带着一丝温柔："

    show p2 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    p2 "'魁星楼下阶前灯，对应二十八星宿之'壁宿'。壁宿为北方玄武第七宿，主守护、主藏秘，与张宿合为'张壁'，乃古堡之名的由来。此灯虽偏，却是星象阵的收尾，不可或缺。灯若不亮，非线路之故，或与碑下之物有关，星石藏于碑，星脉系于石。'"

    hide p2
    with dissolve
    narrator "你蹲下身检查灯座，线路完好无损，接头也没有松动，可灯就是毫无动静，像沉睡了一般。正疑惑时，脚边被什么硬东西硌了一下，低头一看，碑座旁的浮土里，露出一角锈迹斑斑的铁盒，被泥土半掩着。"

    p1 "这是什么？藏在碑座下，难道是爷爷说的碑下之物？"

    narrator "你用手轻轻挖开碑座旁的浮土，将铁盒取了出来，铁盒巴掌大小，锈迹裹满了盒身，上面刻着一个小小的星纹，与之前找到的星石碎片纹路一致。"

    # 你轻轻扣开铁盒
    play sound "audio/sound/Chapter 1/a2s8.mp3" fadeout 0.3
    narrator "你轻轻扣开铁盒，"

    # 【游戏触发预留位置】华容道游戏
    pass # 【游戏触发预留位置】华容道游戏（壁宿星石）

    narrator "里面铺着一层红布，红布上放着一本更旧的手抄本，封皮是泛黄的宣纸，用线装订着，封面上用工整的小楷写着《张壁星象考》，旁边还放着两块黑漆漆的星石。"

    p1 "这就是爷爷说的星石？居然有三块。"

    narrator "'这些星石碎片，是我二十岁时修缮魁星楼，从楼基地下挖出的，村里的老人都说，这是上古星石，藏着古堡的星脉。我收着，藏在碑下、灯杆里，也许有一天，有人能读懂我的日记，找到这些碎片，集齐三片，可解古堡星象之秘，可通古堡地脉。'"

    narrator "你从口袋里拿出之前在二楼找到的星石碎片，将三片碎片拼在一起，就在三片碎片拼合的瞬间，那盏一直不亮的矮杆路灯突然'啪'地自己亮了起来。"

    # 矮杆路灯自己亮起
    play sound "audio/sound/Chapter 1/a2s5.mp3" fadeout 0.3

    narrator "光芒柔和，与一楼、二楼的灯交相辉映，三道光芒在夜空中连成一线，正是奎宿、张宿、壁宿三宿的星轨。"

    narrator "{color=#0000ffff}*获得道具：星石残片（2/3）→ 星石残片（3/3）→ 星晷碎片（已合成）*{/color}"
    narrator "{color=#0000ffff}*获得道具：手抄本《张壁星象考》*{/color}"

    narrator "魁星楼一楼的壁灯、二楼的高杆灯、楼下的矮杆灯三灯同时亮起，三道暖光从不同方向射向夜空，在魁星楼的上空交汇，形成一个清晰的星轨图案，与天上奎、张、壁三宿的星辰遥遥相对。"

    # 隐藏小远立绘
    hide p1
    with dissolve

    # 村支书拍你肩膀（支线音效）
    play sound "audio/sound/Chapter 1/支a3s1.mp3" fadeout 0.3

    narrator "村支书不知何时站在广场上，抬头望着夜空的光轨，嘴巴微张，语气满是惊叹，喃喃道："

    # 显示村支书立绘
    show p3 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    p3 "好家伙，这三盏灯的位置，连起来不就是天上的奎宿吗？你爷爷当年安的灯，那里是安灯啊，是照着星星的位置，布了一个星阵啊！我们都错怪他了，他哪里是老糊涂，他是把古堡的星星，藏进了灯里。"

    # 显示小远立绘
    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    with dissolve
    narrator "你站在魁星楼下，抬头望向夜空，奎、张、壁三宿的星辰在天幕上格外明亮，七星连珠，与地上的三盏灯遥遥呼应，星光落进眼里，像爷爷的目光，温柔而坚定。"

    # 显示守护灵立绘
    show p5 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    guardian "星脉已显，三宿归位。孩子，你爷爷没记错，也没白记，他守了一辈子的星，终于等到了懂的人。"

    p1 "原来爷爷说的'各应星宿'，是真的。他把古堡的名字，把古堡的脉，都藏进了星星里。"

    # 隐藏所有立绘
    hide p5
    hide p3
    hide p1
    with dissolve

    jump chapter1_act3

# ============================================================
# 第三幕：星启·魁星楼顶
# ============================================================
label chapter1_act3:
    # 场景：第一章第三幕场景
    show bg c1s3 at Position(xfill=True,yfill=True)

    # 显示小远立绘
    show p1 at Position(xpos=0.3, ypos=0.95, yanchor=1.0)
    with dissolve

    # 你踩着木质楼梯，一步步登上魁星楼顶层
    play sound "audio/sound/Chapter 1/a3s1.mp3" fadeout 0.3
    narrator "你踩着木质楼梯，一步步登上魁星楼顶层，脚下的古堡在夜色中沉沉睡去，青砖古巷、亭台建筑都被星光与灯光笼罩，安静而祥和，远处可罕庙的轮廓在夜色中若隐若现，铜钟的余音似乎还在巷陌间回荡。"

    narrator "你站在顶层凭栏处，迎着微凉的夜风，翻开爷爷的《张壁往事》第一册，翻到最后一页。在星光与灯光的交映下，你发现这一页的角落，有一行极淡的字迹，也许是冥冥中的指引，字迹带着一丝颤抖，却依旧坚定："

    show p2 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    p2 "'星象既明，庙宇当启。可罕庙中，藏有古堡千年之谜。欲知地道真容，需先解庙堂之秘。'"

    hide p2
    with dissolve
    narrator "你猛地想起，刚才在魁星楼一楼整理壁灯时，好像看见老木柜的后面，有一扇不起眼的小木门，被布帘遮着，门把手上刻着星纹，当时只顾着修灯，并未在意。"

    p1 "可罕庙……爷爷的意思是，下一步要去可罕庙？"

    show p5 at Position(xpos=0.7, ypos=0.95, yanchor=1.0)
    with dissolve
    guardian "星脉归位，奎宿重光。孩子，你爷爷记了一辈子的东西，你找到了。但这只是开始——古堡的秘密，还在可罕庙中等着你。"

    hide p5
    with dissolve
    narrator "你低头望向魁星楼下，夜风拂过，似乎能听见隐约的滴水声从地底传来，轻轻的，像是古堡的心跳。"

    # 隐约的滴水声从地底传来
    play sound "audio/sound/Chapter 1/a3s2.mp3" fadeout 0.3

    p1 "爷爷，我接着记了，接着守了。下一站，可罕庙。"

    # 远处可罕庙的铜钟，在深夜里突然再次撞响
    play sound "audio/sound/Chapter 1/a3s3.mp3" fadeout 0.3
    narrator "远处可罕庙的铜钟，在深夜里突然再次撞响，'当——当——'，余音悠远绵长，绕着古堡的青砖飞檐，绕着满天星斗，在夜色中久久不散。"

    narrator "爷爷说，星星是落在天上的灯，灯是种在地上的星。"

    narrator "他把一辈子的光阴，种进古堡的每一道砖缝里。你翻开日记的那一刻，那些光，就醒了。"

    narrator "三盏灯，照着三宿；三宿，守着一座堡。你接的不是线，是他没走完的路；你亮的不是灯，是他没说完的话。"

    narrator "（第一章 完）"

    # 隐藏所有立绘
    hide p1
    with dissolve

    scene black with fade
    
    # 跳转至第二章
    call chapter2_act1
