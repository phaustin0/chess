import pygame
from settings import *
from board import *
from pieces.pawn import *
from pieces.bishop import *
from pieces.knight import *
from pieces.rook import *

start_white = [
    [black_rook, black_knight, black_bishop, black_queen, black_king, black_bishop, black_knight, black_rook],
    [black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],
    [empty, empty, empty, empty, empty, empty, empty, empty,],
    [empty, empty, empty, empty, empty, empty, empty, empty,],
    [empty, empty, empty, empty, empty, empty, empty, empty,],
    [empty, empty, empty, empty, empty, empty, empty, empty,],
    [white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn,],
    [white_rook, white_knight, white_bishop, white_queen, white_king, white_bishop, white_knight, white_rook],
]

start_black = [
    [white_rook, white_knight, white_bishop, white_king, white_queen, white_bishop, white_knight, white_rook],
    [white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn, white_pawn,],
    [empty, empty, empty, empty, empty, empty, empty, empty,],
    [empty, empty, empty, empty, empty, empty, empty, empty,],
    [empty, empty, empty, empty, empty, empty, empty, empty,],
    [empty, empty, empty, empty, empty, empty, empty, empty,],
    [black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn, black_pawn],
    [black_rook, black_knight, black_bishop, black_king, black_queen, black_bishop, black_knight, black_rook],
]

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
		self.pieces = pygame.sprite.LayeredUpdates()
		self.board = Board(self)
		self.start = start_white if self.is_white else start_black

		Pawn(self, self._get_positions()[0][0], self.is_white)
		Pawn(self, self._get_positions()[0][1], not self.is_white)
		Bishop(self, self._get_positions()[0][2], self.is_white)
		Bishop(self, self._get_positions()[0][3], not self.is_white)
		Knight(self, self._get_positions()[0][4], self.is_white)
		Knight(self, self._get_positions()[0][5], not self.is_white)
		Rook(self, self._get_positions()[0][6], self.is_white)
		Rook(self, self._get_positions()[0][7], not self.is_white)

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def update(self):
		self.all_sprites.update()

	def draw(self):
		self.clock.tick(fps)

		self.screen.fill(bg)
		self.all_sprites.draw(self.screen)
		pygame.display.update()

	def _get_positions(self):
		pos = []
		for h in range(0, 8):
			row = []
			for w in range(0, 8):
				row.append((w*width/8 + self.start_x + width/16, h*height/8 + self.start_y + height/16))
			pos.append(row)
		return pos


if __name__ == "__main__":
	g = Game()
	g.new()

	while g.running:
		g.events()
		g.update()
		g.draw()
