import pygame
from settings import *
from tile import *

class Board(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface([width, height])

        self.rect = self.image.get_rect()
        self.rect.center = (width / 2 + self.game.start_x, height / 2 + self.game.start_y)
        self.draw_board()

    def draw_board(self):
        white = 1
        for h in range(0,8):
            for w in range(0,8):
                Tile(self.game, light if white else dark, (w*width/8 + self.game.start_x, h*height/8 + self.game.start_y))
                white = (white + 1) % 2
            white = (white + 1) % 2
