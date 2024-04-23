class Circle:
    def __init__(self, radius):
        self.radius = radius

    def square(self):
        return 3.141 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.141 * self.radius


a = Circle(5)
print(f'Площадь: {a.square()}\nПериметр: {a.perimeter()}')
