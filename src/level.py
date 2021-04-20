import pygame
from square import Square

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

