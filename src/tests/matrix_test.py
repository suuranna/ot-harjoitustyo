import unittest

from application_logic.matrix import *

class TestMatrx(unittest.TestCase):
    def setUp(self):
        self.matrix = generate_matrix(5)

    #def test_flipping_works_when_not_fliped(self):
