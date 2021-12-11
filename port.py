#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/10 20:19
# @Author : Seeumt
# @File : port.py

import pygame

from alien import Alien
from game_stats import GameStats
from gift import Gift
from setting import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def pre_prepare(scene):
    game_setting = Setting()

    pygame.mixer.music.load('sound/piano1.mp3')
    pygame.mixer.music.set_volume(100)
    pygame.mixer.music.play(-1, 0.0)
    gift_sound = pygame.mixer.Sound('sound/gift4.mp3')
    shot_sound = pygame.mixer.Sound('sound/attack.mp3')
    collision_sound = pygame.mixer.Sound('sound/collision2.mp3')
    screen = pygame.display.set_mode((game_setting.screen_width, game_setting.screen_height))
    ship = Ship(screen, game_setting)
    ship.level = scene
    ship.image = pygame.image.load(game_setting.ship_image[ship.level-1])
    pygame.display.set_caption("game")
    bullets = Group()
    aliens = Group()
    alien_bullets_1 = Group()
    gf.create_fleet(game_setting, screen, aliens, scene)
    gifts = Group()
    boss = Alien(screen, game_setting)
    boss.image_url = 'images/boss' + str(scene) + '_right.png'
    boss.image = pygame.image.load(boss.image_url)
    boss.type_ = "boss"
    boss.power = scene + 1

    stats = GameStats(game_setting)
    return game_setting, gift_sound, shot_sound, collision_sound, screen, ship, bullets, aliens, alien_bullets_1, gifts, stats, boss


def game1(scene):


    bg = pygame.image.load('./images/bg'+str(scene)+'.png').convert()
    game_setting, gift_sound, shot_sound, collision_sound, screen, ship, bullets, aliens, alien_bullets_1, gifts, stats, boss = pre_prepare(
        scene)

    while True:
        if ship.wudi:
            ship.wudi_time = ship.wudi_time - 0.5
            if ship.wudi_time <= 0:
                ship.wudi = False
        gf.check_events(game_setting, screen, ship, bullets, aliens, gifts, shot_sound, bg, stats,alien_bullets_1, scene)

        if stats.game_active:
            ship.move()
            gf.update_bullets(game_setting, screen, ship, bullets, aliens, gifts, collision_sound, scene)
            gf.update_aliens(game_setting, bullets, aliens, gifts, ship, stats)
            gf.update_gifts(game_setting, gifts, ship, gift_sound)
            gf.update_ship(game_setting, ship, stats)
            gf.update_test(ship, boss, aliens)
            life_rect = pygame.image.load("images/life.png")
            life_ = pygame.transform.scale(life_rect, (
                life_rect.get_rect()[2] * abs(ship.live_volume), life_rect.get_rect()[3]))
            screen.blit(life_, (10, 10))



        gf.update_screen(game_setting, screen, ship, bullets, aliens, gifts, stats, alien_bullets_1)

        if ship.dead:
            return 6
        if ship.win:
            return 9


        pygame.display.flip()


def game2(scene):
    bg = pygame.image.load('./images/bg'+str(scene)+'.png').convert()
    game_setting, gift_sound, shot_sound, collision_sound, screen, ship, bullets, aliens, alien_bullets_1, gifts, stats, boss = pre_prepare(
        scene)
    while True:
        if ship.wudi:
            ship.wudi_time = ship.wudi_time - 0.5
            if ship.wudi_time <= 0:
                ship.wudi = False
        gf.check_events(game_setting, screen, ship, bullets, aliens, gifts, shot_sound, bg, stats, alien_bullets_1,
                        scene)

        if stats.game_active:
            ship.move()
            gf.update_bullets(game_setting, screen, ship, bullets, aliens, gifts, collision_sound, scene)
            gf.update_aliens(game_setting, bullets, aliens, gifts, ship, stats)
            gf.update_gifts(game_setting, gifts, ship, gift_sound)
            gf.update_ship(game_setting, ship, stats)
            gf.update_test(ship, boss, aliens)
            life_rect = pygame.image.load("images/life.png")
            life_ = pygame.transform.scale(life_rect, (
                life_rect.get_rect()[2] * abs(ship.live_volume), life_rect.get_rect()[3]))
            screen.blit(life_, (10, 10))

        gf.update_screen(game_setting, screen, ship, bullets, aliens, gifts, stats, alien_bullets_1)

        if ship.dead:
            return 6
        if ship.win:
            return 10

        pygame.display.flip()


def game3(scene):
    bg = pygame.image.load('./images/bg'+str(scene)+'.png').convert()
    game_setting, gift_sound, shot_sound, collision_sound, screen, ship, bullets, aliens, alien_bullets_1, gifts, stats, boss = pre_prepare(
        scene)

    while True:
        if ship.wudi:
            ship.wudi_time = ship.wudi_time - 0.5
            if ship.wudi_time <= 0:
                ship.wudi = False
        gf.check_events(game_setting, screen, ship, bullets, aliens, gifts, shot_sound, bg, stats, alien_bullets_1,
                        scene)

        if stats.game_active:
            ship.move()
            gf.update_bullets(game_setting, screen, ship, bullets, aliens, gifts, collision_sound, scene)
            gf.update_aliens(game_setting, bullets, aliens, gifts, ship, stats)
            gf.update_gifts(game_setting, gifts, ship, gift_sound)
            gf.update_ship(game_setting, ship, stats)
            gf.update_test(ship, boss, aliens)
            life_rect = pygame.image.load("images/life.png")
            life_ = pygame.transform.scale(life_rect, (
                life_rect.get_rect()[2] * abs(ship.live_volume), life_rect.get_rect()[3]))
            screen.blit(life_, (10, 10))

        gf.update_screen(game_setting, screen, ship, bullets, aliens, gifts, stats, alien_bullets_1)

        if ship.dead:
            return 6
        if ship.win:
            return 5

        pygame.display.flip()

