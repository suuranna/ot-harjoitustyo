import pygame
import os
from square import Square
from level import Level
from renderer import Renderer
from gameloop import Gameloop
from eventqueue import Eventqueue

def main():
	level = Level(matrix, 50)
	display = pygame.display.set_mode((600,600))
	pygame.display.set_caption("Peli")
	#color = (255,255,255)
	#display.fill(color)
	eventqueue = Eventqueue()
	renderer = Renderer(display, level)
	gameloop = Gameloop(level, 50, display, renderer, eventqueue)

	pygame.init()
	gameloop.start()
	#level.all_sprites.draw(display)
	#pygame.display.update()

	#displayText(level, display)

	#pygame.display.update()
	#pygame.display.quit()
	#pygame.quit()

matrix = [[1,1,1,1,1], [1,2,3,1,1], [1,1,1,1,3], [1,2,1,1,1], [1,1,1,1,2]]

if __name__ == "__main__":
	main()
