
import pygame

class Menu(object):
    def __init__(self, screen_size):
        self.title_font = pygame.font.Font(None, 32)
        self.title_rect = pygame.Rect(300, 50, 100, 25)

        self.screen = pygame.Surface(screen_size)
        self.screen = self.screen.get_rect()
        self.visible = False

    def draw(self, game_screen):
        title_text = self.title_font.render("Game paused. Press Q to quit.", False, (255, 255, 255))
        game_screen.blit(title_text, self.title_rect)

    def show(self):
        self.visible = True
    def hide(self):
        self.visible = False