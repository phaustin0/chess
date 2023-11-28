import pygame
import os
import io
from settings import *

class Piece(pygame.sprite.Sprite):
    def __init__(self, game, pos, img_path):
        self.game = game
        self.groups = self.game.all_sprites, self.game.pieces
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.is_moved = False

        # scale = 2
        path = os.path.join(os.getcwd(),f"pieces/img/{img_path}.png")
        # svg_string = open(path, "rt").read()
        # start = svg_string.find('<svg')
        # if start > 0:
        #     svg_string = svg_string[:start+4] + f' transform="scale({scale},{scale})"' + svg_string[start+4:]
        # self.image = pygame.image.load(io.BytesIO(svg_string.encode()))
        self.image = pygame.image.load(path)
        # self.image = pygame.transform.smoothscale(self.image,(75,75))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move(self):
        pass

    def get_valid_moves(self):
        pass