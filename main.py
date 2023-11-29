import pygame
from math import ceil
from settings import *
from board import *
from pieces.pawn import *
from pieces.bishop import *
from pieces.knight import *
from pieces.rook import *
from pieces.queen import *
from pieces.king import *

# TODO: fix valid moves of black pieces
# TODO: remove drag to drop functionality (at least for now)

start_white_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

class Game:
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((win_width, win_height))
		pygame.display.set_caption(title)

		self.clock = pygame.time.Clock()

		self.running = True

		self.start_x = (win_width - width) / 2
		self.start_y = (win_height - height) / 2
		self.positions = self._get_positions()

	def new(self):
		self.all_sprites = pygame.sprite.LayeredUpdates()
		self.pieces_sprites = pygame.sprite.LayeredUpdates()
		self.board = Board(self)
		self.start_fen = start_white_fen

		self.pieces = self._load_pieces_from_fen(start_white_fen)
		self.selected_piece = None
		self.valid_moves = []

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			clicked = event.type == pygame.MOUSEBUTTONDOWN and event.button == 1
			if clicked and self.selected_piece is None:
				x, y = self.get_board_position()
				if x < 0 or y < 0:
					continue

				piece = self.pieces[y][x]
				if piece == "":
					continue

				if not piece.is_white:
					continue

				if len(piece.get_valid_moves()) == 0:
					continue

				if self.selected_piece is not None:
					continue

				self.selected_piece = (piece, (x, y))
				self.valid_moves = piece.get_valid_moves()

			elif clicked and self.selected_piece is not None:
				x, y = self.get_board_position()
				if x < 0 or y < 0:
					continue

				if (x, y) in self.valid_moves:
					if self.pieces[y][x] != "":
						self.pieces[y][x].kill()

					self.pieces[y][x] = self.selected_piece[0]
					old_x, old_y = self.selected_piece[1]
					self.pieces[old_y][old_x] = ""

					self.pieces[y][x].rect.center = self.positions[y][x]
					self.pieces[y][x].has_moved = True

				self.selected_piece = None
				self.valid_moves = []

	def update(self):
		self.all_sprites.update()

	def draw(self):
		self.clock.tick(fps)

		self.screen.fill(bg)
		self.all_sprites.draw(self.screen)
		pygame.display.update()

	def get_board_position(self):
		x, y = pygame.mouse.get_pos()
		x = x - self.start_x
		y = y - self.start_y

		if x <= 0 or x >= width or y <= 0 or y >= height:
			return (-1, -1)

		x = ceil(x / 100) - 1
		y = ceil(y / 100) - 1
		return (x, y)

	# def is_player_in_check(self):
	# 	for r in range(len(self.pieces)):
	# 		for c in range(len(self.pieces[r])):
	# 			piece = self.pieces[r][c]
	# 			if piece == "":
	# 				continue
	# 			if piece.is_white:
	# 				continue

	# 			if self.king_position in piece.get_valid_moves():
	# 				print(piece, r, c, piece.get_valid_moves())
	# 				return True
	# 	return False

	# private functions
	def _get_positions(self):
		pos = []
		for h in range(0, 8):
			row = []
			for w in range(0, 8):
				row.append((w*width/8 + self.start_x + width/16, h*height/8 + self.start_y + height/16))
			pos.append(row)
		return pos

	# def _load_pieces(self):
	# 	pieces = []
	# 	for i in range(len(self.start)):
	# 		for j in range(len(self.start[i])):
	# 			piece = self.start[i][j]
	# 			if piece == empty:
	# 				continue

	# 			is_white = piece[0] == "w"
	# 			if piece[1] == "p":
	# 				pieces.append(Pawn(self, self.positions[i][j], is_white))
	# 			elif piece[1] == "k":
	# 				pieces.append(Knight(self, self.positions[i][j], is_white))
	# 			elif piece[1] == "b":
	# 				pieces.append(Bishop(self, self.positions[i][j], is_white))
	# 			elif piece[1] == "r":
	# 				pieces.append(Rook(self, self.positions[i][j], is_white))
	# 			elif piece[1] == "q":
	# 				pieces.append(Queen(self, self.positions[i][j], is_white))
	# 			elif piece[1] == "K":
	# 				pieces.append(King(self, self.positions[i][j], is_white))
	# 	return pieces

	def _load_pieces_from_fen(self, fen):
		pieces = []
		rows = fen.split("/")
		for i in range(len(rows)):
			j = 0
			row = []
			for c in range(len(rows[i])):
				if j >= 8: break

				char = rows[i][c]
				if str.isnumeric(char):
					char = int(char)
					empty = ["" for i in range(char)]
					row = row + empty
					j += char
					continue

				is_white = str.isupper(char)
				if str.lower(char) == "p":
					row.append(Pawn(self, self.positions[i][j], is_white))
				elif str.lower(char) == "n":
					row.append(Knight(self, self.positions[i][j], is_white))
				elif str.lower(char) == "b":
					row.append(Bishop(self, self.positions[i][j], is_white))
				elif str.lower(char) == "r":
					row.append(Rook(self, self.positions[i][j], is_white))
				elif str.lower(char) == "q":
					row.append(Queen(self, self.positions[i][j], is_white))
				elif str.lower(char) == "k":
					row.append(King(self, self.positions[i][j], is_white))

				j += 1
			pieces.append(row)

		return pieces


if __name__ == "__main__":
	g = Game()
	g.new()

	while g.running:
		g.events()
		g.update()
		g.draw()
