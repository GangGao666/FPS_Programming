#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : gift.py
# @Description The item class dropped after killing the demon inherits the Sprite class in pygame
import pygame
from pygame.sprite import Sprite
import random


class Gift(Sprite):
    def __init__(self, screen, game_setting):
        super(Gift, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # The type of dropped items, randomly generated
        self.gift_type = random.choice(range(len(game_setting.gift_image)))
        self.image = pygame.image.load(game_setting.gift_image[self.gift_type])
        self.rect = self.image.get_rect()

    '''
    Override the update function of Sprite, the Groups array in the Sprite class can call this method，
    Make each object in the Groups array execute this method
    Display the props on the screen
    '''

    def update(self):
        self.screen.blit(self.image, self.rect)
