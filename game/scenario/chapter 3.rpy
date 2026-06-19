# 第三章：地道往事

# 角色定义
define p1 = Character("小远")  # 主角
define p2 = Character("爷爷")  # 张明月（回忆/日记中出现）
define p3 = Character("村支书")  # 张建国
define guardian = Character("守护灵")  # 古堡守护之灵，说书人形象
define professor = Character("王教授")  # 文物局专家
define narrator = Character("")

# 场景图片（无特定第三章图片，使用注释标记）
# image bg chapter3 = "chapter3/xxx.jpg"

label chapter3:
    # ========== 第一幕：序章 ==========
    scene black with fade

    narrator "时间：清晨"
    narrator "地点：地道入口外"

    # 音效：踩泥泞咯吱声(a1s1)
    play sound "audio/sound/Chapter 3/a1s1.MP3" fadeout 0.3
    narrator "雨后清晨，晨雾缭绕。"
    narrator "地面满是泥泞水洼，鞋底踩上去会发出轻微的咯吱声。"

    # show bg chapter3_scene1 with dissolve
    narrator "地道入口外的土坡被暴雨冲塌，露出直径约两米的深坑。"

    # 音效：村民议论声(a1s2)、泥土坍塌声(a1s3)
    play sound "audio/sound/Chapter 3/a1s2.MP3" fadeout 0.3
    play sound "audio/sound/Chapter 3/a1s3.MP3" fadeout 0.3
    narrator "坑边围满了议论纷纷的村民。"

    # show p3 at left with dissolve
    p3 "小远，你来了！"
    p3 "这土坡被暴雨冲塌，露出另一个入口，我爹生前最熟悉这条道了。"

    menu:
        "主动请缨我下去看看":
            jump ch3_a1_choice1
        "先看看情况再想办法":
            jump ch3_a1_choice2

    label ch3_a1_choice1:
        p1 "我下去看看！"
        jump ch3_a1_continue

    label ch3_a1_choice2:
        p1 "先别急，让我看看情况。"
        jump ch3_a1_continue

    label ch3_a1_continue:
        # show p3 at left with dissolve
        p3 "行，这是安全帽和手电，我扛着铁锹跟你下去。"

        # ========== 第二幕：缘起 ==========
        scene black with fade
        narrator "时间：接上"
        narrator "地点：地道内部距入口约20米处"

        # show bg chapter3_tunnel with dissolve
        narrator "手电光在黑暗地道中晃动。"

        # 音效：铁锹铲土声(a2s2)、碰硬物声(a2s3)
        play sound "audio/sound/Chapter 3/a2s2.MP3" fadeout 0.3
        narrator "前方被泥土碎石堆堵死。"
        p3 "这堆得够严实的。"
        narrator "村支书放下铁锹喘气。"

        narrator "你和村支书用铁锹铲土，泥土沙沙作响。"

        play sound "audio/sound/Chapter 3/a2s3.MP3" fadeout 0.3
        narrator "你的铁锹碰到一块坚硬的东西。"

        # 音效：摩挲墙砖声(a2s4)
        play sound "audio/sound/Chapter 3/a2s4.MP3" fadeout 0.3
        narrator "你攥着墙砖，指腹摩挲着刻痕。"

        # show guardian at center with dissolve
        guardian "三号交通站——1944.8"
        narrator "这是爷爷张明山的笔迹！"

        # show p3 at left with dissolve
        p3 "这是……三号交通站？你爷爷当年藏过一批抗战物资，就是在这里！"

        menu:
            "快，继续挖！":
                jump ch3_a2_choice1
            "先看看墙面，找最容易挖开的位置":
                jump ch3_a2_choice2

        label ch3_a2_choice1:
            p1 "快，继续挖！"
            jump ch3_a2_continue

        label ch3_a2_choice2:
            p1 "等等，我先看看墙面，找最容易挖开的位置。"
            jump ch3_a2_continue

        label ch3_a2_continue:
            # 【游戏触发预留位置】看相挖游戏
            # 移动铲子找松动土格
            # 路径：(1,1)→(1,2)→(2,2)→(2,3)→(3,3)终点
            # 或 (1,1)→(1,2)→(1,4)→(2,4)→(2,3)→(2,1)→(2,2)→(4,2)→(4,4)
            # 或 (1,1)→(1,3)→(2,3)→(2,1)→(4,1)→(4,3)→(4,5)→(3,5)→(3,4)→(5,4)→(5,2)→(5,3)
            pass  # 【游戏触发预留位置】看相挖游戏

            narrator "挖开缺口，走进土洞。"

            # show bg chapter3_cave with dissolve
            narrator "宽大土洞，十几个锈迹斑斑的铁皮箱木箱，粗陶大缸。"

            # show p3 at left with dissolve
            p3 "这……这是当年的物资库！"

            narrator "掀开缸口木板，粮食早已碳化。"

            # 音效：掰开箱扣声(a2s7)、箱盖吱呀声(a2s8)
            play sound "audio/sound/Chapter 3/a2s7.MP3" fadeout 0.3
            play sound "audio/sound/Chapter 3/a2s8.MP3" fadeout 0.3
            narrator "用力掰开锈蚀的箱扣，箱盖发出吱呀的陈旧声响。"

            narrator "油纸包裹的文件，最上面放着硬皮登记册。"

            # 音效：指尖抚过纸页声(a2s9)
            play sound "audio/sound/Chapter 3/a2s9.MP3" fadeout 0.3
            narrator "翻至最后一页，铅笔字迹："
            narrator "\"三十八号情报：日军八月扫荡计划已送出。粮弹封存待取。若有不测，后来者启。——张明山，1944.8.15\""
            narrator "指尖抚过爷爷的签名，喉咙发紧。"

            # 音效：苍老咳嗽声(a2s10)
            play sound "audio/sound/Chapter 3/a2s10.MP3" fadeout 0.3
            narrator "土洞深处的黑暗中传来一声苍老的咳嗽。"

            # ========== 第三幕：渡尘 ==========
            scene black with fade
            narrator "地点：地道物资库内"

            # 音效：长衫飘动(a2s11)
            play sound "audio/sound/Chapter 3/a2s11.MP3" fadeout 0.3

            # show guardian at center with dissolve
            guardian "你终于来了。"

            # 音效：折扇声(a3s1)
            play sound "audio/sound/Chapter 3/a3s1.MP3" fadeout 0.3
            guardian "（折扇一挥）"

            # 光影中年轻爷爷奔跑场景
            # 音效：年轻爷爷跑步声(a3s2)、日军吆喝声(a3s3)
            play sound "audio/sound/Chapter 3/a3s2.MP3" fadeout 0.3
            play sound "audio/sound/Chapter 3/a3s3.MP3" fadeout 0.3
            narrator "光影中，年轻爷爷在狭窄的地道中快速奔跑，身后传来日军的吆喝声。"

            narrator "爷爷钻进狭窄岔洞屏息。"

            # show guardian at center with dissolve
            guardian "你爷爷藏了三日，送走七批情报，掩护五名同志脱险。"

            narrator "光影化作地道结构剖面图。"

            guardian "这三层地道，上层伪装层、中层指挥层、底层储备层。"
            guardian "六眼水井的秘密洞口，藏着通往各处的暗道。"
            guardian "翻板陷阱、伏击坑、射箭坑——战争年代不是你死就是我亡。"

            narrator "光影淡去。"

            guardian "你爷爷等了七十多年的后来人。"

            # 【获得道具】爷爷的日记本《张壁往事·三》
            narrator "{color=#f00}*获得 爷爷的日记本《张壁往事·三》*{/color}"

            menu:
                "坚定回应我一定会复原地道传承爷爷心愿":
                    jump ch3_a3_choice1
                "郑重点头我明白了我会做好的":
                    jump ch3_a3_choice2

        label ch3_a3_choice1:
            p1 "我一定会复原地道，传承爷爷的心愿！"
            jump ch3_a3_continue

        label ch3_a3_choice2:
            p1 "我明白了，我会做好的。"
            jump ch3_a3_continue

        label ch3_a3_continue:
            narrator "旁白：修复三层地道九处关键设施。"

            # 旁白描述修复过程
            narrator "当九处设施复原，地道轻微震颤，机关运转。"
            narrator "金色大字浮现："
            narrator "\"{color=#ffd700}古堡千年，地道万里。吾辈守之，后人继之。{/color}\""

            # ========== 第四幕：传承 ==========
            scene black with fade
            narrator "时间：正午"
            narrator "地点：地道塌方入口处"

            # 音效：钻出地道脚步声(a4s1)
            play sound "audio/sound/Chapter 3/a4s1.MP3" fadeout 0.3
            narrator "正午阳光，你和村支书从地道入口钻出来。"

            # show bg chapter3_entrance with dissolve
            narrator "地道入口拉起警戒线。"

            # 音效：村民议论声(a4s2)
            play sound "audio/sound/Chapter 3/a4s2.MP3" fadeout 0.3
            narrator "围了不少闻讯赶来的村民和游客，小声议论着。"

            # show professor at center with dissolve
            professor "这就是新发现的地道入口？太好了！"

            # show p3 at left with dissolve
            p3 "王教授，这是我们发现的新入口，通往当年的物资库。"

            professor "文物局会组织专家清理登记，这是重大的考古发现！"

            # 音效：快步走脚步声(a4s3)
            play sound "audio/sound/Chapter 3/a4s3.MP3" fadeout 0.3
            narrator "村支书快步走到王教授身旁。"

            # show p3 at left with dissolve
            p3 "来来，先喝点水。"

            # 音效：瓶盖拧开声(a4s4)
            play sound "audio/sound/Chapter 3/a4s4.MP3" fadeout 0.3
            narrator "村支书递来冰镇矿泉水，你拧开喝了一口。"

            p3 "你爷爷要是还活着，看到这一幕不知多高兴。"
            p3 "他复员回来当解说员，讲地道故事、抗战历史，一讲就是几十年。"

            narrator "记者采访问他是不是英雄。"

            # show p1 at right with dissolve
            p1 "我不是英雄，地道里的粮食才是英雄。"

            narrator "你从背包拿出爷爷的日记本。"

            # 音效：纸页翻动声(a4s5)
            play sound "audio/sound/Chapter 3/a4s5.MP3" fadeout 0.3
            narrator "翻到记录地道的那一页。"
            narrator "\"古堡千年，地道万里。吾辈守之，后人继之。\""

            narrator "英雄不必在史书里。"

            scene black with fade
            
            # 跳转至第四章
            call chapter4_start
