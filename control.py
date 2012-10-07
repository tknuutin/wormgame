
import pygame

class Controller(object):
    def __init__(self):
        self.player = None
        self.config = {"TURN_LEFT" : pygame.K_RIGHT, "TURN_RIGHT" : pygame.K_LEFT}

    def _process_ingame(self, event):
        #process all key and mouse events here, possibly get controller instance from somewhere
        if event.type == pygame.KEYDOWN:
            #no keydown events yet
            pass

        elif event.type == pygame.KEYUP:
            if event.key == self.config["TURN_RIGHT"]:
                self.player.worm.turn_right()

            elif event.key == self.config["TURN_LEFT"]:
                self.player.worm.turn_left()

            elif event.key == pygame.ESCAPE:
                self.show_menu()

    def _process_menu(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #scroll up in menu
                pass
            elif event.key == pygame.K_DOWN:
                #scroll down in menu
                pass

    def process(self, event):
        if self.ingame:
            self._process_ingame(event)
        else:
            self._process_menu(event)