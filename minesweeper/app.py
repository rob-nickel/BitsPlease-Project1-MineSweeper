#!/usr/local/bin/python3
import pygame
from pygame.locals import *
from Minefield import *

class App:
	def __init__(self):
		x_dim = 5
		y_dim = 5
		n_mines = 10

		self.SPACE_WIDTH = 32
		self.SPACE_HEIGHT = 32
		self.WIDTH = self.SPACE_WIDTH*x_dim
		self.HEIGHT = self.SPACE_HEIGHT*y_dim

		self.minefield = Minefield(x_dim, y_dim, n_mines)
		self.grid = self.minefield.minefield

		pygame.init()
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.screen.fill(Color('black'))

		pygame.display.set_caption("BitSweeper")
		clock = pygame.time.Clock()
		
	def onClick(self, event):
		pos = event.pos()
		realPos = (pos[0]/self.WIDTH, pos[1]/self.HEIGHT)
		try:
			activeSpace = self.minefield.getSpace(realPos)
		except:
			pass
		if activeSpace.isRevealed:
			pass
		elif event.button == 1:
			self.minefield.reveal(realPos)
		elif event.button == 3:
			if not activeSpace.isFlagged():
				self.minefield.placeFlag

def main():	
	app = App()

	

	screen.fill(BLACK)

	done = False
	while not done:
		for event in pygame.event.get():
			# Quit Event 
			if event.type == pygame.QUIT:
				done = True

			
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pos = event.pos()
				realPos = (pos[0]/WIDTH, pos[1]/HEIGHT)
				if event.button == 1:
					minefield.reveal(realPos)
				elif event.button == 3:
					minefield.placeFlag

		screen.fill(BLACK)

		pygame.display.flip()

		clock.tick(60)
	
	pygame.quit()

if __name__ == '__main__': main()

		

