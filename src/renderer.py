import pygame

class Renderer:
	def __init__(self, display, level):
		self.display = display
		self.level = level

	def display_text(self):
                color = (255,255,255)
                self.display.fill(color)
                font = pygame.font.SysFont('Arial', 20)
                text = font.render("Pisteet: "+str(self.level.points), True, (10,10,10))
                textRect = text.get_rect()
                textRect.topleft = (5,5)
                self.display.blit(text, textRect)
                for y in range(5):
                        locationX = 60
                        locationY = 75 * y + 105
                        number = self.level.rowsums[y]
                        font = pygame.font.SysFont('Arial', 20)
                        text = font.render(str(number), True, (10,10,10))
                        textRect = text.get_rect()
                        textRect.topleft = (locationX,locationY)
                        self.display.blit(text, textRect)
                for x in range(5):
                        locationX = 75 * x + 110 
                        locationY = 60
                        number = self.level.columnsums[x]
                        font = pygame.font.SysFont('Arial', 20)
                        text = font.render(str(number), True, (10,10,10))
                        textRect = text.get_rect()
                        textRect.topleft = (locationX,locationY)
                        self.display.blit(text, textRect)

	def rendering(self):
		self.display_text()
		self.level.all_sprites.draw(self.display)
		pygame.display.update()
