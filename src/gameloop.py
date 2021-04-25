import pygame

class Gameloop:
    def __init__(self, level, display, renderer, events):
        self.level = level
        self.display = display
        self.renderer = renderer
        self.events = events

    def start(self):
        while True:
            if not self.event_handling():
                break
            self.rendering()

    def event_handling(self):
        for event in self.events.get_event():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for square in self.level.squares:
                    #if event.pos[0] > square.rect.x and event.pos[0] <
                    # square.rect.x+50 and event.pos[1] > square.rect.y
                    # and event.pos[1] < square.rect.y+50:
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
                return True
    def rendering(self):
        self.renderer.rendering()
