import pygame
from pieces.piece import *

class Queen(Piece):
    def __init__(self, game, pos, white):
        self.game = game
        super().__init__(self.game, pos, white, f"{'white' if white else 'black'} queen")

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