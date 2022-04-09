from math import *

class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def surface_area(self):
        area = 4 * pi * (self.radius ** 2)
        return area

    