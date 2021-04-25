import pygame

class Eventqueue:
    def get_event(self):
        return pygame.event.get()
