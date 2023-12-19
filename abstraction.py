# Abstraction (Class definition)
class Shape:
    def area(self):
        pass


# Implementation (Subclasses implementing the abstraction)
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


# Using the implemented classes
square = Square(5)
circle = Circle(3)

print("Square Area:", square.area())  
print("Circle Area:", circle.area())  
