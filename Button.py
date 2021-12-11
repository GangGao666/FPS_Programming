# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:58:20 2021

@author: Cyc
"""
import pygame

pygame.init()
click_fx = pygame.mixer.Sound("sound/click.wav")
click_fx.set_volume(0.3)


class Button():
    pygame.init()
    click_fx = pygame.mixer.Sound("sound/click.wav")
    click_fx.set_volume(80)

    def __init__(self, x, y, image, font):
        self.x = x
        self.y = y
        self.image = image

    def check_button(self):
        check = pygame.mouse.get_pressed()
        click_x, click_y = pygame.mouse.get_pos()
        if self.x <= click_x <= self.x + 100 and self.y + 100 >= click_y >= self.y:
            if check[0]:
                return True


class Begin():

    def __init__(self, font):
        self.x = 600
        self.y = 400
        # self.image = font.render('Start', True, pygame.Color(37, 4, 4))

    def check_button(self):
        checkbutton = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if 470 <= x <= 795 and 400 >= y >= 300:
            click_fx.play()
            return True


class Parkour():

    def __init__(self, font):
        self.x = 600
        self.y = 400
        # self.image = font.render('Start', True, pygame.Color(37, 4, 4))

    def check_button(self):
        checkbutton = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if 320 <= x <= 920 and 350 >= y >= 240:
            click_fx.play()
            return True


class Fight():

    def __init__(self, font):
        self.x = 600
        self.y = 400
        # self.image = font.render('Start', True, pygame.Color(37, 4, 4))

    def check_button(self):
        checkbutton = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if x >= 310 and x <= 930 and y <= 510 and y >= 400:
            click_fx.play()
            return True


# class End():
#     def __init__(self, font):
#         self.x = 300
#         self.y = 450
#         self.image = font.render('Exit', True, pygame.Color(37, 4, 4))
#
#     def check_button(self):
#         pass


class Help():
    def __init__(self, font):
        self.x = 550
        self.y = 245

    def check_button(self):
        x, y = pygame.mouse.get_pos()
        if x >= 470 and x <= 795 and y <= 540 and y >= 435:
            click_fx.play()
            return True


class About():
    def __init__(self, font):
        self.x = 550
        self.y = 150

    def check_button(self):
        check = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if x >= 470 and x <= 795 and y <= 700 and y >= 580:
            if check[0]:
                click_fx.play()
                return True


class Back():
    def __init__(self, font):
        self.x = 900
        self.y = 25
        self.image = font.render('X', True, pygame.Color(37, 4, 4))

    def check_button(self):
        check = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if x >= 955 and x <= 1200 and y >= 35 and y <= 65:
            if check[0]:
                click_fx.play()
                return True
