import pygame
from pieces.piece import *

class Rook(Piece):
    def __init__(self, game, pos, white):
        self.game = game
        super().__init__(self.game, pos, white, f"{'white' if white else 'black'} rook")

    def get_valid_moves(self):
        moves = []
        x, y = self.game.get_board_position()

        # left
        for i in range(x-1,-1,-1):
            if self.game.pieces[y][i] == "":
                moves.append((i, y))
                continue

            if self.game.pieces[y][i].is_white != self.is_white:
                moves.append((i, y))
            break

        # right
        for i in range(x+1, 8):
            if self.game.pieces[y][i] == "":
                moves.append((i, y))
                continue

            if self.game.pieces[y][i].is_white != self.is_white:
                moves.append((i, y))
            break

        # up
        for i in range(y-1,-1,-1):
            if self.game.pieces[i][x] == "":
                moves.append((x, i))
                continue

            if self.game.pieces[i][x].is_white != self.is_white:
                moves.append((x, i))
            break

        # down
        for i in range(y+1, 8):
            if self.game.pieces[i][x] == "":
                moves.append((x, i))
                continue

            if self.game.pieces[i][x].is_white != self.is_white:
                moves.append((x, i))
            break

        return moves