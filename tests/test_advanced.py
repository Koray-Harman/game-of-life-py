# -*- coding: utf-8 -*-

from .context import gameoflife as gol

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_exists(self):
        self.assertIsNotNone(gol.Gameoflife(10,10))

    def test_exists_zero(self):
        self.assertIsNotNone(gol.Gameoflife(0,0))


if __name__ == '__main__':
    unittest.main()
