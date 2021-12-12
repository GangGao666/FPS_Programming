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

'''检查恶魔群中的每个恶魔是否触及到屏幕边缘，如果是则改变运动方向'''


def check_fleet_edges(game_setting, demons):
    for demon in demons.sprites():
        if demon.check_edges():
            demon.change_direction()


'''更新并追踪英雄生存状态，英雄的生命值在不断自动下降，当英雄的生命值小于等于0时，判定英雄死亡'''


def update_hero(game_setting, hero):
    hero.live_volume = hero.live_volume - 0.01
    if hero.live_volume <= 0:
        hero.live_volume = 0
        hero.dead = True


'''检测每个恶魔的状态：检查是否触及屏幕边缘'''


def update_demons(game_setting, bullets, demons, gifts, hero):
    check_fleet_edges(game_setting, demons)
    # 更新恶魔位置
    demons.update()
    # 判断是否英雄是否与恶魔接触
    coll = pygame.sprite.spritecollide(hero, demons, False, pygame.sprite.collide_circle)
    # 如果接触
    if coll:
        # 获取那个恶魔的信息，
        demon = pygame.sprite.spritecollideany(hero, demons)
        # 将其stop属性设置为1
        demon.stop = 1
        # 将恶魔的图像更改为攻击图像
        image_url = demon.image_url
        image_url_attack = image_url.replace("/", "/attack_")
        demon.image = pygame.image.load([image_url, image_url_attack][np.random.choice([0, 1])])
        # 当英雄不处于无敌状态时，恶魔单次攻击有效
        if not hero.shield:
            # 英雄血量降低
            hero.live_volume = hero.live_volume - demon.power
            # 收到攻击后，将英雄设置一段时间的无敌状态
            hero.shield = True
            # 设置英雄的无敌时间
            hero.shield_time = game_setting.hero_shield_time
    else:
        # 如果英雄没有与恶魔接触，将恶魔stop属性设置为0，恶魔恢复正常状态，并改变恶魔外表
        for demon in demons.sprites():
            demon.stop = 0
            demon.image = pygame.image.load(demon.image_url)


'''更新掉落道具的状态'''


def update_gifts(game_setting, gifts, hero, gift_sound):
    # 如果英雄拾取道具成功
    coll = pygame.sprite.spritecollideany(hero, gifts)
    if coll:
        # 英雄生命值恢复初始状态
        hero.live_volume = game_setting.hero_live_volume
        # 播放获取道具的音频
        gift_sound.play()
        # 获取道具的类型
        gift_type = pygame.sprite.spritecollideany(hero, gifts).gift_type
        # 如果是0类道具
        if gift_type == 0:
            # 英雄速度增加0.1
            hero.hero_speed += 0.1
        # 如果是1类道具
        if gift_type == 1:
            # 恶魔速度减少0.1
            game_setting.demon_speed = game_setting.demon_speed - 0.1
        # 如果是2类道具
        if gift_type == 2:
            # 子弹速度增加
            game_setting.bullet_speed += 0.1
            # 增加子弹限制数目
            game_setting.bullet_allowed += 1
        # 如果是4/5/6类道具
        if gift_type in [4, 5, 6]:
            # 英雄处于胜利状态，进入下一关
            hero.win = True
        # 加快恶魔移动速度
        game_setting.demon_speed = game_setting.demon_speed + 0.05
        # 将英雄拾取的道具从屏幕中移除
        coll.remove(gifts)


'''更新子弹状态：更新子弹所处位置、检测子弹是否撞击，以及撞击后的对子弹的处理'''


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
    # 判断子弹是否与恶魔碰撞，并将屏幕上对应的子弹和恶魔删除
    coll = pygame.sprite.groupcollide(bullets, demons, True, True)
    # 如果碰撞
    if coll:
        # 英雄的击杀数量增加
        hero.kill_number += 1
        # 播放撞击音频
        collision_sound.play()
    '''
    https://stackoverflow.com/questions/66746880/how-to-access-each-items-attributes-in-a-list-returned-by-groupcollide-in-pyth
    为了解决找到子弹击中的具体恶魔，借鉴了stackoverflow
    '''
    # 找到发生撞击的每一个子弹
    for bullet in coll:
        # 寻找与其发生撞击的恶魔
        for demon in coll[bullet]:
            # 创建道具
            gift = Gift(screen, game_setting)
            # 将被子弹撞击的恶魔的位置设置为道具出现位置
            gift.rect.x = demon.rect.x
            gift.rect.y = demon.rect.y
            # 如果与子弹碰撞的恶魔是boss
            if demon.type_ == 'boss':
                # 清空恶魔群组中的所有恶魔
                demons.empty()
                # 为不同关卡的恶魔设置不同的掉落道具
                gift.gift_type = scene + len(game_setting.gift_image)
                # 为不同关卡的恶魔设置不同的外表
                gift.image = pygame.image.load(game_setting.gift_boss_image[scene - 1])
            # 将创建好的道具添加到道具群组里
            gifts.add(gift)
    # 当只剩boss时
    if len(demons) == 1:
        # 创建新的恶魔群
        create_fleet(game_setting, screen, demons, scene)

# todo citation book website
'''创建子弹，将子弹加入Sprites的Group数组中'''


def fire_bullet(game_setting, screen, hero, bullets):
    # 当目前屏幕内的子弹小于子弹限制数量时
    if len(bullets) < game_setting.bullet_allowed:
        # 创建子弹
        new_bullet = Bullet(game_setting, screen, hero)
        # 将英雄移动方向设置为子弹移动方向
        new_bullet.direction = hero.direction
        # 将英雄设置为子弹的host
        new_bullet.host = 'hero'
        # 将创建和的子弹添加到子弹列表中
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
    # 绘制背景图片
    screen.blit(bg, (0, 0))
    # 监听点击、键盘等事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_setting, screen, hero, bullets, shot_sound, demons)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hero)


'''更新屏幕内子弹、掉落的道具、英雄位置'''


def update_screen(game_setting, screen, hero, bullets, demons, gifts):
    bullets.update()
    gifts.update()
    hero.update()
    demons.update()


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


'''创建恶魔群'''


def create_fleet(game_setting, screen, demons, scene):
    for demon_number in range(game_setting.demon_number):
        create_demon(game_setting, screen, demons, demon_number, scene)


'''创建单个恶魔'''


def create_demon(game_setting, screen, demons, demon_number, scene):
    # 创建恶魔对象
    demon = Demon(screen, game_setting)
    # 设置恶魔尺寸
    demon_width = demon.rect.width
    demon_height = demon.rect.height
    # 根据恶魔的移动方向，展现不同的外表
    demon.image_url = game_setting.demon_image[demon.dir]
    # 为不同级别的恶魔设置不同的外表
    demon.image_url = demon.image_url.replace("1_", str(scene) + "_")
    demon.image = pygame.image.load(demon.image_url)
    # 为不同恶魔设置不同的初始位置
    demon.x = demon_width + 1 * demon_width * demon_number
    demon.rect.x = random.randrange(0, game_setting.screen_width - demon_width)
    demon.rect.y = random.randrange(0, game_setting.screen_height - 2 * demon_height)
    # 将创建好的恶魔添加到恶魔群组中
    demons.add(demon)


'''检测boss状态，当英雄的杀敌数达到一定数量时，boss出现'''


def update_boss(hero, boss, demons):
    # 击杀一定数目的恶魔后，boss出现
    if hero.kill_number == 3:
        # 将之前创建好的boss加入恶魔群组中
        demons.add(boss)
        # 将boss绘制到屏幕上
        boss.update()
