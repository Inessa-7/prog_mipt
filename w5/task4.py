class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Shape):
    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def area(self):
        return 0.5 * self.width * self.height


fig1 = Rectangle(5, 7)
fig2 = Triangle(12, 6)
print(fig1.area())
print(fig2.area())
