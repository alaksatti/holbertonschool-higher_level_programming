#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Unit test """
    def test_max_int(self):
        """
        Returns max_integer
        """
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([3, 4, 5, 6]), 6)
        self.assertEqual(max_integer([-1, -5, -9, -7]), -1)
        self.assertEqual(max_integer([0, 1, 2, 1, 0]), 2)
        self.assertEqual(max_integer([10, 9, 8, 7]), 10)
        self.assertEqual(max_integer(), None)
if __name__ == '__main__':
    unittest.main()
