
import pygame

class Controller(object):
    def process(self, event):
        #process all key and mouse events here, possibly get controller instance from somewhere
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                scrollRight = True
            elif event.key == pygame.K_LEFT:
                scrollLeft = True
            elif event.key == pygame.K_UP:
                scrollUp = True
            elif event.key == pygame.K_DOWN:
                scrollDown = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                scrollRight = False
            elif event.key == pygame.K_LEFT:
                scrollLeft = False
            elif event.key == pygame.K_UP:
                scrollUp = False
            elif event.key == pygame.K_DOWN:
                scrollDown = False