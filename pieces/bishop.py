import pygame
from pieces.piece import *

class Bishop(Piece):
    def __init__(self, game, pos, white):
        self.game = game
        super().__init__(self.game, pos, white, f"{'white' if white else 'black'} bishop")

    def get_valid_moves(self):
        moves = []
        x,y = self.game.get_board_position()

        # upper left
        i = min(x, y)
        for j in range(i):
            if self.game.pieces[y-j-1][x-j-1] == "":
                moves.append((x - j - 1, y - j - 1))
                continue

            if self.game.pieces[y-j-1][x-j-1].is_white != self.is_white:
                moves.append((x - j - 1, y - j - 1))
            break

        # lower left
        i = min(x, 7 - y)
        for j in range(i):
            if self.game.pieces[y+j+1][x-j-1] == "":
                moves.append((x - j - 1, y + j + 1))
                continue

            if self.game.pieces[y+j+1][x-j-1].is_white != self.is_white:
                moves.append((x - j - 1, y + j + 1))
            break

        # upper right
        i = min(7 - x, y)
        for j in range(i):
            if self.game.pieces[y-j-1][x+j+1] == "":
                moves.append((x + j + 1, y - j - 1))
                continue

            if self.game.pieces[y-j-1][x+j+1].is_white != self.is_white:
                moves.append((x + j + 1, y - j - 1))
            break

        # lower right
        i = min(7 - x, 7 - y)
        for j in range(i):
            if self.game.pieces[y+j+1][x+j+1] == "":
                moves.append((x + j + 1, y + j + 1))
                continue

            if self.game.pieces[y+j+1][x+j+1].is_white != self.is_white:
                moves.append((x + j + 1, y + j + 1))
            break

        return moves