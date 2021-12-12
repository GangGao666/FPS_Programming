#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : setting.py
# @Description : The file of system settings
import pygame


class Setting:
    def __init__(self):
        # The width of the gaming screen
        self.screen_width = 1200
        # The height of the gaming screen
        self.screen_height = 800
        # The speed of hero
        self.hero_speed = 1
        # Hero's HP
        self.hero_live_volume = 10
        # The duration of the hero's invincible state
        self.hero_shield_time = 80
        # The image path list of the hero's initial image
        self.hero_image = ["images/up1.png","images/up2.png","images/up3.png"]
        # A list of image paths for the demons to randomly drop items
        self.gift_image = ["images/vaccine1.png","images/vaccine2.png","images/vaccine3.png"]
        # A list of image paths for the demons to randomly drop items
        self.gift_boss_image = ["images/gift3.png","images/gift4.png","images/gift5.png"]
        # The speed of the movement of bullet
        self.bullet_speed = 2
        # The number of bullets the hero can fire before the bullet disappears
        self.bullet_allowed = 1
        # A list of image paths of bullets that can be fired by the hero
        self.bullet_image = ["images/mask1.png","images/mask2.png","images/mask3.png"]
        # A list of image paths of bullets that can be fired by the hero
        self.demon_speed = 3
        # The number of demons in the fleet
        self.demon_number = 8
        # Movement speed of the demon in the vertical direction
        self.demon_drop_speed = 1.5
        # The initial horizontal movement direction of the demon,
        # 1 means to the right, -1 means to the left
        self.demon_direction = 1
        # List of initial moving images of demons
        self.demon_image = ["images/monster1_right.png","images/monster1_left.png"]

    '''
    Change the click sound effects of start, help, and about buttons, and add sound effects of clicking
    '''
    def check_btn(self,x1,x2,y1,y2,sound):
        check = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if x1 <= x <= x2 and y1 <= y <= y2:
            if check[0]:
                sound.play()
                return True
