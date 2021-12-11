import pygame
import sys
import function
import port


def main():
    # init pygame and font
    pygame.init()
    pygame.font.init()

    # clock = pygame.time.Clock()
    # fps = 60

    # set font type and size
    font = pygame.font.SysFont("Arial", 42)

    # pygame.key.set_repeat(10, 20)

    pygame.mixer.music.load('sound/piano1.mp3')  # 加载背景音乐
    pygame.mixer.music.set_volume(0.5)  # 设置音量
    pygame.mixer.music.play(-1, 0.0)
    # there are four scene, 0 = menu, 1 = first map, 2 = second map, 3 = help
    scene = 0

    screen = pygame.display.set_mode((1200, 800))

    while True:
        # clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # we import function class, the function in function class will return scene
            if scene == 0:
                scene = function.menu(screen, font)
            if scene == 1:
                scene = function.help(screen, font)
            if scene == 2:
                pygame.key.set_repeat(10, 20)
                scene = function.game1(screen, font, scene)
            if scene == 3:
                pygame.key.set_repeat(10, 20)
                scene = function.game2(screen, font, scene)
            if scene == 4:
                pygame.key.set_repeat(10, 20)
                scene = function.game3(screen, font, scene)
            if scene == 5:
                scene = function.success(screen, font)
            if scene == 6:
                scene = function.fail(screen, font)
            if scene == 7:
                scene = function.about(screen, font)
            if scene == 8:
                scene = scene - 7
                scene = port.game1(scene)
            if scene == 9:
                scene = scene - 7
                scene = port.game2(scene)
            if scene == 10:
                scene = scene - 7
                scene = port.game3(scene)
            if scene == 11:
                scene = function.mode(screen,font)


        pygame.display.flip()


main()
