import pygame

class Gameloop:
        def __init__(self, level, square_size, display, renderer, events):
                self.level = level
                self.square_size = square_size
                self.display = display
                self.renderer = renderer
                self.events = events

        def start(self):
                while True:
                        if self.event_handling() == False:
                                break
                        self.rendering()

        def event_handling(self):
                for event in self.events.get_event():
                        if event.type == pygame.QUIT:
                                return False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                for square in self.level.squares:
                                        #if event.pos[0] > square.rect.x and event.pos[0] < square.rect.x+50 and event.pos[1] > square.rect.y and event.pos[1] < square.rect.y+50:
                                        if square.rect.collidepoint(event.pos):
                                                square.flip()
#print(square.number, int(square.rect.x), int(square.rect.y))
#self.level.all_sprites.flip(self.events.get_event())

        def rendering(self):
                self.renderer.rendering()
