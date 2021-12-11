#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/7 22:09
# @Author : Seeumt
# @File : gift.py
import pygame
from pygame.sprite import Sprite
import random

class Gift(Sprite):
    def __init__(self,screen,game_setting):
        super(Gift, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.gift_type = random.choice(range(len(game_setting.gift_image)))
        self.image = pygame.image.load(game_setting.gift_image[self.gift_type])
        self.rect = self.image.get_rect()

    def update(self):
        self.screen.blit(self.image, self.rect)

    def appear(self):
        self.screen.blit(self.image, self.rect)