#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/5 21:55
# @Author : Xiang Ren
# @File : maingame.py
import sys

import pygame
from setting import Setting
import port

def run_game():
    pygame.init()
    game_setting = Setting()
    pygame.mixer.music.load('sound/piano1.mp3')
    pygame.mixer.music.set_volume(100)
    pygame.mixer.music.play(-1,0.0)
    pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    pygame.display.set_caption("game")
    scene = 1
    while True:
        if scene == 1:
            scene = port.game1(scene)
        if scene == 2:
            scene = port.game2(scene)
        if scene == 3:
            scene = port.game3(scene)
        if scene == 4:
            print("通关了。。。。。。")
            break
run_game()
