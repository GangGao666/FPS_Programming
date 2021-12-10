# -*- coding: utf-8 -*-
import pygame
import sys
from Button import Begin, Back, Help, About
from Player import Player
from Monster import Monsters

# menu scene
def menu(screen,font):

    # begin, end, and help option in menu
    begin = Begin(font)
    help = Help(font)
    about = About(font)

    while True:

        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if user click one of option, it will direct the user to the corresponding scene
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if begin.check_button():
                    return 2
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
        # screen.fill((255,255,255))
        # screen.blit(begin.image,(begin.x,begin.y))
        # screen.blit(end.image, (end.x, end.y))
        # screen.blit(helpp.image,(helpp.x,helpp.y))

        pygame.display.update()


def game1(screen,font):
    # init player, back option and monsters
    player = Player(screen)
    back = Back(font)
    bg_1 = pygame.image.load('images/bg1.png').convert()

    speed = 0.1
    blood = pygame.image.load('./life.jpeg')
    monsters = Monsters(screen,pygame.image.load('./life.jpeg'),player,speed,2)
    monsters.create()

    while True:

        # Handle event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            # when monsters are all killed, press f to go to next map
            elif event.type == pygame.KEYDOWN and len(monsters.monsters)==0:
                if event.key == pygame.K_f:
                    return 2
            elif event.type == pygame.KEYDOWN and not player.checkDead():
                player.check_keydown_events(event,monsters)
            elif event.type == pygame.KEYUP and not player.checkDead():
                player.check_keyup_events(event)


        #screen.blit(pygame.image.load('./back.png'),(0,0))
        screen.blit(bg_1, (0, 0))
        screen.blit(pygame.image.load('./tp.png'), (500, 200))
        # todo 需添加失败或通关画面
        if player.checkDead():
            return 0
        if player.checkSuccess():
            return 3
        life = pygame.transform.scale(blood, (blood.get_rect()[2]*player.life,blood.get_rect()[3]))
        screen.blit(life,(10,10))
        # # screen.blit(back.image,(back.x,back.y))
        player.life -= 0.001

        player.show()
        monsters.update(screen)


        pygame.display.update()


def game2(screen,font):
    player = Player(screen)
    back = Back(font)
    speed = 0.1
    blood = pygame.image.load('./life.jpeg')
    monsters = Monsters(screen, pygame.image.load('./life.jpeg'), player, speed,2)
    monsters.create()
    bg_2 = pygame.image.load('images/bg2.png').convert()

    while True:

        # Handle event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            # when monsters are all killed, press f to go to next map
            elif event.type == pygame.KEYDOWN and not player.checkDead():
                player.check_keydown_events(event, monsters)
            elif event.type == pygame.KEYUP and not player.checkDead():
                player.check_keyup_events(event)


        #screen.blit(pygame.image.load('./back2.png'), (0, 0))
        screen.blit(bg_2, (0, 0))
        screen.blit(pygame.image.load('./tp.png'),(500,200))
        if player.checkDead():
            return 0
        if player.checkSuccess():
            return 4

        life = pygame.transform.scale(blood, (blood.get_rect()[2] * player.life, blood.get_rect()[3]))
        screen.blit(life, (10, 10))
        screen.blit(back.image, (back.x, back.y))
        player.life -= 0.004
        player.show()
        monsters.update(screen)

        pygame.display.update()

def game3(screen,font):
    player = Player(screen)
    back = Back(font)
    speed = 0.1
    blood = pygame.image.load('./life.jpeg')
    monsters = Monsters(screen, pygame.image.load('./life.jpeg'), player, speed,2)
    monsters.create()
    bg_3 = pygame.image.load('images/bg3.png').convert()

    while True:

        # Handle event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            # when monsters are all killed, press f to go to next map
            elif event.type == pygame.KEYDOWN and len(monsters.monsters) == 0:
                if event.key == pygame.K_f:
                    return 4
            elif event.type == pygame.KEYDOWN and not player.checkDead():
                player.check_keydown_events(event, monsters)
            elif event.type == pygame.KEYUP and not player.checkDead():
                player.check_keyup_events(event)


        #screen.blit(pygame.image.load('./back2.png'), (0, 0))
        screen.blit(bg_3, (0, 0))
        screen.blit(pygame.image.load('./tp.png'), (500, 200))
        if player.checkDead():
            return 0
        if player.checkSuccess():
            return 0

        life = pygame.transform.scale(blood, (blood.get_rect()[2] * player.life, blood.get_rect()[3]))
        screen.blit(life, (10, 10))
        screen.blit(back.image, (back.x, back.y))
        player.life -= 0.004
        player.show()
        monsters.update(screen)

        pygame.display.update()

def success(screen,font):
    back = Back(font)

    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        screen.fill((255, 255, 255))
        # # screen.blit(back.image,(back.x,back.y))
        screen.blit(font.render('Congratulation!', True, pygame.Color(37, 4, 4)), (250,120))
        pygame.display.update()

def fail(screen,font):
    back = Back(font)

    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        screen.fill((255, 255, 255))
        # screen.blit(back.image,(back.x,back.y))
        screen.blit(font.render('Sorry, you failed!', True, pygame.Color(37, 4, 4)), (250,120))
        pygame.display.update()

def help(screen, font):
    back = Back(font)

    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        screen.fill((255, 255, 255))
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

def about(screen, font):
    back = Back(font)

    while True:
        # Handle events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()


        screen.fill((255, 255, 255))
        about = pygame.image.load('./images/about.png')
        about = pygame.transform.scale(about, (1200, 800))
        screen.blit(about, (0, 0))
        # screen.blit(back.image, (back.x, back.y))
        pygame.display.update()

            
        
            