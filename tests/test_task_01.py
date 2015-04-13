#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 01."""


# Import Python libs
import unittest


# Import user libs
import produce
import task_01


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""


    def test_tomato_is_produce(self):
        """Tests TOMATO is an instance of Produce()"""
        self.assertIsInstance(task_01.TOMATO, produce.Produce)


    def test_eggplant_is_produce(self):
        """Tests TOMATO is an instance of Produce()"""
        self.assertIsInstance(task_01.EGGPLANT, produce.Produce)


    def test_tomato_arrival_value(self):
        """Tests that TOMATO_ARRIVAL is the same as what is found in the
        TOMATO instance"""
        self.assertEqual(task_01.TOMATO_ARRIVAL, task_01.TOMATO.arrival)


    def test_eggplant_expires_value(self):
        """Tests that EGGPLANT_EXPIRES is the same as what is found in the
        EGGPLANT instance"""
        self.assertEqual(task_01.EGGPLANT_EXPIRES,
                         task_01.EGGPLANT.get_expiration())


if __name__ == '__main__':
    unittest.main()
