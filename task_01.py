#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Instating and accessing custom classes instances"""

import produce

# instances for the produce
TOMATO = produce.Produce()
TOMATO_ARRIVAL = TOMATO.arrival

# accessing the attribute
EGGPLANT = produce.Produce(1311210802)
EGGPLANT_EXPIRES = EGGPLANT.get_expiration()
