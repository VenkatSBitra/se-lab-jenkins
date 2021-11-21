#!/usr/bin/python3

import unittest

from prog import *

class TestAdd(unittest.TestCase):
    def test_add_nums(self):
        data = [34, 23]
        result = 57
        self.assertEqual(add_nums(data[0], data[1]), result)

    def test_sub_nums(self):
        data = [34, 23]
        result = 11
        self.assertEqual(sub_nums(data[0], data[1]), result)

    def test_mul_nums(self):
        data = [34, 23]
        result = 782
        self.assertEqual(mul_nums(data[0], data[1]), result)

    def test_div_nums(self):
        data = [5, 2]
        result = 2.5
        self.assertAlmostEqual(div_nums(data[0], data[1]), result)

    def test_avg_nums(self):
        data = [1, 2, 3, 4, 5]
        result = 3
        self.assertAlmostEqual(avg_nums(data), result)


if __name__ == '__main__':
    unittest.main()