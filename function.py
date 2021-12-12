#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File: function.py
# @Description: Generate scene

import pygame
import sys
from Button import Begin, Back, Help, About, Parkour, Fight
from Player import Player, Tp
from Monster import Monsters

# Set sound
from my_enum import Scene

tp_fx = pygame.mixer.Sound("sound/tpsound.mp3")
tp_fx.set_volume(0.5)

# Menu scene
def menu(screen):
    # Define begin, help and about option in menu
    begin = Begin()
    help = Help()
    about = About()

    while True:
        # Handle events.
        for event in pygame.event.get():
            # Check quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if user click one of option, it will direct the user to the corresponding scene
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if begin.check_button():
                    return Scene.MODE.value
                if help.check_button():
                    return Scene.HELP.value
                if about.check_button():
                    return Scene.ABOUT.value

        # Draw the menu
        main_interface = pygame.image.load('./images/bg0.png')
        # transform the picture scale to match the screen
        main_interface = pygame.transform.scale(main_interface, (1200, 800))
        screen.blit(main_interface, (0, 0))
        pygame.display.update()

# Game1 scene
def game1(screen, scene):

    # Initiate player, tp, background, speed of monster, blood and monsters
    player = Player(screen)
    player.level = scene - 1
    tp = Tp()
    bg_1 = pygame.image.load('images/bg1.png').convert()
    # transform the picture scale to match the screen
    bg_1 = pygame.transform.scale(bg_1, (1200, 800))
    speed = 0.1
    blood = pygame.image.load('./images/life.png')
    # set an object for "Monsters"
    monsters = Monsters(screen, pygame.image.load('./images/blood_bag.png'), player, speed, 3)
    monsters.create()

    while True:

        # Handle event
        for event in pygame.event.get():
            # Check quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If key is down and player is alive, check event
            elif event.type == pygame.KEYDOWN and not player.checkDead():
                player.check_keydown_events(event, monsters)
            # If key is up and player is alive, check event
            elif event.type == pygame.KEYUP and not player.checkDead():
                player.check_keyup_events(event, monsters)

        # Draw the scene and tp
        screen.blit(bg_1, (0, 0))
        screen.blit(tp.image, (tp.x, tp.y))

        # If player enters tp, play the music and direct to next level
        if nextlevel(player, tp):
            tp_fx.play()
            return Scene.MODE1_GAME2.value

        # If player is dead, direct to failure scene
        if player.checkDead():
            return Scene.FAIL.value

        # Draw the life and update player, monsters and scene
        life = pygame.transform.scale(blood, (blood.get_rect()[2] * player.life, blood.get_rect()[3]))
        screen.blit(life, (10, 10))
        player.life -= 0.005
        player.show()
        monsters.update(screen)
        pygame.display.update()

# Game2 scene
def game2(screen, scene):

    # Initiate player, tp, background, speed of monster, blood and monsters
    player = Player(screen)
    player.level = scene - 1
    tp = Tp()
    speed = 0.2
    # set loaded images to a variable
    blood = pygame.image.load('./images/life.png')
    # set an object for "Monsters"
    monsters = Monsters(screen, pygame.image.load('./images/blood_bag.png'), player, speed, 3)
    monsters.create()
    bg_2 = pygame.image.load('images/bg2.png').convert()
    # transform the picture scale to match the screen
    bg_2 = pygame.transform.scale(bg_2, (1200, 800))

    while True:

        # Handle event
        for event in pygame.event.get():
            # Check quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If key is down and player is alive, check event
            elif event.type == pygame.KEYDOWN and not player.checkDead():
                player.check_keydown_events(event, monsters)
            # If key is up and player is alive, check event
            elif event.type == pygame.KEYUP and not player.checkDead():
                player.check_keyup_events(event, monsters)

        # Draw the background and tp
        screen.blit(bg_2, (0, 0))
        screen.blit(tp.image, (tp.x, tp.y))

        # If player enters tp, play the music and direct to next level
        if nextlevel(player, tp):
            tp_fx.play()
            return Scene.MODE1_GAME3.value

        # If player is dead, direct to failure scene
        if player.checkDead():
            return Scene.FAIL.value

        # Draw the life and update player, monsters and scene
        life = pygame.transform.scale(blood, (blood.get_rect()[2] * player.life, blood.get_rect()[3]))
        screen.blit(life, (10, 10))
        player.life -= 0.01
        player.show()
        monsters.update(screen)
        pygame.display.update()

# Game3 scene
def game3(screen, scene):

    # Initiate player, tp, background, speed of monster, blood and monsters
    player = Player(screen)
    player.level = scene - 1
    tp = Tp()
    speed = 0.3
    # set loaded images to a variable
    blood = pygame.image.load('./images/life.png')
    # set an object for "Monsters"
    monsters = Monsters(screen, pygame.image.load('./images/blood_bag.png'), player, speed, 3)
    monsters.create()
    bg_3 = pygame.image.load('images/bg3.png').convert()
    # transform the picture scale to match the screen
    bg_3 = pygame.transform.scale(bg_3, (1200, 800))

    while True:

        # Handle event
        for event in pygame.event.get():
            # Check quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If key is down and player is alive, check event
            elif event.type == pygame.KEYDOWN and not player.checkDead():
                player.check_keydown_events(event, monsters)
            # If key is up and player is alive, check event
            elif event.type == pygame.KEYUP and not player.checkDead():
                player.check_keyup_events(event, monsters)

        # Draw the background and tp
        screen.blit(bg_3, (0, 0))
        screen.blit(tp.image, (tp.x, tp.y))

        # If player enters tp, play the music and direct to next level
        if nextlevel(player, tp):
            return Scene.SUCCESS.value

        # If player is dead, direct to failure scene
        if player.checkDead():
            return Scene.FAIL.value

        # Draw the life and update player, monsters and scene
        life = pygame.transform.scale(blood, (blood.get_rect()[2] * player.life, blood.get_rect()[3]))
        screen.blit(life, (10, 10))
        player.life -= 0.013
        player.show()
        monsters.update(screen)
        pygame.display.update()

# Define if player can go to next level. If player collide with tp, it will go to next level
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

# Success scene
def success(screen):

    # Initiate back option
    back = Back()

    while True:
        # Handle events.
        for event in pygame.event.get():
            # Check quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If user clicks back button, return to menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back.check_button():
                    return Scene.MENU.value

        # Draw success scene
        success = pygame.image.load('./images/success.png')
        # transform the picture scale to match the screen
        success = pygame.transform.scale(success, (1200, 800))
        # draw picture
        screen.blit(success, (0, 0))
        # screen updates
        pygame.display.update()

# Fail scene
def fail(screen):

    # Initiate back option
    back = Back()

    while True:
        # Handle events.
        for event in pygame.event.get():
            # Check quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If user clicks back button, return to menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back.check_button():
                    return Scene.MENU.value

        # Draw fail scene
        fail = pygame.image.load('./images/fail.png')
        # transform the picture scale to match the screen
        fail = pygame.transform.scale(fail, (1200, 800))
        screen.blit(fail, (0, 0))
        pygame.display.update()

# a function to redirect screen to "HELP" page
def help(screen):

    # Initiate back option
    back = Back()

    while True:
        # Handle events.
        for event in pygame.event.get():
            # Check quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If user clicks back button, return to menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back.check_button():
                    return Scene.MENU.value

        # Draw help scene
        help = pygame.image.load('./images/help.png')
        help = pygame.transform.scale(help, (1200, 800))
        screen.blit(help, (0, 0))
        pygame.display.update()

# a function to redirect screen to "ABOUT" page
def about(screen):

    # Initiate back option
    back = Back()

    while True:
        # Handle events.
        for event in pygame.event.get():
            # Check quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If user clicks back button, return to menu
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back.check_button():
                    return Scene.MENU.value

        # Draw about scene
        about = pygame.image.load('./images/about.png')
        about = pygame.transform.scale(about, (1200, 800))
        screen.blit(about, (0, 0))
        pygame.display.update()

# a function to redirect screen to "MODE" page
def mode(screen):

    # Initiate parkour and fight option
    parkour = Parkour()
    fight = Fight()
    back = Back()

    while True:

        # Handle events.
        for event in pygame.event.get():
            # Check quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # If user clicks one of option, it will direct the user to the corresponding scene
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if parkour.check_button():
                    # enter mode1: parkour
                    return Scene.MODE1_GAME1.value
                if fight.check_button():
                    # enter mode2: fight
                    return Scene.MODE2_GAME1.value
                if back.check_button():
                    # return to home page
                    return Scene.MENU.value

        # Draw mode scene
        main_interface = pygame.image.load('./images/mode.png')
        # transform the picture scale to match the screen
        main_interface = pygame.transform.scale(main_interface, (1200, 800))
        screen.blit(main_interface, (0, 0))
        pygame.display.update()

