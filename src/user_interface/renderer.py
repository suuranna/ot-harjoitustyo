import pygame

class Renderer:
    """Luokka, joka vastaa pelinäkymän piirtämisestä

    Attributes:
        display: Kuvaa pelinäkymän ikkunaa
        level: Level-luokan olio, joka hallinnoi pelin ominaisuuksia ja kuvaa pelin tasoa

    """
    def __init__(self, display, level):
        """Luokan konstruktori, joka luo uuden näkymän

        Args:
            display: Kuvaa pelinäkymän ikkunaa
            level: Level-luokan olio, joka hallinnoi pelin ominaisuuksia ja kuvaa pelin tasoa

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
        if text in ("GAME OVER", "LEVEL COMPLETED", "GAME COMPLEETED"):
            font = pygame.font.SysFont('Arial', 60)
        if "Click" in text:
            font = pygame.font.SysFont('Arial', 30)
        displayed_text = font.render(text, True, text_color)
        text_rect = displayed_text.get_rect()
        text_rect.topleft = (x_coordinate, y_coordinate)
        self.display.blit(displayed_text, text_rect)

    def display_text(self):
        """Määrittelee kaikki tekstit, jotka tulevat mukaan pelinäkymään

        """
        black = (10, 10, 10)
        red = (200, 0, 0)
        self.make_text(5, 5, black,
                       "Points: "+str(self.level.points)+" / "+str(self.level.maxinum_points))
        self.make_text(400, 5, black, "Level: "+str(self.level.level_number))
        self.make_text(5, 58, black, "Sum")
        self.make_text(5, 76, red, "Bombs")
        for index in range(5):
            self.make_text(65, 75 * index + 103, black, str(self.level.sums_and_bombs[0][index]))
            self.make_text(65, 75 * index + 123, red, str(self.level.sums_and_bombs[2][index]))
            self.make_text(75 * index + 105, 67, black, str(self.level.sums_and_bombs[1][index]))
            self.make_text(75 * index + 132, 67, red, str(self.level.sums_and_bombs[3][index]))
        if self.level.game_over:
            self.make_text(100, 250, red, "GAME OVER")
            self.make_text(10, 300, red, "Click anywhere to start again from level 1")
        if self.level.points == self.level.maxinum_points:
            self.make_text(10, 250, red, "LEVEL COMPLETED")
            self.make_text(55, 300, red, "Click anywhere to start a new level")
        if self.level.points == self.level.maxinum_points and self.level.level_number == 10:
            self.make_text(10, 250, red, "GAME COMPLETED")
            self.make_text(55, 300, red, "Click anywhere to start again from level 1")

    def rendering(self):
        """Piirtää kaikki neliöt ja tekstit pelinäkymään

        """
        color = (132, 151, 165)
        self.display.fill(color)
        self.level.squares.draw(self.display)
        self.display_text()
        pygame.display.update()
