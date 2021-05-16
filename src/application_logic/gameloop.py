import pygame
from application_logic.level import Level
from application_logic.matrix import generate_matrix

class Gameloop:
    """Luokka, joka kuvaa pelisilmukkaa, jossa luetaan pelaajan syötteet
       ja päivitetään pelinäkymää

    Attributes:
        level: Level-luokan olio, joka hallinnoi pelin ominaisuuksia ja kuvaa pelin tasoa
        display: Kuvaa pelinäkymän ikkunaa
        renderer: Renderer-luokan olio, joka vastaa pelinäkymän piirtämisestä
        events: Lista pelaajan syötteistä / pelin tapahtumista

    """
    def __init__(self, level, display, renderer, events):
        """Luokan konstruktori, joka luo uuden Gameloopin

        Args:
            level: Level-luokan olio, joka hallinnoi pelin ominaisuuksia
            display: Kuvaa pelinäkymän ikkunaa
            renderer: Renderer-luokan olio, joka vastaa pelinäkymän piirtämisestä
            events: Lista pelaajan syötteistä / pelin tapahtumista

        """
        self.level = level
        self.display = display
        self.renderer = renderer
        self.events = events

    def start(self):
        """Aloittaa silmukan

        """
        while True:
            if self.event_handling() is False:
                break
            self.rendering()

    def event_handling(self):
        """Käy läpi kaikki eventit / käyttäjän syötteet

        """
        for event in self.events.get_event():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.level.game_over or (self.level.points == self.level.maxinum_points \
                                            and self.level.level_number == 10):
                    matrix = generate_matrix(5, 1)
                    new_level = Level(1, matrix)
                    self.level = new_level
                    self.renderer.level = new_level
                    return
                if self.level.points == self.level.maxinum_points:
                    matrix = generate_matrix(5, self.level.level_number+1)
                    new_level = Level(self.level.level_number+1, matrix)
                    self.level = new_level
                    self.renderer.level = new_level
                    return
                for square in self.level.squares:
                    if square.rect.collidepoint(event.pos):
                        if not square.fliped:
                            self.level.add_points(square.number)
                        square.flip()

    def rendering(self):
        """Piirtää pelinäkymän

        """
        self.renderer.rendering()
