import pygame
import os
import io
from settings import *

class Piece(pygame.sprite.Sprite):
    def __init__(self, game, pos, is_white, img_path):
        self.game = game
        self.groups = self.game.all_sprites, self.game.pieces_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.has_moved = False

        path = os.path.join(os.getcwd(),f"pieces/img/{img_path}.png")
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        self.is_white = is_white