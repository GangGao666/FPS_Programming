#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : demon.py
# @Description Monster class, inherited from the Sprite class in pygame
import random
import pygame
from pygame.sprite import Sprite


class Demon(Sprite):

    def __init__(self, screen, game_setting):
        super(Demon, self).__init__()
        # Initialize the screen object
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # Setting game parameters
        self.game_setting = game_setting
        # Whether the monster is stopped
        self.stop = 0
        # Monster random left and right walking direction, -1 or 1
        self.direction = random.choice([-1, 1]) * game_setting.demon_direction
        # Determination of left and right direction of travel is based on the determination of 0 or 1 direction,
        # designed for body image display
        self.dir = 0
        # Image parameter settings
        self.image_url = game_setting.demon_image[self.dir]
        self.image = pygame.image.load(self.image_url)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        # The type of the monster, the default value is 'monster'
        self.type_ = 'monster'
        # Monster's damage power Default value is 1
        self.power = 1

    '''
    Override the update function of Sprite. 
    The Groups array in the Sprite class can call this method to make each object in the Groups array execute this method. 
    If the monster is not stopped, it will move normally and display the monster on the screen.
    '''

    def update(self):
        if self.stop == 0:
            self.x = self.x + self.game_setting.demon_speed * self.direction
            self.rect.x = self.x
        self.screen.blit(self.image, self.rect)



    '''
    Determine whether the monster has reached the boundary of the screen
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
    Change the direction of the monster's horizontal movement and switch to the corresponding image
    '''

    def change_direction(self):
        # When it touches the right boundary, the monster drops vertically; when it touches the left boundary,
        # the monster rises vertically
        self.rect.y = self.rect.y + self.game_setting.demon_drop_speed * self.direction
        # Change the direction of horizontal movement at the same time
        self.direction = self.direction * -1
        # When the horizontal movement direction changes, switch the monster image,
        # when the direction is 1, dir is 0, and when the direction is -1, dir is 1
        if self.direction == 1:
            self.dir = 0
            self.image_url = self.image_url.replace("_left", "_right")
            self.image = pygame.image.load(self.image_url)
        elif self.direction == -1:
            self.dir = 1
            self.image_url = self.image_url.replace("_right", "_left")
            self.image = pygame.image.load(self.image_url)
