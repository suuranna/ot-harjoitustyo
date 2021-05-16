import pygame
from application_logic.square import Square

class Level:
    """Luokka, joka kuvaa pelin tasoa ja ylläpitää pelin
       edetessä peliin liittyviä ominaisuuksia, kuten pisteitä

    Attributes:
        squares: Sisältää kaikki neliöt pygame groupina.
        level_matrix: Matriisi, jossa on kerrottu neliöiden numerot.
        sums_and_bombs: Neljässä listassa on joka rivin ja sarakkeen
                        summat ja pommit
        points: Sisältää tiedon sen hetkisestä pistetilanteesta
        maxinum_points: Maksimipisteet, jotka tasosta voi saada
        game_over: Siäsltää tiedon siitä, onko peli hävitty vai ei
        level_number: Kertoo tason numero / monesko taso on menossa.

    """
    def __init__(self, level_number, level_matrix):
        """Luokan konstruktori, joka luo uuden tason

        Args:
            level_number: Kertoo tason numero / monesko taso on menossa.
            level_matrix: Matriisi, jossa on kerrottu neliöiden numerot.

        """
        self.squares = pygame.sprite.Group()
        self.level_matrix = level_matrix
        self.sums_and_bombs = ([0]*5, [0]*5, [0]*5, [0]*5)
        self.points = 0
        self.maxinum_points = 1
        self.init_sprites()
        self.game_over = False
        self.level_number = level_number

    def init_sprites(self):
        """Luo annetun matriisin perusteella neliöt ja antaa niille numerot ja koordinaatit

        """
        for y_coordinate in range(5):
            for x_coordinate in range(5):
                number = self.level_matrix[y_coordinate][x_coordinate]
                self.sums_and_bombs[0][y_coordinate] += number
                self.sums_and_bombs[1][x_coordinate] += number

                if number != 0:
                    self.maxinum_points *= number
                else:
                    self.sums_and_bombs[2][y_coordinate] += 1
                    self.sums_and_bombs[3][x_coordinate] += 1
                location_x = x_coordinate * 1.5 * 50 + 100
                location_y = y_coordinate * 1.5 * 50 + 100
                square = Square(number, location_x, location_y)
                self.squares.add(square)

    def add_points(self, number):
        """Lisää annetun luvun tason sen hetkisiin pisteisiin ja muuttaa pelin tilan
           game overiksi, jos annettu luku on 0.

        """
        if number == 0:
            self.game_over = True
        elif self.points == 0:
            self.points = number
        else:
            self.points *= number
