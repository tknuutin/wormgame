import pygame
import sys
import inputs

print "hello wormgame"
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768

def main():
    start()

def start():
    pygame.init()

    #screen is the lowermost layer of the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    #mapscreen is the layer for all the non-UI elements
    mapscreen = pygame.Surface(SCREEN_SIZE)
    maprect = mapscreen.get_rect()

    mapscreen.fill(pygame.Color("black"))

    while True:

        #copy mapscreen contents to main screen
        screen.blit(mapscreen, maprect)
        pygame.display.flip()

        #if we get an exit command, quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            inputs.process(event)

        #limit fps
        clock.tick(30)

if __name__ == "__main__":
    main()

