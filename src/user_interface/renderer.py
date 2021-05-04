import pygame

class Renderer:
    """Luokka, joka vastaa pelinäkymän piirtämisestä

    Attributes:
        display: Kuvaa pelinäkymän ikkunaa
        level: level: Level-luokan olio, joka hallinnoi pelin ominaisuuksia ja kuvaa pelin tasoa
    """
    def __init__(self, display, level):
        """Luokan konstruktori, joka luo uuden näkymän

        Args:
            display: Kuvaa pelinäkymän ikkunaa
            level: level: Level-luokan olio, joka hallinnoi pelin ominaisuuksia ja kuvaa pelin tasoa
        """
        self.display = display
        self.level = level

    def make_text(self, x_coordinate, y_coordinate, text_color, text):
        """Luo tekstin ja piirtää sen pelinäkymään

        Args:
            x_coordinate: Tekstin alueen vasemman yläkulman x-koordinaatti
            y_coordinate: Tekstin alueen vasemman yläkulman y-koordinaatti
            text_color: Tekstin väri
            text: Tekstin sisältö
        """
        font = pygame.font.SysFont('Arial', 20)
        displayed_text = font.render(text, True, text_color)
        text_rect = displayed_text.get_rect()
        text_rect.topleft = (x_coordinate, y_coordinate)
        self.display.blit(displayed_text, text_rect)

    def display_text(self):
        """Määrittelee kaikki tekstit, jotka tulevat mukaan pelinäkymään
        """
        white = (255, 255, 255)
        black = (10, 10, 10)
        red = (200, 0, 0)
        self.display.fill(white)
        self.make_text(5, 5, black,
                       "Pisteet: "+str(self.level.points)+" / "+str(self.level.maxinum_points))
        self.make_text(5, 58, black, "Summa")
        self.make_text(5, 76, red, "Pommit")
        for index in range(5):
            self.make_text(65, 75 * index + 103, black, str(self.level.rowsums[index]))
            self.make_text(65, 75 * index + 123, red, str(self.level.row_bombs[index]))
            self.make_text(75 * index + 105, 67, black, str(self.level.columnsums[index]))
            self.make_text(75 * index + 132, 67, red, str(self.level.column_bombs[index]))

    def rendering(self):
        """Piirtää kaikki neliöt ja tekstit pelinäkymään
        """
        self.display_text()
        self.level.all_sprites.draw(self.display)
        pygame.display.update()
