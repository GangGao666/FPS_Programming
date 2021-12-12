#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : bullet.py
# @Description The bullet class, which inherits the Sprite class in pygame
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
        # Bullet speed
        self.speed = game_setting.bullet_speed
        # The direction in which the bullet runs, the default value is up, which means upward
        self.direction = direction


    '''DRAW THE BULLET TO THE SCREEN'''
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

