import unittest

from application_logic.square import Square

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square_1 = Square(2, 50, 50)

    def test_flipping_works_when_not_fliped(self):
        self.square_1.flip()
        self.assertEqual(self.square_1.fliped, True)

    def test_flipping_works_when_already_fliped(self):
        self.square_1.flip()
        self.square_1.flip()
        self.assertEqual(self.square_1.fliped, True)

