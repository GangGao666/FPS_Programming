#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/6 10:03
# @Author : Seeumt
# @File : setting.py
class Setting:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.background = "images/bg0.png"
        self.ship_speed = 1
        self.ship_live = 3
        self.ship_live_volume = 10
        self.ship_wudi_time = 80
        self.ship_image = ["images/up1.png","images/up2.png","images/up3.png"]
        self.gift_image = ["images/vaccine1.png","images/vaccine2.png","images/vaccine3.png"]
        self.gift_boss_image = ["images/gift3.png","images/gift4.png","images/gift5.png"]
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 1
        self.bullet_image = ["images/mask1.png","images/mask2.png","images/mask3.png"]
        self.alien_speed = 3
        self.alien_number = 6
        self.alien_drop_speed = 1.5
        self.alien_direction = 1
        self.alien_image = ["images/monster1_right.png","images/monster1_left.png"]


