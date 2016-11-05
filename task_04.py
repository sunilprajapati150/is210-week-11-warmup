#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Using subclass to demonstrate has-a and is-a concepts"""

import car

# class of car.Car
class CustomCar(car.Car):
  
    def __init__(self, tires=None):
      
        self.tires = tires
        car.Car.__init__(self, tires)
        self.tires = tires
        tires = CustomTire()
        
# instance attribut to store the list of tires
        if self.tires is None:
            self.tires = []
            while len(self.tires) < 4:
                self.tires.append(tires)

# psudo-private class attribute added and value assigned to 500
class CustomTire(car.Tire):
  
    __maximum_miles = 500
