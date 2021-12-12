#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : hero.py
# @Description 英雄类
import pygame


class Hero:
    def __init__(self, screen, game_setting):
        self.screen = screen
        # 英雄等级
        self.level = 0
        self.image = pygame.image.load(game_setting.hero_image[self.level])
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.hero_speed = game_setting.hero_speed
        # 英雄移动方向 默认值为"up",可以为up/down/left/right
        self.direction = "up"
        # 英雄生命值
        self.live_volume = game_setting.hero_live_volume
        # 英雄与怪物的碰撞半径
        self.radius = 0.5
        # 英雄是否处于无敌状态
        self.shield = False
        # 英雄无敌状态的持续时长
        self.shield_time = game_setting.hero_shield_time
        # 英雄的击杀数目
        self.kill_number = 0
        # 英雄是否击杀boss
        self.finish = False
        # 英雄是否拾取boss跌落的道具
        self.win = False
        # 英雄是否死亡
        self.dead = False

    '''
    重写了Sprite的update函数，Sprite类中的Groups数组可以调用这个方法，
    使得Groups数组中的每个对象执行此方法
    将主角显示在屏幕上
    '''

    def update(self):
        self.screen.blit(self.image, self.rect)

    '''连续移动主角并确保其活动范围不超过屏幕'''


    def move(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx = self.rect.centerx + self.hero_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx = self.rect.centerx - self.hero_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.centery = self.rect.centery - self.hero_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery = self.rect.centery + self.hero_speed
