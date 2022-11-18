import pygame
from pygame.sprite import Sprite


class Ball(Sprite):
    pygame.init()

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('american_football.bmp').convert_alpha()

        # Create the Ball rect
        self.rect = self.image.get_rect()
        self.rect.midright = ai_game.football.rect.midright

        # Store the ball's position as a decimal value.

        self.x = float(self.rect.x)


    def update(self):
        """Move the bullet up the screen"""
        if self.rect.right < self.screen_rect.right - 100:
            self.x += 1
            self.rect.x = self.x
        # Update the rect position


