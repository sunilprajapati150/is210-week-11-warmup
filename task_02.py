#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating class using time """

import time

# class named snapshot
class Snapshot(object):
    
    # constructer created
    def __init__(self):
        self.created = time.time()
