import pygame
from settings import *

class Game:
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption(title)

		self.clock = pygame.time.Clock()

		self.running = True

	def new(self):
		pass

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

	def update(self):
		pass

	def draw(self):
		self.clock.tick(fps)


if __name__ == "__main__":
	g = Game()
	g.new()

	while g.running:
		g.events()
		g.update()
		g.draw()
