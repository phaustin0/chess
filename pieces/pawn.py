import pygame
from pieces.piece import *

class Pawn(Piece):
    def __init__(self, game, pos, white):
        self.game = game
        super().__init__(self.game, pos, white, f"{'white' if white else 'black'} pawn")

    def get_valid_moves(self):
        moves = []
        x,y = self.game.get_board_position()

        if not self.has_moved:
            moves.append((x, y - 2))

        if self.game.pieces[y-1][x] == "":
            moves.append((x, y - 1))

        can_capture_left = x > 0 and self.game.pieces[y-1][x-1] != "" and self.game.pieces[y-1][x-1].is_white != self.is_white
        if can_capture_left:
            moves.append((x - 1, y - 1))

        can_capture_right = x < 7 and self.game.pieces[y-1][x+1] != "" and self.game.pieces[y-1][x+1].is_white != self.is_white
        if can_capture_right:
            moves.append((x + 1, y - 1))

        # TODO: en passant

        return moves