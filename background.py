import pygame

class Background:
    pygame.init()

    def __init__(self, ai_game):
        self.image = pygame.image.load('bg_image.png').convert_alpha()
        self.settings = ai_game.settings
        self.screen = ai_game.screen

    def draw_bg(self):
        scaled_bg = pygame.transform.scale(self.image, (self.settings.screen_width, self.settings.screen_height))
        self.screen.blit(scaled_bg, (0, 0))