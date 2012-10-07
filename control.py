
import pygame
import menu, ui
import sys

class Controller(object):
    def __init__(self, screen_size):
        self.player = None

        #TODO: load this from config
        self.config = {"TURN_LEFT" : pygame.K_RIGHT, "TURN_RIGHT" : pygame.K_LEFT}

        self.menu = menu.Menu(screen_size)
        self.ingame = True

        #mapscreen is the layer for all the non-UI elements
        self.mapscreen = pygame.Surface(screen_size)
        self.maprect = self.mapscreen.get_rect()
        self.mapscreen.fill(pygame.Color("black"))

        self.gameui = ui.GameUI(screen_size)

        self.quit = False

    def quit_game(self):
        self.quit = True

    def draw(self):
        """Draw the whole game screen."""
        #wipe all screens with black
        self.mapscreen.fill((0, 0, 0))

        if self.ingame:
            #draw ui on top of the map if in game
            self.gameui.draw(self.mapscreen)
            return self.mapscreen, self.maprect
        else:
            #TODO: add filter on top of map to darken map when in menu
            #draw the menu on top of the map if NOT in game
            self.menu.draw(self.mapscreen)
            return self.mapscreen, self.maprect

    def toggle_menu(self):
        self.ingame = not self.ingame
        if self.ingame:
            self.menu.show()
        else:
            self.menu.hide()

    def _process_ingame(self, event):
        """Process all IN GAME key and mouse events here"""
        if event.type == pygame.KEYDOWN:
            #no keydown events yet
            pass

        elif event.type == pygame.KEYUP:
            if event.key == self.config["TURN_RIGHT"]:
                self.player.worm.turn_right()

            elif event.key == self.config["TURN_LEFT"]:
                self.player.worm.turn_left()

            elif event.key == pygame.K_ESCAPE:
                self.toggle_menu()

    def _process_menu(self, event):
        """Process all MENU key and mouse events here"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #scroll up in menu
                pass
            elif event.key == pygame.K_DOWN:
                #scroll down in menu
                pass
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.toggle_menu()
            elif event.key == pygame.K_q:
                self.quit_game()

    def process(self, event):
        if self.ingame:
            self._process_ingame(event)
        else:
            self._process_menu(event)