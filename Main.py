import pygame
import sys
import function
import port
from my_enum import Scene

def main():
    # init pygame and font
    pygame.init()
    pygame.font.init()
    # set font type and size
    font = pygame.font.SysFont("Arial", 42)

    pygame.mixer.music.load('sound/piano1.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)
    # there are four scene, 0 = menu, 1 = first map, 2 = second map, 3 = help
    #
    scene = 0

    screen = pygame.display.set_mode((1200, 800))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # we import function class, the function in function class will return scene
        if scene == Scene.MENU.value:
            scene = function.menu(screen)
        if scene == Scene.HELP.value:
            scene = function.help(screen)
        if scene == Scene.MODE1_GAME1.value:
            pygame.key.set_repeat(80,10)
            scene = function.game1(screen, scene)
        if scene == Scene.MODE1_GAME2.value:
            pygame.key.set_repeat(80,10)
            scene = function.game2(screen, scene)
        if scene == Scene.MODE1_GAME3.value:
            pygame.key.set_repeat(80,10)
            scene = function.game3(screen, scene)
        if scene == Scene.SUCCESS.value:
            scene = function.success(screen)
        if scene == Scene.FAIL.value:
            scene = function.fail(screen)
        if scene == Scene.ABOUT.value:
            scene = function.about(screen)
        if scene == Scene.MODE2_GAME1.value:
            scene = port.game1(scene)
        if scene == Scene.MODE2_GAME2.value:
            scene = port.game2(scene)
        if scene == Scene.MODE2_GAME3.value:
            scene = port.game3(scene)
        if scene == Scene.MODE.value:
            scene = function.mode(screen)
        pygame.display.flip()
main()
