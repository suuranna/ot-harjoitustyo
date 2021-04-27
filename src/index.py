import pygame
from level import Level
from renderer import Renderer
from gameloop import Gameloop
from eventqueue import Eventqueue
from matrix import generate_matrix

def main():
    matrix1 = generate_matrix(5)
    level = Level(matrix1)
    display = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Peli")
    eventqueue = Eventqueue()
    renderer = Renderer(display, level)
    gameloop = Gameloop(level, display, renderer, eventqueue)

    pygame.init()
    gameloop.start()

#matrix = [[1, 1, 1, 1, 1], [1, 2, 3, 1, 1], [1, 1, 1, 1, 3],
#          [1, 2, 1, 1, 1], [1, 1, 1, 1, 2]]

if __name__ == "__main__":
    main()
