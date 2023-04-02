class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Membuat objek Rectangle dan Circle
rect = Rectangle(4, 5)
cir = Circle(2)

# Memanggil method area() pada objek Rectangle dan Circle
print("Luas Rectangle: ", rect.area())
print("Luas Circle: ", cir.area())
