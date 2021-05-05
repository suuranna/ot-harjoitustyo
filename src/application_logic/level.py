import pygame
from application_logic.matrix import generate_matrix
from application_logic.square import Square

class Level:
    """Luokka, joka kuvaa pelin tasoa ja ylläpitää pelin
       edetessä peliin liittyviä ominaisuuksia, kuten pisteitä

    Attributes:
        level_number: Kertoo tason numero / monesko taso on menossa
    """
    def __init__(self, level_number):
        """Luokan konstruktori, joka luo uuden tason

        Args:
            level_number: Kertoo tason numero / monesko taso on menossa
        """
        self.squares = pygame.sprite.Group()
        self.sums = ([0]*5, [0]*5)
        self.bombs = ([0]*5, [0]*5)
        self.points = 0
        self.maxinum_points = 1
        self.init_sprites()
        self.game_over = False
        self.level_number = level_number

    def renew_level(self, new_level_number):
        """Nollaa kaiken, jolloin syntyy uusi taso

        Args:
            new_level_number: Kertoo uuden tason numero / monesko taso on menossa
        """
        self.squares.empty()
        self.level_number = new_level_number
        self.sums = ([0]*5, [0]*5)
        self.bombs = ([0]*5, [0]*5)
        self.points = 0
        self.maxinum_points = 1
        self.game_over = False
        self.init_sprites()

    def init_sprites(self):
        """Luo annetun matriisin perusteella neliöt ja antaa niille numerot ja koordinaatit

        Args:
            level_matrix: Matriisi, joka kuvaa mitä numeroita on missäkin neliössä
        """
        level_matrix = generate_matrix(5)

        for y_coordinate in range(5):
            for x_coordinate in range(5):
                number = level_matrix[y_coordinate][x_coordinate]
                self.sums[0][y_coordinate] += number
                self.sums[1][x_coordinate] += number

                if number != 0:
                    self.maxinum_points *= number
                else:
                    self.bombs[0][y_coordinate] += 1
                    self.bombs[1][x_coordinate] += 1
                location_x = x_coordinate * 1.5 * 50 + 100
                location_y = y_coordinate * 1.5 * 50 + 100
                square = Square(number, location_x, location_y)
                self.squares.add(square)
