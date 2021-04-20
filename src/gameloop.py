import pygame

class GameLoop:
        def __init__(self, level, square_size, display):
                self.level = level
                self.square_size = square_size
                self.display = display

        def start(self):
                return
                while True:
                        if self.event_handling() == False:
                                break

        def event_handling(self):
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return False
                        if event.key == pygame.MOUSEBUTTONDOWN:
                                return

