#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/7 14:31
# @Author : Seeumt
# @File : alien.py
import random

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, screen, game_setting):
        super(Alien, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_setting = game_setting
        self.stop = 0
        self.dir = 0
        self.image_url = game_setting.alien_image[self.dir]
        self.image = pygame.image.load(self.image_url)
        self.rect = self.image.get_rect()

        # todo centerx 与 x 的区别
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.direction = 1

        self.type_ = 'monster'


        self.power = 1



    def blitAlien(self):
        self.screen.blit(self.image, self.rect)



    def update(self):
        if self.stop == 0:
            self.x = self.x + self.game_setting.alien_speed * self.direction
            self.rect.x = self.x

    def appear(self):

        if self.stop == 0:
            self.x = self.x + self.game_setting.alien_speed * self.direction
            self.rect.x = self.x
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right:
            return True
        if self.rect.left <= 0:
            return True
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        if self.rect.top <= 0:
            return True

    def change_direction(self):

        self.rect.y = self.rect.y + self.game_setting.alien_drop_speed*self.direction
        self.direction = self.direction * -1
        if self.direction == 1:
            self.dir = 0
            # if self.type_ == 'boss':
            #     self.image_url = 'images/boss0.png'
            # elif self.type_ =='monster':
                # pass
            self.image_url = self.image_url.replace("_left","_right")
                # self.image_url = self.game_setting.alien_image[self.dir]
            self.image = pygame.image.load(self.image_url)
        elif self.direction ==-1:
            self.dir = 1
            # if self.type_ == 'boss':
            #     self.image_url = 'images/boss0.png'
            # elif self.type_ == 'monster':
            self.image_url = self.image_url.replace("_right","_left")
                # self.image_url = self.game_setting.alien_image[self.dir]
            self.image = pygame.image.load(self.image_url)

