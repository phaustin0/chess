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

# start_white = [
#     [black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight, black_rook],
#     [black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],
#     [empty, empty, empty, empty, empty, empty, empty, empty,],
#     [empty, empty, empty, empty, empty, empty, empty, empty,],
#     [empty, empty, empty, empty, empty, empty, empty, empty,],
#     [empty, empty, empty, empty, empty, empty, empty, empty,],
#     [white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn,],
#     [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook],
# ]
start_white_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

# start_black = [
#     [white_rook, white_knight, white_bishop, white_king, white_queen, white_bishop, white_knight, white_rook],
#     [white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn,],
#     [empty, empty, empty, empty, empty, empty, empty, empty,],
#     [empty, empty, empty, empty, empty, empty, empty, empty,],
#     [empty, empty, empty, empty, empty, empty, empty, empty,],
#     [empty, empty, empty, empty, empty, empty, empty, empty,],
#     [black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],
#     [black_rook, black_knight, black_bishop, black_king, black_queen, black_bishop, black_knight, black_rook],
# ]
start_black_fen = "RNBKQBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbkqbnr"

class Game:
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((win_width, win_height))
		pygame.display.set_caption(title)

		self.clock = pygame.time.Clock()

		self.running = True
		self.is_white = True

		self.start_x = (win_width - width) / 2
		self.start_y = (win_height - height) / 2
		self.positions = self._get_positions()

	def new(self):
		self.all_sprites = pygame.sprite.LayeredUpdates()
		self.pieces_sprites = pygame.sprite.LayeredUpdates()
		self.board = Board(self)
		# self.start = start_white if self.is_white else start_black
		self.start_fen = start_white_fen if self.is_white else start_black_fen

		self.pieces = self._load_pieces_from_fen(self.start_fen)
		self.moved_piece = None

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button != 1:
					continue

				x, y = self._get_board_position()
				if x < 0 or y < 0:
					continue

				piece = self.pieces[x][y]
				if piece == "":
					continue
				self.moved_piece = piece
				self.pieces[x][y] = ""

			if event.type == pygame.MOUSEBUTTONUP:
				if event.button != 1: continue
				if self.moved_piece is None: continue

				x, y = self._get_board_position()
				if self.pieces[x][y] != "":
					self.pieces[x][y].kill()

				self.pieces[x][y] = self.moved_piece
				self.moved_piece.has_moved = True
				self.moved_piece.rect.center = self.positions[x][y]
				self.moved_piece = None

	def update(self):
		if self.moved_piece is not None:
			self.moved_piece.rect.center = pygame.mouse.get_pos()
		self.all_sprites.update()

	def draw(self):
		self.clock.tick(fps)

		self.screen.fill(bg)
		self.all_sprites.draw(self.screen)
		pygame.display.update()

	# private functions
	def _get_board_position(self):
		y, x = pygame.mouse.get_pos()
		x = x - self.start_x
		y = y - self.start_y

		if x <= 0 or x >= width or y <= 0 or y >= height:
			return (-1, -1)

		x = ceil(x / 100) - 1
		y = ceil(y / 100) - 1
		return (x, y)

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
