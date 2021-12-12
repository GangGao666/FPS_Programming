#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File: Button.py
# @Description: Define button

import pygame
from setting import Setting
pygame.init()
click_fx = pygame.mixer.Sound("sound/click.wav")
click_fx.set_volume(0.3)

class Button:
    pygame.init()
    click_fx = pygame.mixer.Sound("sound/click.wav")
    click_fx.set_volume(80)

# Begin button, check if it's clicked
class Begin:

    def check_button(self):
        return Setting().check_btn(470, 795, 300, 400, click_fx)

# Parkour button, check if it's clicked
class Parkour:

    def check_button(self):
        return Setting().check_btn(320, 920, 240, 350, click_fx)

# Fight button, check if it's clicked
class Fight:
    def check_button(self):
        return Setting().check_btn(310, 930, 400, 510, click_fx)

# Help button, check if it's clicked
class Help:
    def check_button(self):
        return Setting().check_btn(470,795,435,540,click_fx)

# About button, check if it's clicked
class About:
    def check_button(self):
        return Setting().check_btn(470,795,580,700,click_fx)

# Back button, check if it's clicked
class Back:
    def check_button(self):
        return Setting().check_btn(955,1200,35,65,click_fx)