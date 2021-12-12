#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : game_functions.py
# @Description : Integrated "battle mode" function
import sys
import random
import pygame
from bullet import Bullet
from demon import Demon
from gift import Gift
import numpy as np

'''
Check whether each monster in the monster group touches the edge of the screen, 
if so, change the direction of movement
'''


def check_fleet_edges(game_setting, demons):
    for demon in demons.sprites():
        if demon.check_edges():
            demon.change_direction()


'''
Update and track the hero’s survival status. 
The hero’s health is continuously falling. 
When the hero’s health is less than or equal to 0, 
the hero is judged to be dead
'''


def update_hero(game_setting, hero):
    hero.live_volume = hero.live_volume - 0.01
    if hero.live_volume <= 0:
        hero.live_volume = 0
        hero.dead = True


'''
Detect the status of each monster: 
check whether it touches the edge of the screen
'''


def update_demons(game_setting, bullets, demons, gifts, hero):
    check_fleet_edges(game_setting, demons)
    # 更新怪物位置
    demons.update()
    # 判断是否撞击
    coll = pygame.sprite.spritecollide(hero, demons, False, pygame.sprite.collide_circle)
    if coll:
        demon = pygame.sprite.spritecollideany(hero, demons)
        demon.stop = 1
        image_url = demon.image_url
        image_url_attack = image_url.replace("/", "/attack_")
        demon.image = pygame.image.load([image_url, image_url_attack][np.random.choice([0, 1])])
        if not hero.shield:
            hero.live_volume = hero.live_volume - demon.power
            hero.shield = True
            hero.shield_time = game_setting.hero_shield_time
    else:
        for demon in demons.sprites():
            demon.stop = 0
            demon.image = pygame.image.load(demon.image_url)


'''
Update the status of dropped items
'''


def update_gifts(game_setting, gifts, hero, gift_sound):
    if pygame.sprite.spritecollideany(hero, gifts):
        hero.live_volume = game_setting.hero_live_volume
        gift_sound.play()
        gift_type = pygame.sprite.spritecollideany(hero, gifts).gift_type
        if gift_type == 0:
            hero.hero_speed += 0.1
        if gift_type == 1:
            game_setting.demon_speed = game_setting.demon_speed - 0.1
        if gift_type == 2:
            game_setting.bullet_speed += 0.1
            game_setting.bullet_allowed += 1
        if gift_type in [4, 5, 6]:
            hero.win = True
        # 加快怪物移动速度
        game_setting.demon_speed = game_setting.demon_speed + 0.05
        collisions = pygame.sprite.spritecollideany(hero, gifts)
        collisions.remove(gifts)


'''
Update bullet status: 
update the position of the bullet, 
detect whether the bullet hits, and 
handle the bullet after the hit
'''


def update_bullets(game_setting, screen, hero, bullets, demons, gifts, collision_sound, scene):
    # 装好子弹后，直接将Sprite的Group数组对象调用update()方法，更新子弹位置
    bullets.update()
    # 删除超出屏幕的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= bullet.screen_rect.top:
            bullets.remove(bullet)
        if bullet.rect.top >= bullet.screen_rect.bottom:
            bullets.remove(bullet)
        if bullet.rect.left >= bullet.screen_rect.right:
            bullets.remove(bullet)
        if bullet.rect.right <= bullet.screen_rect.left:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, demons, True, True)
    if collisions:
        hero.kill_number += 1
        collision_sound.play()
    # stack-overflow
    for bullet in collisions:  # each bullet
        for demon in collisions[bullet]:  # each demon that collides with that bullet
            gift = Gift(screen, game_setting)
            gift.rect.x = demon.rect.x
            gift.rect.y = demon.rect.y
            if demon.type_ == 'boss':
                demons.empty()
                hero.finish = True
                gift.gift_type = scene + len(game_setting.gift_image)
                gift.image = pygame.image.load(game_setting.gift_boss_image[scene - 1])
            gifts.add(gift)
    if len(demons) == 1 and not hero.finish:
        bullets.empty()
        create_fleet(game_setting, screen, demons, scene)


'''
Create a bullet, add the bullet to the Group array of Sprites
'''


def fire_bullet(game_setting, screen, hero, bullets):
    # 判断是否小于子弹限制数量
    if len(bullets) < game_setting.bullet_allowed:
        new_bullet = Bullet(game_setting, screen, hero)
        new_bullet.direction = hero.direction
        new_bullet.host = 'hero'
        bullets.add(new_bullet)


'''
Detect keystroke events
'''


def check_keydown_events(event, game_setting, screen, hero, bullets, shot_sound, demons):
    if event.key == pygame.K_d:
        hero.moving_right = True
        hero.direction = "right"
        hero.image = pygame.image.load('images/' + hero.direction + str(hero.level) + '.png')
    if event.key == pygame.K_a:
        hero.moving_left = True
        hero.direction = "left"
        hero.image = pygame.image.load('images/' + hero.direction + str(hero.level) + '.png')
    if event.key == pygame.K_w:
        hero.moving_up = True
        hero.direction = "up"
        hero.image = pygame.image.load('images/' + hero.direction + str(hero.level) + '.png')
    if event.key == pygame.K_s:
        hero.moving_down = True
        hero.direction = "down"
        hero.image = pygame.image.load('images/' + hero.direction + str(hero.level) + '.png')
    elif event.key == pygame.K_j:
        if len(bullets) < game_setting.bullet_allowed:
            shot_sound.play()
        fire_bullet(game_setting, screen, hero, bullets)


'''
Check mouse and keyboard events
'''


def check_events(game_setting, screen, hero, bullets, demons, gifts, shot_sound, bg, scene):
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_setting, screen, hero, bullets, shot_sound, demons)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hero)


'''
Update bullets, dropped items, hero positions on the screen
'''


def update_screen(game_setting, screen, hero, bullets, demons, gifts):
    bullets.update()
    gifts.update()
    hero.update()
    demons.update()


'''
Check keyboard up event
'''


def check_keyup_events(event, hero):
    if event.key == pygame.K_d:
        hero.moving_right = False
    if event.key == pygame.K_a:
        hero.moving_left = False
    if event.key == pygame.K_w:
        hero.moving_up = False
    if event.key == pygame.K_s:
        hero.moving_down = False


'''
Create a monster group
'''


def create_fleet(game_setting, screen, demons, scene):
    for demon_number in range(game_setting.demon_number):
        create_demon(game_setting, screen, demons, demon_number, scene)


'''
Create a single monster
'''


def create_demon(game_setting, screen, demons, demon_number, scene):
    demon = Demon(screen, game_setting)
    demon_width = demon.rect.width
    demon_height = demon.rect.height
    demon.image_url = game_setting.demon_image[demon.dir]
    demon.image_url = demon.image_url.replace("1_", str(scene) + "_")
    demon.image = pygame.image.load(demon.image_url)
    demon.x = demon_width + 1 * demon_width * demon_number
    demon.rect.x = random.randrange(0, game_setting.screen_width - demon_width)
    demon.rect.y = random.randrange(0, game_setting.screen_height - 2 * demon_height)
    demons.add(demon)


'''
Detect the boss status, when the hero kills a certain number of enemies, the boss appears
'''


def update_boss(hero, boss, demons):
    if hero.kill_number == 3:
        demons.add(boss)
        boss.update()
