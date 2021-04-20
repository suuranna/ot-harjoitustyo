import pygame
import os
from square import Square
from level import Level


def displayText(level, display):
	font = pygame.font.SysFont('Arial', 20)
	text = font.render("Pisteet: "+str(level.maxinumPoints), True, (10,10,10))
	textRect = text.get_rect()
	textRect.topleft = (5,5)
	display.blit(text, textRect)
	for y in range(5):
		locationX = 50 
		locationY = 75 * y + 105
		number = level.rowsums[y]
		font = pygame.font.SysFont('Arial', 20)
		text = font.render(str(number), True, (10,10,10))
		textRect = text.get_rect()
		textRect.topleft = (locationX,locationY)
		display.blit(text, textRect)
	for x in range(5):
		locationX = 75 * x + 105 
		locationY = 50
		number = level.columnsums[x]
		font = pygame.font.SysFont('Arial', 20)
		text = font.render(str(number), True, (10,10,10))
		textRect = text.get_rect()
		textRect.topleft = (locationX,locationY)
		display.blit(text, textRect)

def main():
	level = Level(matrix, 50)
	display = pygame.display.set_mode((600,600))
	pygame.display.set_caption("Peli")
	color = (255,255,255)
	display.fill(color)

	pygame.init()
	level.all_sprites.draw(display)
	pygame.display.update()

	displayText(level, display)

	pygame.display.update()
	#pygame.display.quit()
	#pygame.quit()

matrix = [[1,1,1,1,1], [1,2,3,1,1], [1,1,1,1,3], [1,2,1,1,1], [1,1,1,1,2]]

if __name__ == "__main__":
	main()
