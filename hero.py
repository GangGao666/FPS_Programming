#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : hero.py
# @Description the class of hero
import pygame


class Hero:
    def __init__(self, screen, game_setting):
        self.screen = screen
        # the level of hero
        self.level = 0
        self.image = pygame.image.load(game_setting.hero_image[self.level])
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Set the initial position of the hero to the bottom middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Whether the hero keeps moving right
        self.moving_right = False
        # Whether the hero keeps moving left
        self.moving_left = False
        # Whether the hero keeps moving up
        self.moving_up = False
        # Whether the hero keeps moving down
        self.moving_down = False
        # the speed of hero
        self.hero_speed = game_setting.hero_speed
        # The direction of the hero's movement ,the default value is "up", which can be up/down/left/right
        self.direction = "up"
        # Hero's HP
        self.live_volume = game_setting.hero_live_volume
        # Collision radius between hero and demon
        self.radius = 0.5
        # Whether the hero is invincible
        self.shield = False
        # The duration of the hero's invincible state
        self.shield_time = game_setting.hero_shield_time
        # Hero kills
        self.kill_number = 0
        # Whether the hero picks up the props dropped by the boss
        self.win = False
        # Whether the hero is dead
        self.dead = False

    '''
    Override the update function of Sprite, the Groups array in the Sprite class can call this method，
    Make each object in the Groups array execute this method
    Show the hero on the screen
    '''

    def update(self):
        self.screen.blit(self.image, self.rect)

    '''Move the hero continuously and make sure it is active within the range of the screen'''


    def move(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx = self.rect.centerx + self.hero_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx = self.rect.centerx - self.hero_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.centery = self.rect.centery - self.hero_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery = self.rect.centery + self.hero_speed
