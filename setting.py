#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : setting.py
# @Description : 系统设置文件
class Setting:
    def __init__(self):
        # 游戏屏幕宽度
        self.screen_width = 1200
        # 游戏屏幕高度
        self.screen_height = 800
        # 英雄移动速度
        self.hero_speed = 1
        # 英雄生命值
        self.hero_live_volume = 10
        # 英雄无敌状态的持续时长
        self.hero_shield_time = 80
        # 英雄的初始形象的图像路径列表
        self.hero_image = ["images/up1.png","images/up2.png","images/up3.png"]
        # 怪物随机掉落道具的图像路径列表
        self.gift_image = ["images/vaccine1.png","images/vaccine2.png","images/vaccine3.png"]
        # boss随机掉落道具的图像路径列表
        self.gift_boss_image = ["images/gift3.png","images/gift4.png","images/gift5.png"]
        # 子弹移动速度
        self.bullet_speed = 2
        # 在子弹消失前，英雄可发射的子弹数目
        self.bullet_allowed = 1
        # 英雄可发射的子弹的图像路径列表
        self.bullet_image = ["images/mask1.png","images/mask2.png","images/mask3.png"]
        # 怪物移动速度
        self.demon_speed = 3
        # 初始怪物数目
        self.demon_number = 6
        # 怪物垂直方向的移动速度
        self.demon_drop_speed = 1.5
        # 怪物水平初始移动方向，1代表向右，-1代表向左
        self.demon_direction = 1
        # 怪物初始移动图像列表
        self.demon_image = ["images/monster1_right.png","images/monster1_left.png"]


