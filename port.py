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
    bg = pygame.image.load('./images/bg' + str(scene) + '.png').convert()
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


'''Fight模式第一关游戏入口'''


def game1(scene):
    game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss,bg,scene = pre_prepare(
        scene)
    while True:
        game_body(game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss, bg,
                  scene)
        # 如果英雄死亡，跳转到失败页面
        if hero.dead:
            return Scene.FAIL.value
        # 如果英雄胜利，进入下一关
        if hero.win:
            return Scene.MODE2_GAME2.value
        pygame.display.flip()


'''Fight模式第二关游戏入口'''


def game2(scene):
    game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss,bg,scene = pre_prepare(
        scene)
    while True:
        game_body(game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss, bg,
                  scene)
        # 如果英雄死亡，跳转到失败页面
        if hero.dead:
            return Scene.FAIL.value
        # 如果英雄胜利，进入下一关
        if hero.win:
            return Scene.MODE2_GAME3.value
        pygame.display.flip()


'''Fight模式第三关游戏入口'''


def game3(scene):
    game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss,bg,scene = pre_prepare(
        scene)
    while True:
        game_body(game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss, bg,
                  scene)
        # 如果英雄死亡，跳转到失败页面
        if hero.dead:
            return Scene.FAIL.value
        # 如果英雄胜利，跳转到成功页面
        if hero.win:
            return Scene.SUCCESS.value
        pygame.display.flip()


def game_body(game_setting, gift_sound, shot_sound, collision_sound, screen, hero, bullets, demons, gifts, boss, bg,
              scene):
    # 当英雄处于无敌状态
    if hero.shield:
        # todo setting
        # 英雄无敌时间减少
        hero.shield_time = hero.shield_time - 0.5
        # 当无敌时间小于等于0时
        if hero.shield_time <= 0:
            # 无敌状态关闭
            hero.shield = False
    # 检查鼠标、键盘事件
    gf.check_events(game_setting, screen, hero, bullets, demons, gifts, shot_sound, bg, scene)
    # 英雄移动
    hero.move()
    # 更新子弹状态
    gf.update_bullets(game_setting, screen, hero, bullets, demons, gifts, collision_sound, scene)
    # 检测每个恶魔的状态
    gf.update_demons(game_setting, bullets, demons, gifts, hero)
    # 更新掉落道具的状态
    gf.update_gifts(game_setting, gifts, hero, gift_sound)
    # 更新并追踪英雄生存状态
    gf.update_hero(game_setting, hero)
    # 检测boss状态
    gf.update_boss(hero, boss, demons)
    # 加载英雄剩余血量图片
    life_rect = pygame.image.load("images/life.png")
    # 动态展示英雄剩余血量
    life_ = pygame.transform.scale(life_rect, (
        life_rect.get_rect()[2] * abs(hero.live_volume), life_rect.get_rect()[3]))
    screen.blit(life_, (10, 10))
    # 更新屏幕内子弹、掉落的道具、英雄位置
    gf.update_screen(game_setting, screen, hero, bullets, demons, gifts)