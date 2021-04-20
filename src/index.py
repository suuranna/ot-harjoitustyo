import pygame
import os

class GameLoop:
	def __init__(self, level, square_size, display):
		self.level = level
		self.square_size = square_size
		self.display = display

	def start(self):
		return
		while True:
			if self.event_handling() == False:
				break

	def event_handling(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
			if event.key == pygame.MOUSEBUTTONDOWN:
				return

class Level:
	def __init__(self, level_matrix, square_size):
		self.square_size = square_size
		self.squares = pygame.sprite.Group()
		self.all_sprites = pygame.sprite.Group()
		self.rowsums = [0]*5
		self.columnsums = [0]*5
		self.maxinumPoints = 1
		self.init_sprites(level_matrix)

	def init_sprites(self, level_matrix):
		for y in range(5):
			for x in range(5):
				number = level_matrix[y][x]
				self.rowsums[y] += number
				self.columnsums[x] += number
				self.maxinumPoints *= number
				locationX = x*1.5 * self.square_size+100 
				locationY = y*1.5 * self.square_size+100
				square = Square(self.square_size, number, locationX, locationY)
				self.squares.add(square)
		self.all_sprites.add(self.squares)

dirname = os.path.dirname("/home/suuranna/Ohjelmistotekniikka_jutut/ot-harjoitustyo")

class Square(pygame.sprite.Sprite):
	def __init__(self, square_size, number, x, y):
		super().__init__()
		self.square_size = square_size
		#self.rect = pygame.Rect(x, y, self.square_size, self.square_size)
		self.number = number
		self.fliped = False

		self.image = pygame.image.load(os.path.join(dirname, "ot-harjoitustyo", "kuvake.png"))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		#self.image = pygame.Rect(x, y, 50, 50)
		#self.rect = pygame.Rect(x, y, 50, 50)

	def flip(self):
		if not self.fliped:
			self.fliped = True

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
