# -*- coding: utf-8 -*-

import unittest
from .context import gameoflife as gol



class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_helper_valid_x(self):
        g = gol.Gameoflife(5, 5)
        assert False

    def test_helper_valid_y(self):
        g = gol.Gameoflife(5, 5)
        self.assertFalse(g.is_valid_y(55))
        assert False

    def test_method_is_alive(self):
        g = gol.Gameoflife(5, 5)
        assert False

    def test_method_count_live_neighbours(self):
        g = gol.Gameoflife(5, 5)
        self.assertEqual(gol.count_live_neighbours(1,1), 0)
        g.next_generation()
        self.assertEqual(gol.count_live_neighbours(1,1), 0)
        assert False

if __name__ == '__main__':
    unittest.main()
