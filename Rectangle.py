class Figure:

    def get_area(self):
        pass

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.get_area()+other_figure.get_area()
        raise ValueError(f'Object {other_figure} is not figure')


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f'Cant create rectangle')
        self.side_a = side_a
        self.side_b = side_b
        self.name = "Rectangle"

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()

class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError(f'Cant create square')
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.name = "Square"