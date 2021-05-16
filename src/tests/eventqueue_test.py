import unittest

from application_logic.eventqueue import Eventqueue

class TestEventqueue(unittest.TestCase):
    def setUp(self):
        self.eventqueue = Eventqueue()

    #def test_f(self):
