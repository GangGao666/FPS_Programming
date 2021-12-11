#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/6 19:48
# @Author : Seeumt
# @File : bullet.py
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # todo 子弹和飞船建立起关系，飞船作为子弹构造函数的参数
    def __init__(self, game_setting, screen, ship, direction="up"):
        super(Bullet, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # todo 可以自行创建矩形 pygame.Rect()
        # self.image = pygame.image.load(ship.image)
        self.image = pygame.image.load(game_setting.bullet_image[ship.level-1])
        self.rect = self.image.get_rect()

        # self.rect = pygame.Rect(0,0,game_setting.bullet_width,game_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        # 要从飞船中射出子弹，最起初是隐藏在子弹里的
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        # todo 可以通过rect对象获取y坐标
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.color = game_setting.bullet_color
        self.speed = game_setting.bullet_speed

        self.direction = direction
        self.host = 'ship'

    # todo 因为这个继承了精灵类 所以需要重写这个方法;
    #  这个方法的作用是对bullets里的每个bullet执行操作？更新位置？
    def update(self):
        if self.host == 'ship':
            # print("飞船的子弹")
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
            # print("外星人的子弹")
            if self.direction == -1:
                self.x = self.x - self.speed
                self.rect.x = self.x

            # self.image = pygame.image.load('images/1.gif')
            # print(self.rect.y)

    # todo pygame.draw.rect和screen.blit的区别：一个只是有阴影，一个可以加载自定义图片
    def appear(self):
        self.screen.blit(self.image, self.rect)
        # pygame.draw.rect(self.screen,self.color,self.rect)
