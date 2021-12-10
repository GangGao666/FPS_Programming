import pygame
import sys
from Button import Begin, Back, Help, About
from Monster import Monsters
from Player import Player
import function

def main():
    # init pygame and font
    pygame.init()
    pygame.font.init()

    # set font type and size
    font = pygame.font.SysFont("Arial", 42)

    pygame.key.set_repeat(10,20)

    # there are four scene, 0 = menu, 1 = first map, 2 = second map, 3 = help
    scene = 0

    screen = pygame.display.set_mode((1200,800))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # we import function class, the function in function class will return scene
            if scene == 0:
                scene = function.menu(screen,font)
            if scene == 1:
                scene = function.help(screen,font)
            if scene == 2:
                scene = function.game1(screen,font)
            if scene == 3:
                scene = function.game2(screen,font)
            if scene == 4:
                scene = function.game3(screen,font)
            if scene == 5:
                scene = function.success(screen,font)
            if scene == 6:
                scene = function.fail(screen,font)
            if scene == 7:
                scene = function.about(screen, font)

        pygame.display.flip()

main()