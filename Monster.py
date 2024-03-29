#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File: Monster.py
# @Description: Define monsters and soldiers

import pygame
import random

# Define Monsters. It contains a list of soldier
class Monsters:

    def __init__(self, screen, output, player, speed, num):
        self.monsters = []
        self.crea = False
        self.output = output
        self.player = player
        self.screen = screen
        self.speed = speed
        self.num = num
        self.soldier_position = []

    # Create soldier position
    def create_num(self):
        for i in range(self.num):
            for j in range(self.num):
                self.soldier_position.append([random.randint(300, 1000), random.randint(400, 500)])

    # Create a list of soldier
    def create(self):
        self.create_num()
        for i in self.soldier_position:
            self.monsters.append(Soldier(i, self.speed, 5, 600, 250, self.player.level))
        self.crea = True

    # Update Monsters. For each soldier in monsters, if soldier is alive, it will move. If soldier is dead,
    # it will disappear and a blood bag will appear. If player collides with blood bag, player will get 2 points of
    # blood and blood bag will disappear.
    def update(self, screen):
        # If there is no monsters, create monsters
        if not self.crea:
            self.create()
        elif len(self.monsters) > 0:
            for monster in self.monsters:
                if not monster.checkDead():
                    monster.move()
                    screen.blit(monster.image.convert_alpha(), (monster.x, monster.y))
                else:
                    screen.blit(self.output, (monster.x + 10, monster.y + 15))
                    player_rect = self.player.image.get_rect()
                    player_rect.left = self.player.x
                    player_rect.top = self.player.y
                    output_rect = self.output.get_rect()
                    output_rect.left = monster.x
                    output_rect.top = monster.y
                    # Use rectangle of blood bag and player to determine collision
                    if player_rect.colliderect(output_rect):
                        if self.player.life >= 10:
                            pass
                        elif self.player.life < 8:
                            self.player.life += 2
                        else:
                            self.player.life = 10
                        self.monsters.remove(monster)

# Define soldier
class Soldier():
    def __init__(self, location, speed, life, img_width, img_height, level):
        self.img_list = ['images/monster'+str(level)+'_left.png', 'images/monster'+str(level)+'_right.png', 'images/monster'+str(level)+'_right.png',
                         'images/monster'+str(level)+'_left.png']
        self.location = location
        self.x = location[0]
        self.y = location[1]
        self.speed = speed
        self.life = life
        self.img_width = img_width
        self.img_height = img_height
        self.dead = False
        self.dir = random.choice([0, 1, 2, 3])
        self.image = pygame.image.load(self.img_list[self.dir])
        self.rect = pygame.Rect(self.x, self.y, 70, 70)
        self.level = level
        self.imagesizex = 128
        self.imagesizey = 128
        self.type_ = 'soldier'

    # If soldier does not exceed range, move left if dir = 0, move down if dir = 1, move right if dir =2,
    # move up if dir = 3. If its next move will exceed range, it will randomly choose a direction except the
    # original one.
    def move(self):
        if self.dir == 0:
            if self.x - self.speed > 300:
                self.x = self.x - self.speed
            else:
                self.dir = random.choice([1, 2, 3])
        elif self.dir == 1:
            if self.y + self.speed + 128 < 700:
                self.y = self.y + self.speed
            else:
                self.dir = random.choice([0, 2, 3])
        elif self.dir == 2:
            if self.x + self.speed + 128 < 1000:
                self.x = self.x + self.speed
            else:
                self.dir = random.choice([0, 1, 3])
        else:
            if self.y - self.speed > 300:
                self.y = self.y - self.speed
            else:
                self.dir = random.choice([0, 1, 2])
        self.image = pygame.image.load(self.img_list[self.dir])

    # Check if soldier is dead
    def checkDead(self):
        if self.life <= 0:
            self.dead = True
            return True
        else:
            return False