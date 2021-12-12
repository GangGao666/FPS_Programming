#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : gift.py
# @Description 击杀恶魔后掉落的道具类，继承了pygame中的Sprite类
import pygame
from pygame.sprite import Sprite
import random


class Gift(Sprite):
    def __init__(self, screen, game_setting):
        super(Gift, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 掉落道具的类型，随机生成
        self.gift_type = random.choice(range(len(game_setting.gift_image)))
        self.image = pygame.image.load(game_setting.gift_image[self.gift_type])
        self.rect = self.image.get_rect()

    '''
    重写了Sprite的update函数，Sprite类中的Groups数组可以调用这个方法，
    使得Groups数组中的每个对象执行此方法
    将道具显示在屏幕上
    '''

    def update(self):
        self.screen.blit(self.image, self.rect)
