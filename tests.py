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


if __name__ == '__main__':
    unittest.main()
