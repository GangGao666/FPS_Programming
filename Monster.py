import pygame
import random


class Monsters:

    def __init__(self, screen,output,player,speed,num):
        self.monsters = []
        self.crea = False
        self.output = output
        self.player = player
        self.screen = screen
        self.speed = speed
        self.num = num
        self.soldier_position = []

    def create_num(self):
        for i in range(self.num):
            for j in range(self.num):
                self.soldier_position.append([random.randint(300, 600), random.randint(0, 600)])

    def create(self):
        self.create_num()
        for i in self.soldier_position:
            self.monsters.append(Soldier(i,self.speed,5,600,250,'Soldier'))
        #self.monsters.append(Boss([300,125],self.speed*1.5,10,600,250,'Boss'))
        self.crea = True

    def update(self,screen):
        if not self.crea:
            self.create()
        elif len(self.monsters) > 0:
            for monster in self.monsters:
                if monster.type_ != "Boss":
                    if not monster.checkDead():
                        monster.move()
                        self.screen.blit(monster.image.convert_alpha(), (monster.x, monster.y))
                    else:
                        self.screen.blit(self.output, (monster.x+10, monster.y+15))
                        player_rect = self.player.image.get_rect()
                        player_rect.left = self.player.x
                        player_rect.top = self.player.y
                        output_rect = self.output.get_rect()
                        output_rect.left = monster.x
                        output_rect.top = monster.y
                        if player_rect.colliderect(output_rect):
                            if self.player.life >= 10:
                                pass
                            elif self.player.life < 8:
                                self.player.life += 2
                            else:
                                self.player.life = 10
                            self.monsters.remove(monster)




class Soldier():
    def __init__(self,location, speed, life, img_width, img_height,type_):
        self.img_list = ['./right_down.png','./right_down.png']
        self.location = location
        self.x = location[0]
        self.y = location[1]
        self.speed = speed
        self.life = life
        self.img_width = img_width
        self.img_height = img_height
        self.dead = False
        self.dir = random.choice([0,1])
        self.image = pygame.image.load(self.img_list[self.dir])
        self.type_ = type_
        self.rect = pygame.Rect(self.x,self.y,70,70)

    # move left if dir = 0, move down if dir = 1, move right if dir =2, move up if dir = 3
    def move(self):
        if self.dir == 0:
            if self.x-self.speed>0:
                self.x = self.x-self.speed
            else:
                self.dir=random.choice([1,2,3])
        elif self.dir == 1:
            if self.y+self.speed+70 <250:
                self.y = self.y+self.speed
            else:
                self.dir = random.choice([0,2,3])
        elif self.dir == 2:
            if self.x+self.speed+70<600:
                self.x = self.x+self.speed
            else:
                self.dir=random.choice([0,1,3])
        else:
            if self.y - self.speed>0:
                self.y = self.y - self.speed
            else:
                self.dir=random.choice([0,1,2])

    def checkDead(self):
        if self.life <= 0:
            self.dead = True
            return True
        else:
            return False

class Boss(Soldier):
    def __init__(self,location, speed, life, img_width, img_height, type_):
        self.img_list = ['./12345.png', './12345.png', './12345.png', './12345.png']
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
        self.type_ = type_
        self.rect = pygame.Rect(self.x,self.y,self.image.get_rect()[2],self.image.get_rect()[3])






