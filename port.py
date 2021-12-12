#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Description Fight Mode的入口

import pygame
from demon import Demon
from my_enum import Scene
from setting import Setting
from hero import Hero
import game_functions as gf
from pygame.sprite import Group

'''游戏基本功能设置，例如添加背景声音、设计音效、获取道具音效、击中目标音效'''


def pre_prepare(scene):
    scene = scene - 7
    bg = pygame.image.load('./images/bg' + str(scene+3) + '.png').convert()
    bg = pygame.transform.scale(bg, (1200, 800))
    game_setting = Setting()
    gift_sound = pygame.mixer.Sound('sound/gift4.mp3')
    gift_sound.set_volume(0.1)
    shot_sound = pygame.mixer.Sound('sound/attack.mp3')
    shot_sound.set_volume(0.1)
    collision_sound = pygame.mixer.Sound('sound/collision2.mp3')
    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    # 初始化英雄
    hero = Hero(screen, game_setting)
    # 设置英雄等级
    hero.level = scene
    # 为不同等级的英雄设置不同外表
    hero.image = pygame.image.load(game_setting.hero_image[hero.level - 1])
    pygame.display.set_caption("The Defence Of Nottingham")
    # 创建子弹的Group群组
    bullets = Group()
    # 创建恶魔的Group群组
    demons = Group()
    # 创建恶魔群
    gf.create_fleet(game_setting, screen, demons, scene)
    # 创建道具的Group群组
    gifts = Group()
    # 创建boss
    boss = Demon(screen, game_setting)
    # 设置boss图像
    boss.image_url = 'images/boss' + str(scene) + '_right.png'
    boss.image = pygame.image.load(boss.image_url)
    # 将恶魔类型设置为‘boss’
    boss.type_ = "boss"
    # 为不同关卡的boss设置不同的伤害力
    boss.power = scene + 1
    return game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss,bg,scene


'''ENTRANCE TO THE FIRST LEVEL OF FIGHT MODE'''


def game1(scene):
    game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss,bg,scene = pre_prepare(
        scene)
    while True:
        game_body(game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss, bg,
                  scene)
        # If the hero dies, jump to the failure page
        if hero.dead:
            return Scene.FAIL.value
        # 如果英雄胜利，进入下一关
        if hero.win:
            return Scene.MODE2_GAME2.value
        pygame.display.flip()


'''ENTRANCE TO THE SECOND LEVEL OF FIGHT MODE'''


def game2(scene):
    game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss,bg,scene = pre_prepare(
        scene)
    while True:
        game_body(game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss, bg,
                  scene)
        # If the hero dies, jump to the failure page
        if hero.dead:
            return Scene.FAIL.value
        # If the hero wins, go to the next level
        if hero.win:
            return Scene.MODE2_GAME3.value
        pygame.display.flip()


'''ENTRANCE TO THE THIRD LEVEL OF FIGHT MODE'''


def game3(scene):
    game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss,bg,scene = pre_prepare(
        scene)
    while True:
        game_body(game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss, bg,
                  scene)
        # If the hero dies, jump to the failure page
        if hero.dead:
            return Scene.FAIL.value
        # If the hero wins, jump to the success page
        if hero.win:
            return Scene.SUCCESS.value
        pygame.display.flip()


def game_body(game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss, bg,
              scene):
    # When the hero is invincible
    if hero.shield:
        # todo setting
        # Hero's invincibility time reduced
        hero.shield_time = hero.shield_time - 0.5
        # When the hero's invincibility time is less than or equal to 0
        if hero.shield_time <= 0:
            # Hero's invincibility is off
            hero.shield = False
    # Check mouse and keyboard events
    gf.check_events(game_setting, screen, hero, bullets, demons, gifts, shot_sound, bg, scene)
    # Hero moves
    hero.move()
    # 更新子弹状态
    gf.update_bullets(game_setting, screen, hero, bullets, demons, gifts, collision_sound, scene)
    # Check the status of each demon
    gf.update_demons(game_setting, bullets, demons, gifts, hero)
    # Update the status of dropped items
    gf.update_gifts(game_setting, gifts, hero, gift_sound)
    # Update and track hero survival status
    gf.update_hero(game_setting, hero)
    # Check boss status
    gf.update_boss(hero, boss, demons)
    # Load the hero's remaining HP image
    life_rect = pygame.image.load("images/life.png")
    # Dynamically display the hero's remaining HP
    life_ = pygame.transform.scale(life_rect, (
        life_rect.get_rect()[2] * abs(hero.live_volume), life_rect.get_rect()[3]))
    screen.blit(life_, (10, 10))
    # Update bullets, dropped items, hero positions on the screen
    gf.update_screen(game_setting, screen, hero, bullets, demons, gifts)