#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Description

import pygame
from demon import Demon
from setting import Setting
from hero import Hero
import game_functions as gf
from pygame.sprite import Group

'''游戏基本功能设置，例如添加背景声音、设计音效、获取道具音效、击中目标音效'''


def pre_prepare(scene):
    game_setting = Setting()
    pygame.mixer.music.load('sound/piano1.mp3')
    pygame.mixer.music.set_volume(100)
    pygame.mixer.music.play(-1, 0.0)
    gift_sound = pygame.mixer.Sound('sound/gift4.mp3')
    shot_sound = pygame.mixer.Sound('sound/attack.mp3')
    collision_sound = pygame.mixer.Sound('sound/collision2.mp3')
    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    hero = Hero(screen, game_setting)
    hero.level = scene
    hero.image = pygame.image.load(game_setting.hero_image[hero.level - 1])
    pygame.display.set_caption("game")
    bullets = Group()
    demons = Group()
    gf.create_fleet(game_setting, screen, demons, scene)
    gifts = Group()
    boss = Demon(screen, game_setting)
    boss.image_url = 'images/boss' + str(scene) + '_right.png'
    boss.image = pygame.image.load(boss.image_url)
    boss.type_ = "boss"
    boss.power = scene + 1
    return game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss


'''Fight模式第一关游戏入口'''


def game1(scene):
    scene = scene - 7
    bg = pygame.image.load('./images/bg' + str(scene) + '.png').convert()
    game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss = pre_prepare(
        scene)
    while True:
        if hero.shield:
            hero.shield_time = hero.shield_time - 0.5
            if hero.shield_time <= 0:
                hero.shield = False
        gf.check_events(game_setting, screen, hero, bullets, demons, gifts, shot_sound, bg, scene)
        hero.move()
        gf.update_bullets(game_setting, screen, hero, bullets, demons, gifts, collision_sound, scene)
        gf.update_demons(game_setting, bullets, demons, gifts, hero)
        gf.update_gifts(game_setting, gifts, hero, gift_sound)
        gf.update_hero(game_setting, hero)
        gf.update_boss(hero, boss, demons)
        life_rect = pygame.image.load("images/life.png")
        life_ = pygame.transform.scale(life_rect, (
            life_rect.get_rect()[2] * abs(hero.live_volume), life_rect.get_rect()[3]))
        screen.blit(life_, (10, 10))
        gf.update_screen(game_setting, screen, hero, bullets, demons, gifts)
        if hero.dead:
            return 6
        if hero.win:
            return 9
        pygame.display.flip()


'''Fight模式第二关游戏入口'''


def game2(scene):
    scene = scene - 7
    bg = pygame.image.load('./images/bg' + str(scene) + '.png').convert()
    game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss = pre_prepare(
        scene)
    while True:
        if hero.shield:
            hero.shield_time = hero.shield_time - 0.5
            if hero.shield_time <= 0:
                hero.shield = False
        gf.check_events(game_setting, screen, hero, bullets, demons, gifts, shot_sound, bg,
                        scene)
        hero.move()
        gf.update_bullets(game_setting, screen, hero, bullets, demons, gifts, collision_sound, scene)
        gf.update_demons(game_setting, bullets, demons, gifts, hero)
        gf.update_gifts(game_setting, gifts, hero, gift_sound)
        gf.update_hero(game_setting, hero)
        gf.update_boss(hero, boss, demons)
        life_rect = pygame.image.load("images/life.png")
        life_ = pygame.transform.scale(life_rect, (
            life_rect.get_rect()[2] * abs(hero.live_volume), life_rect.get_rect()[3]))
        screen.blit(life_, (10, 10))
        gf.update_screen(game_setting, screen, hero, bullets, demons, gifts)
        if hero.dead:
            return 6
        if hero.win:
            return 10
        pygame.display.flip()


'''Fight模式第三关游戏入口'''


def game3(scene):
    scene = scene - 7
    bg = pygame.image.load('./images/bg' + str(scene) + '.png').convert()
    game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss = pre_prepare(
        scene)
    while True:
        if hero.shield:
            hero.shield_time = hero.shield_time - 0.5
            if hero.shield_time <= 0:
                hero.shield = False
        gf.check_events(game_setting, screen, hero, bullets, demons, gifts, shot_sound, bg,
                        scene)
        hero.move()
        gf.update_bullets(game_setting, screen, hero, bullets, demons, gifts, collision_sound, scene)
        gf.update_demons(game_setting, bullets, demons, gifts, hero)
        gf.update_gifts(game_setting, gifts, hero, gift_sound)
        gf.update_hero(game_setting, hero)
        gf.update_boss(hero, boss, demons)
        life_rect = pygame.image.load("images/life.png")
        life_ = pygame.transform.scale(life_rect, (
            life_rect.get_rect()[2] * abs(hero.live_volume), life_rect.get_rect()[3]))
        screen.blit(life_, (10, 10))
        gf.update_screen(game_setting, screen, hero, bullets, demons, gifts)
        if hero.dead:
            return 6
        if hero.win:
            return 5
        pygame.display.flip()
