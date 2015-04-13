#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests Task 02."""


# Import Python libs
import time
import unittest


# Import user libs
import task_02


class Task02TestCase(unittest.TestCase):
    """Task 02 tests"""


    def test_snapshot(self):
        """Tests that the snapshot class exists."""
        snapshot = task_02.Snapshot()
        self.assertIsInstance(snapshot, task_02.Snapshot)


    def test_snapshot_created(self):
        """Tests that the created attribute of snapshot exists."""
        snap = task_02.Snapshot()
        self.assertTrue(hasattr(snap, 'created'))


    def test_snapshot_instance_attr(self):
        """Tests that created only exists within instanced Snapshots"""
        self.assertFalse(hasattr(task_02.Snapshot, 'created'))


if __name__ == '__main__':
    unittest.main()
