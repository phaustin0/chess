import pygame
from pieces.piece import *

class King(Piece):
    def __init__(self, game, pos, white):
        self.game = game
        super().__init__(self.game, pos, white, f"{'white' if white else 'black'} king")

    def get_valid_moves(self):
        moves = []
        x,y = self.game.get_board_position()

        possible_moves = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), # top
                          (x - 1, y), (x + 1, y),                     # middle
                          (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)] # bottom

        for move in possible_moves:
            x, y = move
            tile_exists = x >= 0 and x < 8 and y >= 0 and y < 8

            if not tile_exists: continue
            if self.game.pieces[y][x] == "":
                moves.append((x, y))
                continue

            if self.game.pieces[y][x].is_white != self.is_white:
                moves.append((x, y))

        return moves