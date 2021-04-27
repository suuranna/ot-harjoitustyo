import pygame

class Gameloop:
    def __init__(self, level, display, renderer, events):
        self.level = level
        self.display = display
        self.renderer = renderer
        self.events = events

    def start(self):
        while True:
            if self.event_handling() is False:
                break
            self.rendering()

    def event_handling(self):
        for event in self.events.get_event():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for square in self.level.squares:
                    if square.rect.collidepoint(event.pos):
                        if not square.fliped:
                            if self.level.points == 0:
                                self.level.points = square.number
                            else:
                                if square.number != 0:
                                    self.level.points *= square.number
                            #if square.number == 0:
                                #return False
                        square.flip()
    def rendering(self):
        self.renderer.rendering()
