#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 04."""


# Import Python libs
import unittest


# Import user libs
import task_04


class Task04TestCase(unittest.TestCase):
    """Task 04 tests"""


    def test_tires_attr(self):
        """Tests that the tires argument exists and sets the attr."""
        tire = task_04.CustomTire(20)
        tires = [tire, tire, tire, tire]
        mycar = task_04.CustomCar(tires=tires)

        self.assertEqual(mycar.tires, tires)

    def test_maximum_miles(self):
        """Tests that the maximum_miles pseudo-private was created."""
        tire = task_04.CustomTire(20)
        self.assertEqual(tire._CustomTire__maximum_miles, 500)


if __name__ == '__main__':
    unittest.main()
