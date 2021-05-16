import unittest

from application_logic.level import Level

matrix_1 = [[1,2,1,1,0],
            [0,1,0,3,1],
            [3,1,0,0,1],
            [1,2,1,1,2],
            [1,1,3,1,0]]

m_1_rowsums = [5,5,5,7,6]
m_1_columnsums = [6,7,5,6,4]
m_1_row_bombs = [1,2,2,0,1]
m_1_column_bombs = [1,0,2,1,2]

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level_1 = Level(1, matrix_1)

    def test_row_and_column_sums_are_correct(self):
        self.assertEqual(self.level_1.sums_and_bombs[0], m_1_rowsums)
        self.assertEqual(self.level_1.sums_and_bombs[1], m_1_columnsums)

    def test_row_and_column_bombs_are_correct(self):
        self.assertEqual(self.level_1.sums_and_bombs[2], m_1_row_bombs)
        self.assertEqual(self.level_1.sums_and_bombs[3], m_1_column_bombs)

    def test_add_points_correctly(self):
        self.assertEqual(self.level_1.points, 0)
        self.level_1.add_points(3)
        self.assertEqual(self.level_1.points, 3)
        self.level_1.add_points(2)
        self.assertEqual(self.level_1.points, 6)
        self.level_1.add_points(1)
        self.assertEqual(self.level_1.points, 6)

    def test_game_over_happens(self):
        self.assertEqual(self.level_1.points, 0)
        self.assertEqual(self.level_1.game_over, False)
        self.level_1.add_points(0)
        #self.assertEqual(self.level_1.points, 0)
        self.assertEqual(self.level_1.game_over, True)

