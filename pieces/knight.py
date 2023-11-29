import pygame
from pieces.piece import *

class Knight(Piece):
    def __init__(self, game, pos, white):
        self.game = game
        super().__init__(self.game, pos, white, f"{'white' if white else 'black'} knight")

    def move(self):
        pass

    def get_valid_moves(self):
        pass