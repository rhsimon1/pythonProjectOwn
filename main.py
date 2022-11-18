

import pygame
import sys

from settings import Settings
from footballplayer import Footballplayer
from background import Background
from ball import Ball






class Field:
    pygame.init()

    def __init__(self):
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Football game")
        self.football = Footballplayer(self)
        self.background = Background(self)
        self.ball = pygame.sprite.Group()

    def run_game(self):
        running = True
        while running:
            self._check_events()
            self.football.footballplayer_movement()
            self._update_ball()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._keyup_event(event)

    def _keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.football.moving_right = True
        if event.key == pygame.K_LEFT:
            self.football.moving_left = True
        if event.key == pygame.K_UP:
            self.football.moving_up = True
        if event.key == pygame.K_DOWN:
            self.football.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._throw_football()


        elif event.key == pygame.K_q:
            sys.exit()

    def _keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.football.moving_right = False
        if event.key == pygame.K_LEFT:
            self.football.moving_left = False
        if event.key == pygame.K_UP:
            self.football.moving_up = False
        if event.key == pygame.K_DOWN:
            self.football.moving_down = False


    def _update_ball(self):
        self.ball.update()


    def _update_screen(self):
        self.background.draw_bg()
        self.football.draw_image()
        """somehow draw bullets"""
        self.ball.draw(self.screen)
        pygame.display.flip()



    def _throw_football(self):
        new_ball = Ball(self)
        self.ball.add(new_ball)



field = Field()
field.run_game()