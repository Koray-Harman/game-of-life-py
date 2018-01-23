# -*- coding: utf-8 -*-

import unittest
from .context import gameoflife as gol



class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True

    def test_helper_valid_x(self):
        g = gol.Gameoflife(5, 5)
        self.assertFalse(g.is_valid_x(55))
        self.assertFalse(g.is_valid_x(5))
        self.assertFalse(g.is_valid_x(6))
        self.assertTrue(g.is_valid_x(4))

    def test_helper_valid_y(self):
        g = gol.Gameoflife(5, 5)
        self.assertFalse(g.is_valid_y(55))
        self.assertFalse(g.is_valid_y(5))
        self.assertFalse(g.is_valid_y(6))
        self.assertTrue(g.is_valid_y(4))

    def test_method_is_alive(self):
        g = gol.Gameoflife(5, 5)
        g.set_all_values(True)
        self.assertTrue(g.is_alive(0,0))
        self.assertTrue(g.is_alive(4,4))
        self.assertFalse(g.is_alive(5,5))
        self.assertFalse(g.is_alive(-1,-1))

    def test_method_count_live_neighbours(self):
        g = gol.Gameoflife(5, 5)
        g.set_all_values(True)
        self.assertEqual(g.count_live_neighbours(0, 0), 3)
        self.assertEqual(g.count_live_neighbours(1, 1), 8)
        g.next_generation()

    def test_method_set_cell(self):
        g = gol.Gameoflife(5, 5)
        g.set_cell(0, 0, False)
        self.assertFalse(g.is_alive(0, 0))
        g.set_cell(0, 0, True)
        self.assertTrue(g.is_alive(0, 0))
        

if __name__ == '__main__':
    unittest.main()
