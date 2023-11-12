
class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError(f'Cant create circle')
        self.radius = radius
        self.name = "Circle"

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        return 6.28 * self.radius

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()