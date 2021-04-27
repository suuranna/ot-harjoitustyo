import pygame
from application_logic.square import Square

class Level:
    def __init__(self, level_matrix):
        self.squares = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.rowsums = [0]*5
        self.columnsums = [0]*5
        self.row_bombs = [0]*5
        self.column_bombs = [0]*5
        self.points = 0
        self.maxinum_points = 1
        self.init_sprites(level_matrix)

    def init_sprites(self, level_matrix):
        for y_coordinate in range(5):
            for x_coordinate in range(5):
                number = level_matrix[y_coordinate][x_coordinate]
                self.rowsums[y_coordinate] += number
                self.columnsums[x_coordinate] += number
                if number != 0:
                    self.maxinum_points *= number
                if number == 0:
                    self.row_bombs[y_coordinate] += 1
                    self.column_bombs[x_coordinate] += 1
                location_x = x_coordinate * 1.5 * 50 + 100
                location_y = y_coordinate * 1.5 * 50 + 100
                square = Square(number, location_x, location_y)
                self.squares.add(square)
        self.all_sprites.add(self.squares)