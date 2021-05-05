import pygame
from application_logic.level import Level

class Gameloop:
    """Luokka, joka kuvaa pelisilmukkaa, jossa luetaan pelaajan syötteet
       ja päivitetään pelinäkymää

    Attributes:
        level: Level-luokan olio, joka hallinnoi pelin ominaisuuksia ja kuvaa pelin tasoa
        display: Kuvaa pelinäkymän ikkunaa
        renderer: Renderer-luokan olio, joka vastaa pelinäkymän piirtämisestä
        events: lista pelaajan syötteistä / pelin tapahtumista
    """
    def __init__(self, level, display, renderer, events):
        """Luokan konstruktori, joka luo uuden Gameloopin

        Args:
            level: Level-luokan olio, joka hallinnoi pelin ominaisuuksia
            display: Kuvaa pelinäkymän ikkunaa
            renderer: Renderer-luokan olio, joka vastaa pelinäkymän piirtämisestä
            events: lista pelaajan syötteistä / pelin tapahtumista
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
            #if self.level.game_over:
            #    break

    def event_handling(self):
        """Käy läpi kaikki eventit / käyttäjän syötteet
        """
        for event in self.events.get_event():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.level.game_over:
                    new_level = Level(1)
                    self.level = new_level
                    self.renderer.level = new_level
                    return
                if self.level.points == self.level.maxinum_points:
                    new_level = Level(self.level.level_number+1)
                    self.level = new_level
                    self.renderer.level = new_level
                    return
                for square in self.level.squares:
                    if square.rect.collidepoint(event.pos):
                        if not square.fliped:
                            if self.level.points == 0:
                                self.level.points = square.number
                            if square.number != 0:
                                self.level.points *= square.number
                            else:
                                self.level.game_over = True
                        square.flip()

    def rendering(self):
        """Piirtää pelinäkymän
        """
        self.renderer.rendering()
