# 角色定义
define p1 = Character("小远")  # 主角
define p3 = Character("村支书")  # 张建国
define guardian = Character("守护灵")  # 古堡守护之灵
define guardian_old = Character("陈守义")  # 二郎庙守庙人，50年
define narrator = Character("")

# 第七章：二郎庙·数镇山河

label chapter_7:
    # ========== 第一幕：庙门启秘 ==========
    scene black with fade

    narrator "翌日辰时，晨雾未散。"

    # show bg erlang_temple_front  # 庙门前场景图
    narrator "阳光斜洒在二郎庙朱红庙门上，庙门两侧石狮蹲坐，檐角铜铃随风轻响。"

    play sound "audio/sound/Chapter 7/a1s2.mp3" fadeout 0.3
    narrator "檐角铜铃随风轻响。"

    narrator "攥着日记站在庙门前，翻开爷爷的笔记："
    p1 "二郎庙中，藏古堡数术之核。三灯对应三才，一碑暗合方圆。灯灭则脉断，碑裂则气散。"

    play sound "audio/sound/Chapter 7/a1s3.mp3" fadeout 0.3
    narrator "身后传来熟悉的脚步声。"

    p3 "小远，这么早就来了？"
    p3 "你爷爷生前最常来这庙里，说是喜欢这里的清净。"

    play sound "audio/sound/Chapter 7/a1s4.mp3" fadeout 0.3
    narrator "庙门'吱呀'一声开了。"

    # show bg erlang_temple_courtyard  # 庙内场景
    play sound "audio/sound/Chapter 7/a1s5.mp3" fadeout 0.3
    narrator "一位白发苍苍的老人从庙内走出，腰间挂着一串钥匙，走路时叮当作响。"

    guardian_old "你是……明月老哥的孙子？"
    guardian_old "像，真像……你爷爷年轻时候的样子。"

    narrator "老人看到小远，眼眶泛红，拉着手往庙里走。"

    guardian_old "你爷爷留了东西给你，就在藏经柜里。"

    play sound "audio/sound/Chapter 7/a1s4.mp3" fadeout 0.3
    narrator "庙门'吱呀'一声合上，光线暗了下来。"

    # ========== 第二幕：镇堡二器 ==========
    scene black with fade

    # show bg erlang_temple_main_hall  # 正殿场景
    narrator "二郎庙正殿内，光线偏暗，香烟袅袅。"

    play sound "audio/sound/Chapter 7/a1s6.mp3" fadeout 0.3
    narrator "香烟袅袅。"

    narrator "二郎神像端坐，目光如炬，手持三尖两刃刀，脚下踩着哮天犬。"
    narrator "神像背后墙上嵌着一块青石碑，碑面有一道斜裂纹。"

    guardian_old "半月前那一夜，三盏灯突然全灭了。"
    guardian_old "灯油是满的，灯芯也是新换的，不知道是怎么回事。"

    guardian_old "你看这石碑，也裂了。"

    guardian_old "你爷爷说，这二器之间暗合数术……"

    narrator "老人从怀中掏出一把旧黄铜钥匙，递到你手中。"

    # 【获得道具】爷爷的旧黄铜钥匙
    narrator "{color=#f00}*获得道具：爷爷的旧黄铜钥匙*{/color}"

    # show bg erlang_temple_cabinet  # 藏经柜场景
    narrator "走到藏经柜前，钥匙插入锁孔。"

    play sound "audio/sound/Chapter 7/a1s7.mp3" fadeout 0.3
    narrator "钥匙插入锁孔，轻轻一转，锁芯'咔哒'一声弹开。"

    play sound "audio/sound/Chapter 7/a1s8.mp3" fadeout 0.3
    narrator "拉开柜门，墨香扑面而来。"

    narrator "柜内整齐摆放着：《张壁往事·七》、《二郎庙镇堡四器布局图》、数学手稿、泛黄的纸条……"

    # 【获得道具】
    narrator "{color=#f00}*获得道具：《张壁往事·七》、《二郎庙镇堡四器布局图》、数学手稿、纸条*{/color}"

    play sound "audio/sound/Chapter 7/a1s16.mp3" fadeout 0.3
    narrator "翻开日记，爷爷的字迹映入眼帘："

    p1 "二郎庙者，古堡之威仪所系。二器各司其职：灯定天地人，碑锁二方气……"

    # show guardian sprite
    guardian "数术之道，在于天人相应。三灯灭，则地脉断；一碑裂，则气数散。"
    guardian "你既已寻得钥匙，便需解开这数术之谜。"

    # 【GAME触发】三道虚影/三守护神问答游戏
    # 真理/谎言/混沌三神，只能问是否问题，限3次
    pass # 【游戏触发预留位置：三守护神问答游戏（三灯定位与石碑修复的谜题）】

    menu:
        "先去庙门口测量石狮方位":
            jump scene_lion_measurement
        "先向陈爷爷打听爷爷当年怎么发现的":
            jump scene_chen_story

    label scene_lion_measurement:
        # show bg erlang_temple_front
        narrator "你蹲在雄狮旁，对照手稿开始测量。"

        guardian_old "你爷爷当年也蹲在这儿，画了三天的图。"
        guardian_old "他拿着绳子这里量量，那里测测，村里人都说他疯了。"

        narrator "你从雄狮左眼拉线到雌狮右眼，记下角度。"
        narrator "回到正殿测量三盏灯位置，果然发现中间那盏偏了两指宽。"

        menu:
            "用撬棍调整灯座":
                jump scene_adjust_lamp
            "先问陈爷爷怎么调":
                guardian_old "你爷爷当年就是这么调的，灯座底部有机关，可以微调位置。"
                jump scene_adjust_lamp

        label scene_adjust_lamp:
            play sound "audio/sound/Chapter 7/a1s9.mp3" fadeout 0.3
            narrator "你用撬棍轻轻撬动灯座，一点一点地挪动位置。"

            narrator "反复核对后，三盏灯与石狮视线终于连成直线。"
            narrator "量出三尺六寸的距离，画出另外两个灯位。"

            narrator "将灯挪到标记位置，准备点燃。"

            play sound "audio/sound/Chapter 7/a1s10.mp3" fadeout 0.3
            narrator "再点燃。"

            narrator "第一盏灯映左肩，第二盏灯映右肩，第三盏灯光束交汇落在神像眉心。"
            narrator "陈守义声音发颤："

            guardian_old "亮了……三盏灯都亮了！"

            narrator "旁白：灯定了，该补碑了。庙后古井通地脉，需取井中青泥调浆补碑。"

            jump scene_ancient_well

    label scene_chen_story:
        guardian_old "你爷爷当年发现这秘密，也是费了好大一番功夫。"
        guardian_old "他在这里住了三个月，每天研究那些数术图形。"

        narrator "你想了想，决定先去测量石狮方位。"

        jump scene_lion_measurement

    label scene_ancient_well:
        # show bg erlang_temple_back
        narrator "绕到庙后，古井藏在墙角。"

        play sound "audio/sound/Chapter 7/a1s11.mp3" fadeout 0.3
        narrator "古井藏在墙角，井口青石板被磨得发亮，长着青苔。"

        menu:
            "直接打水取泥":
                jump scene_get_mud
            "问问陈爷爷当年怎么用井传情报":
                guardian_old "当年地下交通站，你爷爷把情报藏在井里。"
                guardian_old "井壁有块砖是活的，他把竹筒藏在砖后面。"
                guardian_old "我那会儿在庙里守庙，每天来打水取情报。"
                guardian_old "这井里的青泥啊，是补碑的上好材料。"
                jump scene_get_mud

        label scene_get_mud:
            narrator "陈守义沉默一会儿，掀开青石板，打上水。"

            play sound "audio/sound/Chapter 7/a1s11.mp3" fadeout 0.3
            narrator "古井滴水。"

            play sound "audio/sound/Chapter 7/a1s12.mp3" fadeout 0.3
            narrator "桶底带着一层湿润的青泥。"

            guardian_old "三份泥，一份糯米浆，这样调出来的浆最牢固。"

            narrator "你搅匀泥浆，捧着回到正殿。"

            # show bg erlang_temple_main_hall
            narrator "用竹片填碑裂纹，填到最上面时泥浆刚好用完。"
            narrator "石碑轻轻震颤，裂缝合上了。"

            play sound "audio/sound/Chapter 7/a1s13.mp3" fadeout 0.3
            narrator "陈守义从供桌上捧起一枚铸铁令牌。"

            guardian_old "这是你爷爷留下的，二郎护佑令牌。"

            # 【获得道具】二郎护佑令牌
            narrator "{color=#f00}*获得道具：二郎护佑令牌*{/color}"

            jump scene_third_act

    # ========== 第三幕：威镇传远 ==========
    label scene_third_act:
        scene black with fade

        # show bg erlang_temple_courtyard
        narrator "三灯亮起的消息很快传开，惊动了村民。"

        play sound "audio/sound/Chapter 7/a1s14.mp3" fadeout 0.3
        narrator "庙门被人从外面推开，几个人探头进来。"

        narrator "消息传开，越来越多人赶来。"
        narrator "有人摆上瓜果供品，有人拿红绸系在庙前的石狮上。"

        play sound "audio/sound/Chapter 7/a1s15.mp3" fadeout 0.3
        narrator "有人从家里拿来红绸系在庙前的石狮上。"

        p3 "小远，好样的！你爷爷在天有灵，一定很欣慰。"

        guardian_old "孩子，你做到了。"

        narrator "陈守义双手捧令牌，郑重递到你手中。"

        play sound "audio/sound/Chapter 7/a1s16.mp3" fadeout 0.3
        narrator "他再从怀里掏出那本旧册子，翻开扉页。"

        narrator "扉页中夹着一张纸条，是爷爷的字迹。"

        # 【获得道具】爷爷的《张壁往事·七》
        narrator "{color=#f00}*获得道具：爷爷的《张壁往事·七》*{/color}"

        narrator "翻开最后一页，爷爷颤抖但依然清晰的字迹映入眼帘："

        p1 "远娃，当你点亮这三盏灯，便懂了数不是冷的，文不是虚的，红色记忆更不是远的……"

        narrator "眼眶发热，合上日记，抬头看向神像。"
        narrator "三盏灯光束在神像眉心交汇，照得正殿通明透亮。"

        narrator "旁白：三盏灯，亮了。一块碑，补了。三百年前贾永春把玉佩藏在神像背后……"

        scene black with fade
        
        # 跳转至终章
        call chapter_final
