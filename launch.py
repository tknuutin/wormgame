import pygame
import sys, logging
import control

logging.basicConfig(filename='wormgame_last.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768

def main():
    start()

def start():
    pygame.init()

    logging.info("Starting Wormgame")
    #screen is the lowermost layer of the screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    ctrl = control.Controller(SCREEN_SIZE)

    start = pygame.time.get_ticks()
    while not ctrl.quit:
        ctrl.view.gameui.set_time_elapsed(pygame.time.get_ticks() - start)
        ctrl.tick()

        #copy mapscreen contents to main screen
        mapscreen, maprect = ctrl.draw()
        screen.blit(mapscreen, maprect)
        pygame.display.flip()

        #if we get an exit command, quit
        for event in pygame.event.get():
            ctrl.process(event)

        #limit fps
        clock.tick(30)

    logging.info("Quitting Wormgame")

if __name__ == "__main__":
    main()

