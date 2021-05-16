import unittest
import pygame

from user_interface.renderer import Renderer
from application_logic.level import Level
from application_logic.gameloop import Gameloop
from application_logic.eventqueue import Eventqueue


matrix_1 = [[1,2,1,1,0],
            [0,1,0,3,1],
            [3,1,0,0,1],
            [1,2,1,1,2],
            [1,1,3,1,0]]

matrix_2 = [[1,1,1,2,0],
            [0,3,0,1,1],
            [0,1,3,0,1],
            [1,2,1,3,2],
            [1,2,3,1,0]]

class TestGameloop(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(1, matrix_1)
        self.level_2 = Level(2, matrix_2)
        display = pygame.display.set_mode((600, 600))
        eventqueue = Eventqueue()
        renderer = Renderer(display, level)
        self.gameloop = Gameloop(self.level_1, display, renderer, eventqueue)

    #def test_clicking(self):
