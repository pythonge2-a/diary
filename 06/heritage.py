

from math import pi 

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 0
        self.name = 'shape'

    def move(self, deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY

    def rotate(self, angle):
        self.angle += angle

    def area(self):
        pass

    def __str__(self):
        return f"{self.name}(x: {self.x} y: {self.y}"
    
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        self.name = 'circle'

    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f"{self.name}(x: {self.x} y: {self.y} radius: {self.radius})"
    
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.name = 'rectangle'

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"{self.name}(x: {self.x} y: {self.y} width: {self.width} height: {self.height})"
    
class Square(Rectangle):
    def __init__(self, x, y, side):
        super().__init__(x, y, side, side)
        self.name = 'square'

    def __str__(self):
        return f"{self.name}(x: {self.x} y: {self.y} side: {self.width})"
    
class Triangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height
        self.name = 'triangle'

    def area(self):
        return self.base * self.height / 2

    def __str__(self):
        return f"{self.name}(x: {self.x} y: {self.y} base: {self.base} height: {self.height}")