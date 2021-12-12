#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Description Entrance to Fight Mode

import pygame
from demon import Demon
from my_enum import Scene
from setting import Setting
from hero import Hero
import game_functions as gf
from pygame.sprite import Group

'''Basic game function settings, such as adding background sounds, 
designing sound effects, obtaining prop sound effects, and hitting target sound effects'''


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
    # Initialize the hero
    hero = Hero(screen, game_setting)
    # Set level the level of hero
    hero.level = scene
    # Set different appearances for the hero of different levels
    hero.image = pygame.image.load(game_setting.hero_image[hero.level - 1])
    pygame.display.set_caption("The Defence Of Nottingham")
    # Create a group of bullets
    bullets = Group()
    # Create a group of demons
    demons = Group()
    # Create a fleet of demons
    gf.create_fleet(game_setting, screen, demons, scene)
    # Create a group of items
    gifts = Group()
    # Create boss
    boss = Demon(screen, game_setting)
    # Set the image of the boss
    boss.image_url = 'images/boss' + str(scene) + '_right.png'
    boss.image = pygame.image.load(boss.image_url)
    # Set the type of demon to 'boss'
    boss.type_ = "boss"
    # Set different damage powers for the boss of different levels
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
        # If the hero wins, go to the next level
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
    # Update bullet status
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