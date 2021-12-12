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

'''Check whether each demon in the demon group touches the edge of the screen, if so, change the direction of movement'''


def check_fleet_edges(game_setting, demons):
    for demon in demons.sprites():
        if demon.check_edges():
            demon.change_direction()


'''Update and track the hero’s survival status. The hero’s health is continuously falling. 
When the hero’s health is less than or equal to 0, the hero is judged to be dead'''


def update_hero(game_setting, hero):
    hero.live_volume = hero.live_volume - 0.01
    if hero.live_volume <= 0:
        hero.live_volume = 0
        hero.dead = True


'''Detect the status of each demon: check if it touches the edge of the screen'''


def update_demons(game_setting, bullets, demons, gifts, hero):
    check_fleet_edges(game_setting, demons)
    # Update demon position
    demons.update()
    # Determine if the hero is in contact with the devil
    coll = pygame.sprite.spritecollide(hero, demons, False, pygame.sprite.collide_circle)
    # If contact
    if coll:
        # Get information about that devil
        demon = pygame.sprite.spritecollideany(hero, demons)
        # Set its stop attribute to 1
        demon.stop = 1
        # Change the image of the demon to an image of attack status
        image_url = demon.image_url
        image_url_attack = image_url.replace("/", "/attack_")
        demon.image = pygame.image.load([image_url, image_url_attack][np.random.choice([0, 1])])
        # When the hero is not invincible, the demon's single attack is effective
        if not hero.shield:
            # Hero's HP decreased
            hero.live_volume = hero.live_volume - demon.power
            # After being attacked, set the hero to an invincible state for a period of time
            hero.shield = True
            # Set the hero's invincibility time
            hero.shield_time = game_setting.hero_shield_time
    else:
        # If the hero is not in contact with the devil, set the devil’s stop attribute to 0,
        # the devil will return to its normal state, and the devil’s appearance will be changed
        for demon in demons.sprites():
            demon.stop = 0
            demon.image = pygame.image.load(demon.image_url)


'''更新掉落道具的状态'''


def update_gifts(game_setting, gifts, hero, gift_sound):
    # If the hero get the item successfully
    coll = pygame.sprite.spritecollideany(hero, gifts)
    if coll:
        # The hero's HP is restored to its original state
        hero.live_volume = game_setting.hero_live_volume
        # Play the audio of getting the items
        gift_sound.play()
        # Get the type of items
        gift_type = pygame.sprite.spritecollideany(hero, gifts).gift_type
        # If it is a category 0 items
        if gift_type == 0:
            # Hero's speed increased by 0.1
            hero.hero_speed += 0.1
        # If it is a category 1 items
        if gift_type == 1:
            # Demon speed decreased by 0.1
            game_setting.demon_speed = game_setting.demon_speed - 0.1
        # If it is a category 2 items
        if gift_type == 2:
            # 子弹速度增加
            game_setting.bullet_speed += 0.1
            # 增加子弹限制数目
            game_setting.bullet_allowed += 1
        # If it is a category 4 or 5 or 6 items
        if gift_type in [4, 5, 6]:
            # The hero is in a victorious state and enter the next level
            hero.win = True
        # Demon speed increased by 0.05
        game_setting.demon_speed = game_setting.demon_speed + 0.05
        # Remove the props picked up by the hero from the screen
        coll.remove(gifts)


'''Update bullet status: update the position of the bullet, 
    detect whether the bullet hits, and handle the bullet after the hit'''


def update_bullets(game_setting, screen, hero, bullets, demons, gifts, collision_sound, scene):
    # After the bullet is installed,
    # directly call the update() method of the Sprite Group array object to update the bullet position
    bullets.update()
    # Delete the bullets that go beyond the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= bullet.screen_rect.top:
            bullets.remove(bullet)
        if bullet.rect.top >= bullet.screen_rect.bottom:
            bullets.remove(bullet)
        if bullet.rect.left >= bullet.screen_rect.right:
            bullets.remove(bullet)
        if bullet.rect.right <= bullet.screen_rect.left:
            bullets.remove(bullet)
    # Determine whether the bullet collides with the demon,
    # and delete the corresponding bullet and demon on the screen
    coll = pygame.sprite.groupcollide(bullets, demons, True, True)
    # If there is a collision
    if coll:
        # Hero kills increased
        hero.kill_number += 1
        # Play impact audio
        collision_sound.play()
    '''
    https://stackoverflow.com/questions/66746880/how-to-access-each-items-attributes-in-a-list-returned-by-groupcollide-in-pyth
    In order to solve the problem of finding the specific demon hit by the bullet, 
    we learned this function from stackoverflow
    '''
    # Find every bullet that hits
    for bullet in coll:
        # Look for the demon who collided with the bullet
        for demon in coll[bullet]:
            # Create item
            gift = Gift(screen, game_setting)
            # Set the position of the demon hit by the bullet to the position where the item appears
            gift.rect.x = demon.rect.x
            gift.rect.y = demon.rect.y
            # If the demon colliding with the bullet is the boss
            if demon.type_ == 'boss':
                # Empty all demons in the demonic group
                demons.empty()
                # Set different drop items for demons in different levels
                gift.gift_type = scene + len(game_setting.gift_image)
                # Set up different appearances for the demons in different levels
                gift.image = pygame.image.load(game_setting.gift_boss_image[scene - 1])
            # Add the created props to the items group
            gifts.add(gift)
    # When only the boss and hero are left in the game
    if len(demons) == 1:
        # Create a new fleet of demons
        create_fleet(game_setting, screen, demons, scene)

# todo citation book website
'''创建子弹，将子弹加入Sprites的Group数组中'''


def fire_bullet(game_setting, screen, hero, bullets):
    # When the current bullet on the screen is less than the bullet limit
    if len(bullets) < game_setting.bullet_allowed:
        # Create bullet
        new_bullet = Bullet(game_setting, screen, hero)
        # Set the hero movement direction to the bullet movement direction
        new_bullet.direction = hero.direction
        # Set the hero as the host of the bullet
        new_bullet.host = 'hero'
        # Add the bullet created and added to the bullet list
        bullets.add(new_bullet)


'''Detect keydown of keyboard events'''


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


'''Check mouse and keyboard events'''


def check_events(game_setting, screen, hero, bullets, demons, gifts, shot_sound, bg, scene):
    # Draw a background image
    screen.blit(bg, (0, 0))
    # Monitor click, keyboard and other events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_setting, screen, hero, bullets, shot_sound, demons)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hero)


'''Update bullets, dropped items, hero positions on the screen'''


def update_screen(game_setting, screen, hero, bullets, demons, gifts):
    bullets.update()
    gifts.update()
    hero.update()
    demons.update()


'''Detect keyup of keyboard events'''


def check_keyup_events(event, hero):
    if event.key == pygame.K_d:
        hero.moving_right = False
    if event.key == pygame.K_a:
        hero.moving_left = False
    if event.key == pygame.K_w:
        hero.moving_up = False
    if event.key == pygame.K_s:
        hero.moving_down = False


'''Create a fleet of demons'''


def create_fleet(game_setting, screen, demons, scene):
    for demon_number in range(game_setting.demon_number):
        create_demon(game_setting, screen, demons, demon_number, scene)


'''Create a single demon'''


def create_demon(game_setting, screen, demons, demon_number, scene):
    # Create a demon object
    demon = Demon(screen, game_setting)
    # Set demon size
    demon_width = demon.rect.width
    demon_height = demon.rect.height
    # Show different appearances according to the moving direction of the devil
    demon.image_url = game_setting.demon_image[demon.dir]
    # Set up different appearances for different levels of demons
    demon.image_url = demon.image_url.replace("1_", str(scene) + "_")
    demon.image = pygame.image.load(demon.image_url)
    # Set different initial positions for different demons
    demon.x = demon_width + 1 * demon_width * demon_number
    demon.rect.x = random.randrange(0, game_setting.screen_width - demon_width)
    demon.rect.y = random.randrange(0, game_setting.screen_height - 2 * demon_height)
    # Add the created demon to the demon group
    demons.add(demon)


'''Detect the boss status, 
when the hero kills a certain number of enemies, the boss appears'''


def update_boss(hero, boss, demons):
    # After killing a certain number of demons, the boss appears
    if hero.kill_number == 3:
        # Add the previously created boss to the demon group
        demons.add(boss)
        # Draw the boss to the screen
        boss.update()
