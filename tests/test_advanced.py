# -*- coding: utf-8 -*-

from .context import gameoflife

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(gameoflife.glossy_grid())


if __name__ == '__main__':
    unittest.main()
