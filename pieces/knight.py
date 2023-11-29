import pygame
from pieces.piece import *

class Knight(Piece):
    def __init__(self, game, pos, white):
        self.game = game
        super().__init__(self.game, pos, white, f"{'white' if white else 'black'} knight")

    def get_valid_moves(self):
        moves = []
        x,y = self.game.get_board_position()

        possible_moves = [(x - 1, y - 2), (x + 1, y - 2), # top left, top right
                          (x + 2, y + 1), (x + 2, y - 1), # right top, right bottom
                          (x - 1, y + 2), (x + 1, y + 2), # bottom left, bottom right
                          (x - 2, y + 1), (x - 2, y - 1)] # left top, bottom left

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