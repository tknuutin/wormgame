
import pygame

class GameUI(object):
    def __init__(self, screen_size):
        self.notify_font = pygame.font.Font(None, 20)
        self.notify_rect = pygame.Rect(50, 600, 100, 25)

        self.screen = pygame.Surface(screen_size)
        self.screen = self.screen.get_rect()

    def draw(self, game_screen):
        notify_text = self.notify_font.render("You are in game. Press ESC for menu.", True, (255, 255, 255))
        game_screen.blit(notify_text, self.notify_rect)