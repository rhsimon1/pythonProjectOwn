import pygame


class Footballplayer:
    pygame.init()

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.footballplayer_image = pygame.image.load('football_player.bmp')
        self.rect = self.footballplayer_image.get_rect()
        self.rect.x  = 174
        self.rect.y = 397

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def footballplayer_movement(self):
        if self.moving_right and self.rect.right < 1095:
            self.x += 0.3
        elif self.moving_left and self.rect.left >= 88:
            self.x -= 0.3
        elif self.moving_up and self.rect.top >= 119:
            self.y -= 0.3
        elif self.moving_down and self.rect.bottom < 680:
            self.y += 0.3

        self.rect.x = self.x
        self.rect.y = self.y

    def draw_image(self):
        self.screen.blit(self.footballplayer_image, self.rect)
