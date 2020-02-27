#!/usr/bin/env python

import unittest
import task


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def testCircleArea(self):
        expected = 28.27431
        self.assertAlmostEqual(expected, task.circleArea(3), None, None, 0.01)

    def testFirstLast(self):
        expected = [1, 9]
        self.assertListEqual(expected, task.firstLast([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def testDateDifference(self):
        expected = 10
        self.assertEqual(expected, task.dateDifference("2020-1-1", "2020-1-11"))


if __name__ == '__main__':
    unittest.main()
