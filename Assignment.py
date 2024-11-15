import math

class Polygon:
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

if __name__ == "__main__":
    rectangle = Rectangle(5, 10)
    print(f"Area of Rectangle: {rectangle.area()}")

    circle = Circle(7)
    print(f"Area of Circle: {circle.area()}")

    triangle = Triangle(6, 8)
    print(f"Area of Triangle: {triangle.area()}")

    square = Square(4)
    print(f"Area of Square: {square.area()}")
