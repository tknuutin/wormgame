import pygame
import sys

print "hello wormgame"

def main():
    start()

def start():
    pygame.init()
    size = width, height = 1024, 768

    #screen is the lowermost layer of the screen
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    #mapscreen is the layer for all the non-UI elements
    mapscreen = pygame.Surface((1024, 768))
    maprect = mapscreen.get_rect()

    black = 0, 0, 0
    mapscreen.fill(black)

    while True:
        #limit fps
        clock.tick(30)

        #copy mapscreen contents to main screen
        screen.blit(mapscreen, maprect)
        pygame.display.flip()

        #if we get an exit command, quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == "__main__":
    main()

