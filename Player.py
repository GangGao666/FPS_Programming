import pygame


class Player():
    pygame.mixer.init() #Initialize mixer function
    walking_fx = pygame.mixer.Sound("sound/walking.mp3") #Introducing walking sound effects
    walking_fx.set_volume(0.5) #Adjusting the sound volume
    attack_fx = pygame.mixer.Sound("sound/attack.wav") #Imported attack sound effects
    attack_fx.set_volume(0.5) #Adjusting the sound volume


    def __init__(self,screen):
        self.screen = screen
        self.img_list = [pygame.image.load("./images/player_right.png"),pygame.image.load("./images/player_left.png")]
        self.dir = 0
        self.image = self.img_list[self.dir]
        self.life = 10
        self.speed = 5
        self.dead = False
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False
        self.x = 50
        self.y = 600
        self.imagesizex = 128
        self.imagesizey = 128
        self.img_width = 1200
        self.img_height = 800
        self.att = False
        self.rect = pygame.Rect(self.x,self.y,70,70)
        self.level = 1

    def show(self):
        self.screen.blit(self.image,(self.x,self.y))


    def move(self):
        if self.life > 0:
            if self.move_up and (self.y - self.speed >= 300):
                self.y = self.y - self.speed
            if self.move_right and (self.x + self.speed <= 1200 - self.imagesizex):
                self.dir = 0
                self.image = self.img_list[0]
                self.x = self.x + self.speed
            if self.move_left and (self.x - self.speed > -0):
                self.dir = 1
                self.image = self.img_list[1]
                self.x = self.x - self.speed
            if self.move_down and (self.y + self.speed <= 700 - self.imagesizey):
                self.y = self.y + self.speed

    def check_keydown_events(self, event,monsters):
        if event.key == pygame.K_w:
            self.move_up = True
            self.move()
            self.walking_fx.play() #Play sound effects while walking
            self.collide(monsters)
        if event.key == pygame.K_d:
            self.move_right = True
            self.move()
            self.walking_fx.play() #Play sound effects while walking
            self.collide(monsters)
        if event.key == pygame.K_a:
            self.move_left = True
            self.move()
            self.walking_fx.play() #Play sound effects while walking
            self.collide(monsters)
        if event.key == pygame.K_s:
            self.move_down = True
            self.move()
            self.walking_fx.play() #Play sound effects while walking
            self.collide(monsters)
        if event.key == pygame.K_j:
            self.att = True
            self.attack()
            self.attack_fx.play() #Play sound effects during attacks
            self.collide(monsters)


    def check_keyup_events(self,event,monsters):
        if event.key == pygame.K_j:
            self.image = self.img_list[self.dir]
            self.att = False
            self.attack_fx.stop() #End of playing sound effects

        if event.key == pygame.K_w:
            self.move_up = False
            self.walking_fx.stop()
        if event.key == pygame.K_d:
            self.move_right = False
            self.walking_fx.stop()
        if event.key == pygame.K_a:
            self.move_left = False
            self.walking_fx.stop()
        if event.key == pygame.K_s:
            self.move_down = False
            self.walking_fx.stop()
    def checkxy(self):
        x1=self.x
        x2=self.x+self.imagesizex
        y1=self.y
        y2=self.y+self.imagesizey
        return(range(x1,x2),range(y1,y2))

    def checkDead(self):
        if self.life < 0:
            self.dead = True
            return True
        else:
            return False

    def attack(self):
        if self.att:
            if self.dir == 0:
                self.image = pygame.image.load('./images/player_right_attack.png')
            else:
                self.image = pygame.image.load('./images/player_left_attack.png')

    def collide(self,monsters):
        if self.att:
            player_rect = self.image.get_rect()
            player_rect.left = self.x
            player_rect.top = self.y
            for monster in monsters.monsters:
                if len(monsters.monsters)>1:
                    if monster.type_ != 'Boss':
                        monster_rect = monster.image.get_rect()
                        monster_rect.left = monster.x
                        monster_rect.top = monster.y
                        if monster_rect.colliderect(player_rect) and not monster.checkDead():
                            monster.life -= 1
                else:
                    monster_rect = monster.image.get_rect()
                    monster_rect.left = monster.x
                    monster_rect.top = monster.y
                    if monster_rect.colliderect(player_rect) and not monster.checkDead():
                        monster.life -= 1
        else:
            player_rect = self.image.get_rect()
            player_rect.left = self.x
            player_rect.top = self.y
            player_rect[2] = 30
            player_rect[3] = 55
            for monster in monsters.monsters:
                monster_rect = monster.image.get_rect()
                monster_rect.left = monster.x+10
                monster_rect.top = monster.y+10
                monster_rect[2] = 30
                monster_rect[3] = 55
                if monster_rect.colliderect(player_rect) and not monster.checkDead():
                    self.life = -1


class Tp():
    def __init__(self):
        self.x=1085
        self.y=465
        self.image=pygame.image.load('./images/tp.png')
        self.imagesizex=60
        self.imagesizey=125
    def checkxy(self):
        x1=self.x
        x2=self.x+self.imagesizex
        y1=self.y
        y2=self.y+self.imagesizey
        return(range(x1,x2),range(y1,y2))