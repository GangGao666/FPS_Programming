#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : bullet.py
# @Description
"""In this module, bullets are created, added and deleted
    and collision monitoring with monsters are inspired by a python book called
    "Python Crash Course - A Hands-On, Project-Based Introduction to Programming by Eric Matthes", which
    is download from the link:
    https://b-ok.cc/
    Only ideas were learned from it, but no code was copied.

    """

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game_setting, screen, hero, direction="up"):
        super(Bullet, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(game_setting.bullet_image[hero.level - 1])
        self.rect = self.image.get_rect()
        # Set the initial horizontal position of the bullet to be consistent with the hero horizontal position,
        # in order to optimize the visual effect of bullet shooting
        self.rect.centerx = hero.rect.centerx
        self.rect.top = hero.rect.top
        # Bullet position expressed as a decimal
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # 子弹的速度
        self.speed = game_setting.bullet_speed
        # 子弹运行的方向，默认值为up,表示向上
        self.direction = direction


    '''将子弹绘制到屏幕上'''
    def update(self):
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
        self.screen.blit(self.image, self.rect)

