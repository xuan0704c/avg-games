# 章节演出代码编写规范 Spec

## Why
根据剧情文本(plot_final.txt)、音效配置(plot_with_sound.txt)和图像配置(plot_with_image.txt)，为张壁古堡游戏编写各章节的演出代码，实现剧情的Ren'Py脚本化。

## What Changes
- 在scenario文件夹创建chapter 1-7及终章的.rpy文件
- 音效文件播放代码对应audio文件夹中的音效，并使用带fadeout的截断代码防止快速跳过时音频错位
- 图像文件使用plot_with_image.txt中定义的角色和场景图像，未找到的立绘留空并添加注释
- 游戏触发选项使用pass和注释标注预留位置

## Impact
- 创建文件：scenario/chapter 1.rpy, chapter 2.rpy, chapter 3.rpy, chapter 4.rpy, chapter 5.rpy, chapter 6.rpy, chapter 7.rpy, chapter final.rpy
- 角色定义：p1(小远), p2(爷爷), p3(村支书), p4(电工老李)
- 场景定义：c1s1, c1s2, c1s2d1, c1s3等

## ADDED Requirements

### Requirement: 音效截断播放
系统应当在播放音效时使用fadeout截断，防止文本快速推进时音频播放错位。
```renpy
play sound "audio/sound/Chapter 1/a1s1.mp3" fadeout 0.3 fadein 0.0
```

### Requirement: 场景图像显示
系统应当支持使用plot_with_image.txt中定义的场景编码显示背景图。

### Requirement: 角色立绘显示
系统应当在对话时显示对应角色的立绘，未设置立绘的角色显示注释提醒。

### Requirement: 游戏触发占位
涉及游戏的选项应当使用pass和注释标注预留位置。

## MODIFIED Requirements
无

## REMOVED Requirements
无
