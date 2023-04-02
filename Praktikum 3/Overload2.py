class Shape:
    @staticmethod
    def get_area(length, breadth):
        return length * breadth

class Circle:
    @staticmethod
    def get_area(radius):
        return 3.14 * (radius ** 2)

print("Luas persegi panjang dengan panjang 4 dan lebar 5: ", Shape.get_area(4, 5))
print("Luas lingkaran dengan jari-jari 2: ", Circle.get_area(2))
