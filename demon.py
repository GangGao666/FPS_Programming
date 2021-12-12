#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : demon.py
# @Description 怪物类,继承了pygame中的Sprite类
import random

import pygame
from pygame.sprite import Sprite


class Demon(Sprite):

    def __init__(self, screen, game_setting):
        super(Demon, self).__init__()
        # 初始化屏幕对象
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # 游戏参数设置
        self.game_setting = game_setting
        # 是否被截停
        self.stop = 0
        # 左右行走方向，-1或1
        self.direction = random.choice([-1, 1]) * game_setting.demon_direction
        # 左右行走方向，0或1,基于direction,为了体态图像展示而设计
        self.dir = 0
        # 图像路径
        self.image_url = game_setting.demon_image[self.dir]
        self.image = pygame.image.load(self.image_url)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        # 怪物的类型，默认值为'monster'
        self.type_ = 'monster'
        # 怪物的伤害力 默认值为1
        self.power = 1

    '''
    重写了Sprite的update函数，Sprite类中的Groups数组可以调用这个方法，
    使得Groups数组中的每个对象执行此方法
    如果怪物没有被截停，则正常运动,并将怪物显示在屏幕上
    '''

    def update(self):
        if self.stop == 0:
            self.x = self.x + self.game_setting.demon_speed * self.direction
            self.rect.x = self.x
        self.screen.blit(self.image, self.rect)



    '''
    判断怪物是否到达了屏幕边界
    '''

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        if self.rect.top <= 0:
            return True

    '''
    改变怪物水平运动方向并切换为相应的图像
    '''

    def change_direction(self):
        # 当触及右侧边界时，怪物垂直下降；当触及左侧边界时，怪物垂直上升
        self.rect.y = self.rect.y + self.game_setting.demon_drop_speed * self.direction
        # 同时改变水平移动方向
        self.direction = self.direction * -1
        # 当水平移动方向改变时，切换怪物图像，direction为1时，dir为0，direction为-1时，dir为1
        if self.direction == 1:
            self.dir = 0
            self.image_url = self.image_url.replace("_left", "_right")
            self.image = pygame.image.load(self.image_url)
        elif self.direction == -1:
            self.dir = 1
            self.image_url = self.image_url.replace("_right", "_left")
            self.image = pygame.image.load(self.image_url)
