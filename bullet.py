#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : bullet.py
# @Description 子弹类,继承了pygame中的Sprite类
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game_setting, screen, hero, direction="up"):
        super(Bullet, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(game_setting.bullet_image[hero.level - 1])
        self.rect = self.image.get_rect()
        # 将子弹的初始位置设置为与一致，为了优化子弹射击的视觉效果
        self.rect.centerx = hero.rect.centerx
        self.rect.top = hero.rect.top
        # 用小数表示的子弹位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # 子弹的速度
        self.speed = game_setting.bullet_speed
        # 子弹运行的方向，默认值为up,表示向上
        self.direction = direction
        # 子弹的主人
        self.host = 'hero'

    def update(self):
        if self.host == 'hero':
            if self.direction == "up":
                self.y = self.y - self.speed
                self.rect.y = self.y
            if self.direction == "down":
                self.y = self.y + self.speed
                self.rect.y = self.y
            if self.direction == "left":
                self.x = self.x - self.speed
                self.rect.x = self.x
            if self.direction == "right":
                self.x = self.x + self.speed
                self.rect.x = self.x
        else:
            if self.direction == 1:
                self.x = self.x + self.speed
                self.rect.x = self.x
            if self.direction == -1:
                self.x = self.x - self.speed
                self.rect.x = self.x
        self.screen.blit(self.image, self.rect)

