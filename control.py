import pygame
import menu, ui, server, serverlogic, hexgrid
import sys

class View(object):
    def __init__(self, screen_size):
        self.menu = menu.Menu(screen_size)
        self.ingame = True

        #mapscreen is the layer for all the non-UI elements
        self.mapscreen = pygame.Surface(screen_size)
        self.maprect = self.mapscreen.get_rect()
        self.mapscreen.fill(pygame.Color("black"))

        self.gameui = ui.GameUI(screen_size)
        self.hexgrid = hexgrid.GridDrawer(screen_size)

    def draw_worms(self, game):
        for player in game.players:
            player.worm.update_draw_rects()
            pygame.draw.ellipse(self.mapscreen, (255, 0, 0), player.worm.rect)

    def draw(self, game):
        """Draw the whole game screen."""
        #wipe all screens with black
        self.mapscreen.fill(pygame.Color("black"))
        self.draw_worms(game)

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

class Controller(object):
    def __init__(self, screen_size, is_server=True):
        self.game = serverlogic.Game()

        #TODO: load this from config
        self.config = {"TURN_LEFT" : pygame.K_RIGHT, "TURN_RIGHT" : pygame.K_LEFT}
        self.view = View(screen_size)

        self.quit = False

        self.game.start()

    def tick(self):
        """Calculate next tick of the game"""
        pass

    def add_player(self):
        pass

    def draw(self):
        return self.view.draw(self.game)

    def quit_game(self):
        self.quit = True

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
                self.view.toggle_menu()

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
                self.view.toggle_menu()
            elif event.key == pygame.K_q:
                self.quit_game()

    def process(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif self.view.ingame:
            self._process_ingame(event)
        else:
            self._process_menu(event)