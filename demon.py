#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : demon.py
# @Description 恶魔类,继承了pygame中的Sprite类
"""In this module, demons are created, added and deleted
    are inspired by a python book called
    "Python Crash Course - A Hands-On, Project-Based Introduction to Programming by Eric Matthes", which
    is download from the link:
    https://b-ok.cc/
    Only ideas were learned from it, but no code was copied.

    """

import random

import pygame
from pygame.sprite import Sprite


class Demon(Sprite):

    def __init__(self, screen, game_setting):
        super(Demon, self).__init__()
        # Initialize the screen object
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # Game parameter settings
        self.game_setting = game_setting
        # Whether to be stopped
        self.stop = 0
        # Left and right walking direction, -1 or 1
        self.direction = random.choice([-1, 1]) * game_setting.demon_direction
        # Left and right walking direction, 0 or 1, based on direction, designed for body image display
        self.dir = 0
        # Path of the demon image
        self.image_url = game_setting.demon_image[self.dir]
        self.image = pygame.image.load(self.image_url)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        # The type of demon, the default value is 'monster'
        self.type_ = 'monster'
        # Devil’s damage default value is 1
        self.power = 1

    '''
    Override the update function of sprite, the groups array in the sprite class can call this method,
     so that each object in the groups array executes this method
    If the demon is not stopped, move normally and display the demon on the screen
    '''

    def update(self):
        if self.stop == 0:
            self.x = self.x + self.game_setting.demon_speed * self.direction
            self.rect.x = self.x
        self.screen.blit(self.image, self.rect)



    '''
    DETERMINE WHETHER THE DEMON HAS REACHED THE BOUNDARY OF THE SCREEN
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
    CHANGE THE DIRECTION OF THE DEMON'S HORIZONTAL MOVEMENT AND SWITCH TO THE CORRESPONDING IMAGE
    '''

    def change_direction(self):
        # When touching the right boundary, the demon descends vertically;
        # when touching the left boundary, the demon rises vertically
        self.rect.y = self.rect.y + self.game_setting.demon_drop_speed * self.direction
        # Change the direction of horizontal movement at the same time
        self.direction = self.direction * -1
        # When the horizontal movement direction is changed, switch the demon image,
        # when the direction is 1, dir is 0, and when the direction is -1, dir is 1
        if self.direction == 1:
            self.dir = 0
            self.image_url = self.image_url.replace("_left", "_right")
            self.image = pygame.image.load(self.image_url)
        elif self.direction == -1:
            self.dir = 1
            self.image_url = self.image_url.replace("_right", "_left")
            self.image = pygame.image.load(self.image_url)
