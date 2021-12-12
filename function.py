# -*- coding: utf-8 -*-
import pygame
import sys
from Button import Begin, Back, Help, About, Parkour, Fight
from Player import Player, Tp
from Monster import Monsters

tp_fx = pygame.mixer.Sound("sound/tpsound.mp3")
tp_fx.set_volume(0.5)

# menu scene
def menu(screen):
    # begin, end, and help option in menu
    begin = Begin()
    help = Help()
    about = About()

    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if user click one of option, it will direct the user to the corresponding scene
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if begin.check_button():
                    return 11
                if help.check_button():
                    return 1
                if about.check_button():
                    return 7
                # if end.check_button():
                #     pygame.quit()
                #     sys.exit()
        # draw the menu
        maininterface = pygame.image.load('./images/bg0.png')
        maininterface = pygame.transform.scale(maininterface, (1200, 800))
        screen.blit(maininterface, (0, 0))
        pygame.display.update()


def game1(screen, scene):
    # init player, back option and monsters
    player = Player(screen)
    player.level = scene - 1
    tp = Tp()
    back = Back()
    bg_1 = pygame.image.load('images/bg1.png').convert()
    bg_1 = pygame.transform.scale(bg_1, (1200, 800))
    speed = 0.1
    blood = pygame.image.load('./images/life.png')
    monsters = Monsters(screen, pygame.image.load('./images/blood_bag.png'), player, speed, 2)
    monsters.create()

    while True:

        # Handle event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # when monsters are all killed, press f to go to next map
            #            elif event.type == pygame.KEYDOWN and len(monsters.monsters)==0:
            #                if event.key == pygame.K_f:
            #                    return 2
            elif event.type == pygame.KEYDOWN and not player.checkDead():
                player.check_keydown_events(event, monsters)
            elif event.type == pygame.KEYUP and not player.checkDead():
                player.check_keyup_events(event)

        screen.blit(bg_1, (0, 0))
        screen.blit(tp.image, (tp.x, tp.y))
        if nextlevel(player, tp):
            tp_fx.play()
            return 3
        if player.checkDead():
            return 6
        #        if player.checkSuccess():
        #            return 3
        life = pygame.transform.scale(blood, (blood.get_rect()[2] * player.life, blood.get_rect()[3]))
        screen.blit(life, (10, 10))
        # # screen.blit(back.image,(back.x,back.y))
        player.life -= 0.001
        player.show()
        monsters.update(screen)
        pygame.display.update()


def game2(screen, scene):
    player = Player(screen)
    player.level = scene - 1
    tp = Tp()
    speed = 0.1
    blood = pygame.image.load('./images/life.png')
    monsters = Monsters(screen, pygame.image.load('./images/blood_bag.png'), player, speed, 2)
    monsters.create()
    bg_2 = pygame.image.load('images/bg2.png').convert()
    bg_2 = pygame.transform.scale(bg_2, (1200, 800))
    while True:

        # Handle event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # when monsters are all killed, press f to go to next map
            elif event.type == pygame.KEYDOWN and not player.checkDead():
                player.check_keydown_events(event, monsters)
            elif event.type == pygame.KEYUP and not player.checkDead():
                player.check_keyup_events(event)
        screen.blit(bg_2, (0, 0))
        screen.blit(tp.image, (tp.x, tp.y))
        if player.checkDead():
            return 6
        if nextlevel(player, tp):
            tp_fx.play()
            return 4
        life = pygame.transform.scale(blood, (blood.get_rect()[2] * player.life, blood.get_rect()[3]))
        screen.blit(life, (10, 10))
        player.life -= 0.004
        player.show()
        monsters.update(screen)
        pygame.display.update()


def game3(screen, scene):
    player = Player(screen)
    player.level = scene - 1
    tp = Tp()
    speed = 0.1
    blood = pygame.image.load('./images/life.png')
    monsters = Monsters(screen, pygame.image.load('./images/blood_bag.png'), player, speed, 2)
    monsters.create()
    bg_3 = pygame.image.load('images/bg3.png').convert()
    bg_3 = pygame.transform.scale(bg_3, (1200, 800))
    while True:

        # Handle event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # when monsters are all killed, press f to go to next map
            #            elif event.type == pygame.KEYDOWN and len(monsters.monsters) == 0:
            #                if event.key == pygame.K_f:
            #                    return 4
            elif event.type == pygame.KEYDOWN and not player.checkDead():
                player.check_keydown_events(event, monsters)
            elif event.type == pygame.KEYUP and not player.checkDead():
                player.check_keyup_events(event)

        # screen.blit(pygame.image.load('./back2.png'), (0, 0))
        screen.blit(bg_3, (0, 0))
        screen.blit(tp.image, (tp.x, tp.y))
        if player.checkDead():
            return 6
        if nextlevel(player, tp):
            return 5
        # if player.checkSuccess():
        #     return 5
        life = pygame.transform.scale(blood, (blood.get_rect()[2] * player.life, blood.get_rect()[3]))
        screen.blit(life, (10, 10))
        # screen.blit(back.image, (back.x, back.y))
        player.life -= 0.004
        player.show()
        monsters.update(screen)
        pygame.display.update()

# todo 时间问题
def nextlevel(A, B):
    listx, listy = A.checkxy()
    listx1, listy1 = B.checkxy()

    def cross(a, b):
        for each in a:
            if each in b:
                return True
        return False

    if cross(listx, listx1) and cross(listy, listy1):
        return True
    else:
        return False


def success(screen):
    back = Back()

    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back.check_button():
                    return 0
        success = pygame.image.load('./images/success.png')
        success = pygame.transform.scale(success, (1200, 800))
        screen.blit(success, (0, 0))
        pygame.display.update()


def fail(screen):
    back = Back()

    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back.check_button():
                    return 0
        fail = pygame.image.load('./images/fail.png')
        fail = pygame.transform.scale(fail, (1200, 800))
        screen.blit(fail, (0, 0))
        pygame.display.update()


def help(screen):
    back = Back()

    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back.check_button():
                    return 0
        help = pygame.image.load('./images/help.png')
        help = pygame.transform.scale(help, (1200, 800))
        screen.blit(help, (0, 0))
        # screen.blit(back.image, (back.x, back.y))
        # screen.blit(font.render('Move up: w', True, pygame.Color(37, 4, 4)), (50, 10))
        # screen.blit(font.render('Move down: s', True, pygame.Color(37, 4, 4)), (50, 40))
        # screen.blit(font.render('Move left: a', True, pygame.Color(37, 4, 4)), (50, 70))
        # screen.blit(font.render('Move right: d', True, pygame.Color(37, 4, 4)), (50, 100))
        # screen.blit(font.render('Produced by: Gang Gao, Xiang Ren, Yicheng Cai, Yuxiang Xu, Zhinan Zhu', True,
        #                         pygame.Color(37, 4, 4)), (50, 150))
        pygame.display.update()


def about(screen):
    back = Back()

    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back.check_button():
                    return 0
        about = pygame.image.load('./images/about.png')
        about = pygame.transform.scale(about, (1200, 800))
        screen.blit(about, (0, 0))
        # screen.blit(back.image, (back.x, back.y))
        pygame.display.update()


def mode(screen):
    parkour = Parkour()
    fight = Fight()

    while True:

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if user click one of option, it will direct the user to the corresponding scene
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if parkour.check_button():
                    return 2
                if fight.check_button():
                    return 8

                # if end.check_button():
                #     pygame.quit()
                #     sys.exit()
        # draw the menu
        maininterface = pygame.image.load('./images/mode.png')
        maininterface = pygame.transform.scale(maininterface, (1200, 800))
        screen.blit(maininterface, (0, 0))
        pygame.display.update()

