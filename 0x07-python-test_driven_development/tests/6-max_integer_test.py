#!/usr/bin/python3
"""Unit test for max_integer(list=[]) function"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class test_max_integer(unittest.TestCase):
    """Define the unittests for the function max_integer(list=[])"""

    def test_max_at_beg(self):
        max_at_beg = [15, 14, 13, 12, 11]
        self.assertEqual(max_integer(max_at_beg), 15)

    def test_sorteD_list(self):
        sorteD = [11, 13, 17, 20, 25]
        self.assertEqual(max_integer(sorteD), 25)

    def test_unsorteD_list(self):
        unsorteD = [50, 97, 35, 100, 10]
        self.assertEqual(max_integer(unsorteD), 100)

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_floats_list(self):
        floats = [1.24, 2.36, 8.65, -13.0]
        self.assertEqual(max_integer(floats), 8.65)

    def test_string(self):
        string = "Holberton to Alx"
        self.assertEqual(max_integer(string), 'x')

    def test_string_empty(self):
        self.assertEqual(max_integer(""), None)

    def test_floats_ints(self):
        floats_ints = [13, 150, -15.6, 87.32, -9]
        self.assertEqual(max_integer(floats_ints), 150)


if __name__ == '__main__':
    unittest.main()
