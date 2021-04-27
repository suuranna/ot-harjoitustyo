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
        text = font.render("Summa", True, (10, 10, 10))
        text_rect.topleft = (5, 58)
        self.display.blit(text, text_rect)
        text = font.render("Pommit", True, (200, 0, 0))
        text_rect.topleft = (5, 76)
        self.display.blit(text, text_rect)
        for y_coordinate in range(5):
            location_x = 65
            location_y = 75 * y_coordinate + 103
            number = self.level.rowsums[y_coordinate]
            text = font.render(str(number), True, (10, 10, 10))
            text_rect.topleft = (location_x, location_y)
            self.display.blit(text, text_rect)
            bombs = self.level.row_bombs[y_coordinate]
            text = font.render(str(bombs), True, (200, 0, 0))
            text_rect.topleft = (location_x, location_y+20)
            self.display.blit(text, text_rect)
        for x_coordinate in range(5):
            location_x = 75 * x_coordinate + 105
            location_y = 67
            number = self.level.columnsums[x_coordinate]
            text = font.render(str(number), True, (10, 10, 10))
            text_rect.topleft = (location_x, location_y)
            self.display.blit(text, text_rect)
            bombs = self.level.column_bombs[x_coordinate]
            text = font.render(str(bombs), True, (200, 0, 0))
            text_rect.topleft = (location_x+27, location_y)
            self.display.blit(text, text_rect)

    def rendering(self):
        self.display_text()
        self.level.all_sprites.draw(self.display)
        pygame.display.update()
