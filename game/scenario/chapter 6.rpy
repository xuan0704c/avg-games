# 第六章：空王殿·琉璃密码
# Chapter 6: Kongwang Temple - Glass Tile Cipher

# 角色定义
define p1 = Character("小远")  # 主角
define p3 = Character("村支书")  # 张建国
define guardian = Character("守护灵")  # 古堡守护之灵，说书人形象
define old_worker = Character("老吴")  # 老匠人，70多岁
define narrator = Character("")

# 图片定义
image bg c6s1 = "chapter6/c6s1.png"  # 【未找到场景图片】
image bg c6s2 = "chapter6/c6s2.png"  # 【未找到场景图片】
image bg c6s3 = "chapter6/c6s3.png"  # 【未找到场景图片】
image bg c6s4 = "chapter6/c6s4.png"  # 【未找到场景图片】
image bg c6s5 = "chapter6/c6s5.png"  # 【未找到场景图片】

# ============================================================
# 第一幕：残瓦
# ============================================================
label chapter6_act1:
    # ============================================================
    # 分场景一：空王佛行祠·晨
    # ============================================================
    label chapter6_act1_scene1:
        # 场景：空王佛行祠院内
        show bg c6s1 at Position(xfill=True,yfill=True)

        # 风吹草动声
        play sound "audio/sound/Chapter 6/a1s1.mp3" fadeout 0.3
        narrator "晨光洒在空王佛行祠的殿顶，琉璃瓦泛幽绿的光，多处瓦片残缺破损，长出杂草。"

        p3 "你爷爷以前常带游客来这儿讲故事，说这殿顶可不简单。"

        narrator "村支书说着，从口袋里掏出一块布包，小心展开，里面是一块琉璃瓦残片。"

        p3 "这是早些年从殿顶落下来的，我捡着留到了现在。"

        narrator "正说着，殿后转出一个佝偻的身影，是老匠人老吴，七十多岁，精神却还健旺。"

        # 滴水声
        play sound "audio/sound/Chapter 6/a1s2.mp3" fadeout 0.3

        old_worker "村支书，小远，你们来啦。"

        p3 "吴叔，这殿顶缺损得厉害，你说要配新瓦，得知道原来烧的什么纹样。"

        old_worker "可不是嘛，这活儿难就难在这儿。早年间烧瓦的窑都关了，纹样也没人记得。"

        narrator "你从包里翻出爷爷留下的手绘图，密密麻麻的符号布满格子。"

        p1 "爷爷这本子里画的都是什么？"

        old_worker "让我看看……"

        narrator "老吴接过本子，眉头越皱越紧。"

        old_worker "这……这像是瓦片的纹样。可这些符号，我也看不太懂。"

        narrator "{color=#0000ffff}*获得道具：琉璃瓦残片*{/color}"

        jump chapter6_act1_scene2

    # ============================================================
    # 分场景二：空王佛行祠院内·古槐下
    # ============================================================
    label chapter6_act1_scene2:
        # 场景：空王佛行祠院内古槐树下
        show bg c6s2 at Position(xfill=True,yfill=True)

        narrator "你走到院中的古槐下，正低头翻看爷爷的手绘图，忽然感觉身后一凉。"

        guardian "这些符号，不是随便画的。"

        narrator "守护灵从古槐后转出，长衫飘飘，像是从旧时的画里走出来的人。"

        guardian "你可知道，这空王殿的琉璃瓦上，藏着什么秘密？"

        p1 "秘密？"

        guardian "当年晋商走南闯北，做生意最怕什么？"

        p1 "……信息不通？"

        guardian "正是。晋商聪明，发明了一套'密码'——用琉璃瓦上的花纹传递商情。"

        narrator "守护灵抬手，光影在空中浮现出一片片琉璃瓦的图案。"

        guardian "你看好了——"
        guardian "山形纹代表'太行'，是晋商出省的必经之路。"
        guardian "水波纹代表'汾河'，是连通南北的水运要道。"
        guardian "城楼纹代表'张壁'，是晋商的大本营。"
        guardian "铜钱纹代表'银两'，是商路的血液。"

        guardian "每片瓦都是信息，按位置排列，就是一张完整的商路图。"

        p1 "原来如此……那爷爷画这些，是为了什么？"

        guardian "你爷爷在追寻晋商的足迹。他知道，这些琉璃瓦不只是建筑装饰，是晋商百年的记忆。"

        p1 "晋商为什么要把商情藏在瓦上？难道不怕……"

        menu:
            "怕盗匪？":
                jump chapter6_act1_scene2_choice_a
            "怕市场波动？":
                jump chapter6_act1_scene2_choice_b

    label chapter6_act1_scene2_choice_a:
        guardian "盗匪？有护卫、有镖局、有会馆，晋商怕的不是刀兵之祸。"

        guardian "他们怕的是——消息滞后，错失商机。"

        jump chapter6_act1_scene2_game

    label chapter6_act1_scene2_choice_b:
        guardian "市场波动虽可畏，但晋商见多识广，自有应对之策。"

        guardian "他们真正怕的，是消息不通——千里之外行情已变，这边还蒙在鼓里。"

        guardian "所以才有了这琉璃密码。"

        jump chapter6_act1_scene2_game

    label chapter6_act1_scene2_game:
        narrator "守护灵挥手，光影扩散开，在你面前形成一道道错落的光影格子。"

        guardian "这是一道光影谜题。移动光源，让影子补全那些空缺的纹样，你就能读懂这密码的拼接之法。"

        # 【游戏触发预留位置】光源影子解密游戏
        # 规则：拖动光源使影子补全空缺
        pass # 【游戏触发预留位置】光源影子解密游戏（晋商琉璃密码）

        guardian "你爷爷画的，就是这张晋商密码路线图。"

        guardian "从张壁出发，经介休、平遥、祁县、太谷、出杀虎口、至恰克图——这条商路，晋商走过了多少年？"

        p1 "……"

        menu:
            "我试试":
                jump chapter6_act1_scene3
            "可我不知道从哪儿开始":
                jump chapter6_act1_scene3

    # ============================================================
    # 分场景三：空王佛行祠殿顶
    # ============================================================
    label chapter6_act1_scene3:
        # 场景：空王佛行祠殿顶
        show bg c6s3 at Position(xfill=True,yfill=True)

        old_worker "小远，帮我扶稳梯子。"

        narrator "老吴指挥着村支书架好木梯，走过来拍了拍梯子腿。"

        # 拍木头
        play sound "audio/sound/Chapter 6/a1s5.mp3" fadeout 0.3

        old_worker "这梯子稳得很，上去吧，帮我记下花纹的位置。"

        narrator "你攀上木梯，木梯发出吱呀声。"

        # 木梯吱呀
        play sound "audio/sound/Chapter 6/a1s6.mp3" fadeout 0.3

        narrator "你蹲下身抚摸殿顶的瓦片，感受着岁月侵蚀的痕迹。"

        p1 "三道水波……这是汾河。城楼纹……是平遥的市楼。骆驼纹……是驼队。"

        narrator "你一一记下，整整二十三片。盯着图纸，忽然发现——这些点连起来，居然是一张地图！"

        narrator "你越看越心惊，颤抖着拿起笔。"

        # 笔尖划纸
        play sound "audio/sound/Chapter 6/a1s7.mp3" fadeout 0.3

        # 再来一次笔尖划纸
        play sound "audio/sound/Chapter 6/a1s8.mp3" fadeout 0.3

        narrator "你一笔一笔地连下去，当最后一笔落下，你猛地抬头。"

        p1 "这殿顶上藏着一张地图！"

        old_worker "什么？"

        p1 "吴爷爷，快上来看看！这不是普通的瓦片，是晋商的商路图！"

        jump chapter6_act1_scene4

    # ============================================================
    # 分场景四：空王佛行祠院内·黄昏
    # ============================================================
    label chapter6_act1_scene4:
        # 场景：空王佛行祠院内
        show bg c6s4 at Position(xfill=True,yfill=True)

        narrator "夕阳西斜，金光照在琉璃瓦上，泛着温暖的光泽。"

        narrator "你坐在石阶上，摊着图纸，旁边是爷爷的日记、残片、老吴的旧本子。"

        # 翻笔记本
        play sound "audio/sound/Chapter 6/a1s3.mp3" fadeout 0.3

        narrator "村支书端茶过来，放在你身边。"

        p3 "小远，看出啥名堂了？"

        narrator "你放下手中的残片，拿起图纸，开始解释。"

        p1 "这些纹样是晋商的'密码'——"
        p1 "山纹代表太行，水纹代表汾河，城纹代表节点城镇，钱纹代表银根，茶纹代表茶货行情，驼纹代表驼队数量。"

        p3 "这么说，你爷爷当年就知道这些？"

        p1 "不止知道。他在追寻这条路。从张壁出发，经介休、平遥、祁县、太谷，然后北上太原，出杀虎口，最后抵达恰克图。"

        narrator "村支书听得目瞪口呆。"

        p3 "这些……都是真的？"

        old_worker "当年我师傅烧瓦，嘴里常念叨一句话。"

        p1 "什么话？"

        old_worker "'山接水，水接城，城接钱。'我一直不懂啥意思，现在想来……"

        p1 "是晋商的口诀！山纹接水纹，是'山水相依'，代表太谷；水纹接城纹，是'水城相连'，代表平遥；城纹接钱纹，是'城中有银'，代表祁县！"

        # 【游戏触发预留位置】滑动方块拼图游戏
        # 规则：四个绿色方块"山，水，城，钱"下滑到箱格中
        pass # 【游戏触发预留位置】滑动方块拼图游戏（晋商密码）

        narrator "你翻开爷爷的日记，翻到《张壁往事·六》，上面写道："

        p1 "'今日听村里老人讲，当年晋商在张壁设分号，屋顶琉璃瓦暗藏商路图。'"

        narrator "日记的字迹渐渐淡去，但那些纹样却越发清晰。"

        narrator "{color=#0000ffff}*获得道具：晋商路线草图*{/color}"
        narrator "{color=#0000ffff}*获得道具：爷爷的日记本《张壁往事·六》*{/color}"

        jump chapter6_act2

    # ============================================================
    # 第二幕：爷爷的老屋·夜
    # ============================================================
    label chapter6_act2:
        # 场景：爷爷老屋，你的卧室
        show bg c6s5 at Position(xfill=True,yfill=True)

        narrator "夜已深，台灯亮着，洒下一圈暖黄的光。"

        narrator "你坐在爷爷的书桌前，摊着日记、琉璃密码图、地道物资登记册拓片。"

        narrator "翻到日记的最后一页，爷爷的字迹依旧清晰，只是末尾多了一行你从未见过的小字："

        narrator "你凑近台灯，仔细辨认——"

        narrator "爷爷写道："

        p1 "'孙儿，如果你看到这页，说明你已经找到了地道，也解开了琉璃的秘密。'"

        narrator "你的心猛地一紧。"

        p1 "'信息会过时，会失传，但只要有后来人愿意读，它就永远活着。'"

        narrator "'这些秘密，交给后来人了。还有很多地方也藏着故事，留给你了。'"

        narrator "窗外月光如水，洒在书桌上。"

        narrator "你抬头望向窗外，可罕寺的轮廓在月色下静静伫立，与空王殿遥遥相望。"

        narrator "忽然，夜风吹过，寺檐风铃叮当作响，清脆的声音在夜里回荡。"

        narrator "你想起爷爷说过的话——"

        narrator "'等人来。'"

        guardian "他说的'等懂的人来'，等的不是懂琉璃的人。"

        narrator "守护灵的声音轻轻响起，像是风中的低语。"

        guardian "等的是愿意听故事的人。"

        narrator "你望着窗外的月色，心中忽然明亮。"

        p1 "爷爷……我会继续听，继续记。"

        narrator "夜风渐止，万籁俱寂。"

        narrator "你知道，那里还有新的故事在等你。"

        narrator "（第六章 完）"

        scene black with fade
        
        # 跳转至第七章
        call chapter_7
