#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 03."""


# Import Python libs
import unittest


# Import user libs
import produce
import task_03


class Task03TestCase(unittest.TestCase):
    """Task 03 tests"""

    def test_apple_subclassed_produce(self):
        """Tests that the Apple class is subclassed from Produce"""
        self.assertTrue(issubclass(task_03.Apple, produce.Produce))

    def test_apple_duration(self):
        """Tests that Apple.duration has the correct value."""
        self.assertEqual(task_03.Apple.duration, 5356800)

    def test_produce_duration(self):
        """Tests that Produce.duration remains unchanged"""
        self.assertEqual(produce.Produce.duration, 604800)


if __name__ == '__main__':
    unittest.main()
