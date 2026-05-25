

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2
    def is_square(self):
        return self.width == self.height


rec = Rectangle(3, 5)
print(rec.is_square())



















