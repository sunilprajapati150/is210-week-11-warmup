#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains the car class."""


class Car(object):
    """A moving vehicle definition."""

    def __init__(self, color='red'):
        """Constructor for the Car() class.

        Args:
            color (string): The color of the car. Defaults to ``'red'``.

        Attributes:
           color (string): The color of the car.
        """
        self.color = color


class Tire(object):
    """A round rubber thing."""

    def __init__(self, miles=0):
        """Constructor for the Tire() class.

        Args:
            miles (integer): The number of miles on the Tire. Defaults to 0.

        Attributes:
           miles (integer): The number of miles on the Tire.
        """
        self.miles = miles

    def add_miles(self, miles):
        """Increments the tire mileage by the specified miles.

        Args:
            miles (integer): The number of miles to add to the tire.
        """
        self.miles += miles
