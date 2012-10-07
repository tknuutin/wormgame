
import pygame

class GameText(object):
    def __init__(self, x, y, x_size, y_size, font_size=20, font_family=None, text="-", color=(255, 255, 255)):
        self.font = pygame.font.Font(font_family, 20)
        self.rect = pygame.Rect(x, y, x_size, y_size)
        self.text = text
        self.color = color

    def draw(self, screen):
        draw_text = self.font.render(self.text, True, self.color)
        screen.blit(draw_text, self.rect)

class GameUI(object):
    def __init__(self, screen_size):
        self.text_elements = [GameText(50, 600, 100, 25, "You are in game. Press ESC for menu.")]

        self.screen = pygame.Surface(screen_size)
        self.screen = self.screen.get_rect()

    def add_text_element(self, gametext):
        self.text_elements.append(gametext)

    def draw(self, game_screen):
        for text in self.text_elements:
            text.draw(game_screen)