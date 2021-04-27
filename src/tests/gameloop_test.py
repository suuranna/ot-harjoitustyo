import unittest
import pygame

from application_logic.level import Level
from application_logic.gameloop import Gameloop

matrix_1 = [[1,2,1,1,0],
            [0,1,0,3,1],
            [3,1,0,0,1],
            [1,2,1,1,2],
            [1,1,3,1,0]]

class TestGameloop(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(matrix_1)
