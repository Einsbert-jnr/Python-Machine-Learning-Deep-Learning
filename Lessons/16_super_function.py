class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.height = height
        super().__init__(length, width)

    def volume(self):
        return self.length * self.width * self.height


square = Square(2, 4)
cube = Cube(2, 2, 2)

print(f"Area: {square.area()}\n Volume: {cube.volume()}")