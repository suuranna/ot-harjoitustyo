import pygame
from user_interface.renderer import Renderer
from application_logic.matrix import generate_matrix
from application_logic.level import Level
from application_logic.gameloop import Gameloop
from application_logic.eventqueue import Eventqueue

def main():
    matrix = generate_matrix(5)
    level = Level(1, matrix)
    display = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Peli")
    eventqueue = Eventqueue()
    renderer = Renderer(display, level)
    gameloop = Gameloop(level, display, renderer, eventqueue)

    pygame.init()
    gameloop.start()

if __name__ == "__main__":
    main()
