import math
class circle():
    def __init__ (self, radius):
        self.radius = radius

    def circumference(self):
        circumference = self.radius * 2 * math.pi
        print (circumference)

circle1 = circle(10)

circle1.circumference()