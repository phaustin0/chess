import pygame
from settings import *
from tile import *

class Board(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface([width, height])

        self.start_x = (win_width - width) / 2
        self.start_y = (win_height - height) / 2
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2 + self.start_x, height / 2 + self.start_y)
        self.draw_board()

    def draw_board(self):
        white = 1
        for h in range(0,8):
            for w in range(0,8):
                Tile(self.game, light if white else dark, (w*width/8 + self.start_x, h*height/8 + self.start_y))
                white = (white + 1) % 2
            white = (white + 1) % 2
