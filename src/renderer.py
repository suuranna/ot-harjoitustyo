import pygame

class Renderer:
    def __init__(self, display, level):
        self.display = display
        self.level = level

    def display_text(self):
        color = (255, 255, 255)
        self.display.fill(color)
        font = pygame.font.SysFont('Arial', 20)
        text = font.render("Pisteet: "+str(self.level.points)+" / "+str(self.level.maxinum_points),
                           True, (10, 10, 10))
        text_rect = text.get_rect()
        text_rect.topleft = (5, 5)
        self.display.blit(text, text_rect)
        for y_coordinate in range(5):
            location_x = 60
            location_y = 75 * y_coordinate + 105
            number = self.level.rowsums[y_coordinate]
            font = pygame.font.SysFont('Arial', 20)
            text = font.render(str(number), True, (10, 10, 10))
            text_rect = text.get_rect()
            text_rect.topleft = (location_x, location_y)
            self.display.blit(text, text_rect)
        for x_coordinate in range(5):
            location_x = 75 * x_coordinate + 110
            location_y = 60
            number = self.level.columnsums[x_coordinate]
            font = pygame.font.SysFont('Arial', 20)
            text = font.render(str(number), True, (10, 10, 10))
            text_rect = text.get_rect()
            text_rect.topleft = (location_x, location_y)
            self.display.blit(text, text_rect)

    def rendering(self):
        self.display_text()
        self.level.all_sprites.draw(self.display)
        pygame.display.update()
