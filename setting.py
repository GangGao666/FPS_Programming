#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : setting.py
# @Description : System setup file
import pygame


class Setting:
    def __init__(self):
        # Game screen width
        self.screen_width = 1200
        # Game screen height
        self.screen_height = 800
        # Hero movement speed
        self.hero_speed = 1
        # Hero Life Value
        self.hero_live_volume = 10
        # Length of heroic invincibility
        self.hero_shield_time = 80
        # List of image paths for the initial image of the hero
        self.hero_image = ["images/up1.png","images/up2.png","images/up3.png"]
        # Image path list of monsters dropping random props
        self.gift_image = ["images/vaccine1.png","images/vaccine2.png","images/vaccine3.png"]
        # List of image paths for randomly dropping props by bosses
        self.gift_boss_image = ["images/gift3.png","images/gift4.png","images/gift5.png"]
        # Bullet movement speed
        self.bullet_speed = 2
        # The number of bullets the hero can fire before the bullet disappears
        self.bullet_allowed = 1
        # List of image paths for bullets
        self.bullet_image = ["images/mask1.png","images/mask2.png","images/mask3.png"]
        # Monster horizontal movement speed
        self.demon_speed = 3
        # Initial number of monsters
        self.demon_number = 6
        # Vertical movement speed of the monster
        self.demon_drop_speed = 1.5
        # Monster horizontal initial movement direction, 1 represents to the right, -1 represents to the left
        self.demon_direction = 1
        # Monster initial moving image list
        self.demon_image = ["images/monster1_right.png","images/monster1_left.png"]

    def check_btn(self,x1,x2,y1,y2,sound):
        check = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if x1 <= x <= x2 and y1 <= y <= y2:
            if check[0]:
                sound.play()
                return True
