#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : game_functions.py
# @Description : 整合了“战斗模式”的函数
import sys
import random
import pygame
from bullet import Bullet
from demon import Demon
from gift import Gift
import numpy as np

'''检查怪物群中的每个怪物是否触及到屏幕边缘，如果是则改变运动方向'''


def check_fleet_edges(game_setting, demons):
    for demon in demons.sprites():
        if demon.check_edges():
            demon.change_direction()


'''更新并追踪主角生存状态，主角的生命值在不断自动下降，当主角的生命值小于等于0时，判定主角死亡'''


def update_hero(game_setting, hero):
    hero.live_volume = hero.live_volume - 0.01
    if hero.live_volume <= 0:
        hero.live_volume = 0
        hero.dead = True


'''检测每个怪物的状态：检查是否触及屏幕边缘'''


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


'''更新掉落道具的状态'''


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
        game_setting.demon_speed = game_setting.demon_speed + 0.1
        collisions = pygame.sprite.spritecollideany(hero, gifts)
        collisions.remove(gifts)


'''更新子弹状态：更新子弹所处位置、检测子弹是否撞击，以及撞击后的对子弹的处理'''


def update_bullets(game_setting, screen, hero, bullets, demons, gifts, collision_sound, scene):
    # todo 通过让Sprite的Group() 数组里的每个bullet对象调用update()方法，让子弹出现
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


'''创建子弹，将子弹加入Sprites的Group数组中'''


def fire_bullet(game_setting, screen, hero, bullets):
    if len(bullets) < game_setting.bullet_allowed:
        new_bullet = Bullet(game_setting, screen, hero)
        new_bullet.direction = hero.direction
        new_bullet.host = 'hero'
        bullets.add(new_bullet)


'''检测键盘敲击事件'''


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


'''检查鼠标、键盘事件'''


def check_events(game_setting, screen, hero, bullets, demons, gifts, shot_sound, bg, scene):
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_setting, screen, hero, bullets, shot_sound, demons)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hero)


'''更新屏幕内子弹、掉落的道具、主角位置'''


def update_screen(game_setting, screen, hero, bullets, demons, gifts):
    bullets.update()
    gifts.update()
    hero.update()
    demons.draw(screen)


'''检查键盘弹起事件'''


def check_keyup_events(event, hero):
    if event.key == pygame.K_d:
        hero.moving_right = False
    if event.key == pygame.K_a:
        hero.moving_left = False
    if event.key == pygame.K_w:
        hero.moving_up = False
    if event.key == pygame.K_s:
        hero.moving_down = False


'''创建怪物群'''


def create_fleet(game_setting, screen, demons, scene):
    for demon_number in range(game_setting.demon_number):
        create_demon(game_setting, screen, demons, demon_number, scene)


'''创建单个怪物'''


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


'''检测boss状态，当主角的杀敌数达到一定数量时，boss出现'''


def update_boss(hero, boss, demons):
    if hero.kill_number == 3:
        demons.add(boss)
        boss.update()
