# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 21:58:20 2021

@author: Cyc
"""
import pygame

class Button():

    def __init__(self,x,y,image,font):
        self.x = x
        self.y = y
        self.image = image

    def check_button(self):
        check = pygame.mouse.get_pressed()
        click_x, click_y = pygame.mouse.get_pos()
        if click_x >= self.x and click_x <= self.x+100 and click_y <= self.y+100 and y >= self.y:
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
        if x >= 470 and x <= 795 and y <= 400 and y >= 300:
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
                return True


class Back():
    def __init__(self, font):
        self.x = 900
        self.y = 25
        self.image = font.render('X', True, pygame.Color(37, 4, 4))

    def check_button(self):
        check = pygame.mouse.get_pressed()
        x, y = pygame.mouse.get_pos()
        if x >= 900 and x <= 995 and y >= 35 and y <= 65:
            if check[0]:
                return True