import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, game, color, position):
        self.game = game
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.image = pygame.Surface([width/8, height/8])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = position