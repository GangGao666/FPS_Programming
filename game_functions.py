#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/12/6 13:30
# @Author : Seeumt
# @File : game_functions.py
import sys
import random
import pygame
from bullet import Bullet
from alien import Alien
from gift import Gift
import numpy as np
from pygame.sprite import Group
import time


def change_alien_direction(game_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y = alien.rect.y + game_setting.alien_drop_speed
    game_setting.alien_direction = game_setting.alien_direction * -1


def check_fleet_edges(game_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            alien.change_direction()
            break


def update_ship(game_setting, ship, stats):
    ship.live_volume = ship.live_volume - 0.01
    if ship.live_volume <= 0:
        dead_gameover(stats, ship, game_setting)


# todo 主角会自己动，主要原因是下面这个for循环监听事件
def update_aliens(game_setting, bullets, aliens, gifts, ship, stats):
    check_fleet_edges(game_setting, aliens)
    aliens.update()
    coll = pygame.sprite.spritecollide(ship, aliens, False, pygame.sprite.collide_circle)
    if coll:
        alien = pygame.sprite.spritecollideany(ship, aliens)
        alien.stop = 1
        image_url = alien.image_url
        image_url_attack = image_url.replace("/", "/attack_")
        alien.image = pygame.image.load([image_url, image_url_attack][np.random.choice([0, 1])])
        if not ship.wudi:
            ship.live_volume = ship.live_volume - alien.power
            ship.wudi = True
            ship.wudi_time = game_setting.ship_wudi_time
    else:
        for alien in aliens.sprites():
            alien.stop = 0
            alien.image = pygame.image.load(alien.image_url)


def update_gifts(game_setting, gifts, ship, gift_sound):
    # todo 新函数 spritecollideany(ship,aliens)
    if pygame.sprite.spritecollideany(ship, gifts):
        ship.live_volume = game_setting.ship_live_volume
        gift_sound.play()

        gift_type = pygame.sprite.spritecollideany(ship, gifts).gift_type
        if gift_type == 0:
            ship.ship_speed += 0.1
        if gift_type == 1:
            game_setting.alien_speed = game_setting.alien_speed - 0.1
        if gift_type == 2:
            game_setting.bullet_speed += 0.1
            game_setting.bullet_allowed += 1
        if gift_type in [4, 5, 6]:
            ship.win = True

        game_setting.alien_speed = game_setting.alien_speed + 0.2
        collisions = pygame.sprite.spritecollideany(ship, gifts)
        collisions.remove(gifts)


def update_bullets(game_setting, screen, ship, bullets, aliens, gifts, collision_sound, scene):
    # todo 通过让Sprite的Group() 数组里的每个bullet对象调用update()方法，让子弹出现
    # 装好子弹后，直接将Sprite的Group数组对象调用update()方法
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= bullet.screen_rect.top:
            bullets.remove(bullet)
        if bullet.rect.top >= bullet.screen_rect.bottom:
            bullets.remove(bullet)
        if bullet.rect.left >= bullet.screen_rect.right:
            bullets.remove(bullet)
        if bullet.rect.right <= bullet.screen_rect.left:
            bullets.remove(bullet)
    # todo pygame.sprite.groupcollide 碰撞功能 除此之外，如何实现掉落

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        ship.kill_number += 1
        collision_sound.play()
    for bullet in collisions:  # each bullet
        for alien in collisions[bullet]:  # each alien that collides with that bullet

            gift = Gift(screen, game_setting)
            gift.rect.x = alien.rect.x
            gift.rect.y = alien.rect.y

            if alien.type_ == 'boss':
                aliens.empty()
                ship.finish = True
                gift.gift_type = scene + 3
                gift.image = pygame.image.load(game_setting.gift_boss_image[scene - 1])

            gifts.add(gift)
    if len(aliens) == 1 and not ship.finish:
        bullets.empty()
        create_fleet(game_setting, screen, aliens, scene)


# 1.创建子弹，将子弹加入Sprites的Group数组中
def fire_bullet(game_setting, screen, ship, bullets):
    if len(bullets) < game_setting.bullet_allowed:
        new_bullet = Bullet(game_setting, screen, ship)
        new_bullet.direction = ship.direction
        new_bullet.host = 'ship'
        bullets.add(new_bullet)


def alien_attack(game_setting, screen, aliens, alien_bullets_1):
    for alien in aliens.sprites():
        new_bullet = Bullet(game_setting, screen, alien)
        new_bullet.host = 'alien'
        alien_bullets_1.add(new_bullet)



def alien_fire_bullet(game_setting, screen, alien, alien_bullets):
    new_bullet = Bullet(game_setting, screen, alien)
    new_bullet.host = 'alien'
    new_bullet.direction = alien.direction
    alien_bullets.add(new_bullet)

    return alien_bullets


def check_keydown_events(event, game_setting, screen, ship, bullets, shot_sound, aliens, alien_bullets_1, stats):
    if event.key == pygame.K_d:
        # print("向右走")
        ship.moving_right = True
        ship.direction = "right"
        # ship.image = pygame.image.load('images/player_right.png')
        ship.image = pygame.image.load('images/' + ship.direction + str(ship.level) + '.png')
    if event.key == pygame.K_a:
        # print("向左走")
        ship.moving_left = True
        ship.direction = "left"
        # ship.image = pygame.image.load('images/player_left.png')
        ship.image = pygame.image.load('images/' + ship.direction + str(ship.level) + '.png')
    if event.key == pygame.K_w:
        # print("向上走")
        ship.moving_up = True
        ship.direction = "up"
        # ship.image = pygame.image.load('images/player_back.png')
        ship.image = pygame.image.load('images/' + ship.direction + str(ship.level) + '.png')
    if event.key == pygame.K_s:
        ship.moving_down = True
        ship.direction = "down"
        # ship.image = pygame.image.load('images/player_front.png')
        ship.image = pygame.image.load('images/' + ship.direction + str(ship.level) + '.png')

    elif event.key == pygame.K_j:
        if len(bullets) < game_setting.bullet_allowed and stats.game_active:
            shot_sound.play()
        fire_bullet(game_setting, screen, ship, bullets)
    elif event.key == pygame.K_F1:
        alien_attack(game_setting, screen, aliens, alien_bullets_1)


def check_events(game_setting, screen, ship, bullets, aliens, gifts, shot_sound, bg, stats,
                 alien_bullets_1, scene):
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_setting, screen, ship, bullets, shot_sound, aliens, alien_bullets_1, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_setting, screen, ship, bullets, aliens, gifts, stats, alien_bullets_1):
    for bullet in bullets.sprites():
        bullet.appear()
    for gift in gifts.sprites():
        gift.appear()
    for alien_bullet in alien_bullets_1.sprites():
        alien_bullet.appear()
    ship.appear()
    aliens.draw(screen)


def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_w:
        ship.moving_up = False
    if event.key == pygame.K_s:
        ship.moving_down = False


def create_fleet(game_setting, screen, aliens, scene):
    for alien_number in range(game_setting.alien_number):
        create_alien(game_setting, screen, aliens, alien_number, scene)


def create_alien(game_setting, screen, aliens, alien_number, scene):
    alien = Alien(screen, game_setting)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.image_url = game_setting.alien_image[alien.dir]
    alien.image_url = alien.image_url.replace("1_", str(scene) + "_")
    alien.image = pygame.image.load(alien.image_url)
    alien.x = alien_width + 1 * alien_width * alien_number
    alien.rect.x = random.randrange(0, game_setting.screen_width - alien_width)
    alien.rect.y = random.randrange(0, game_setting.screen_height - 2 * alien_height)

    aliens.add(alien)


def dead_gameover(stats, ship, game_setting):
    ship.live_volume = 0
    stats.game_active = False
    ship.dead = True





def update_test(ship, boss, aliens):
    if ship.kill_number == 3:
        aliens.add(boss)
        boss.blitAlien()
