import numpy as np


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            if side_a + side_b > side_c or side_a + side_c > side_b or side_c + side_b > side_a:
                raise ValueError(f'Cant create triangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = "Triangle"

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def get_area(self):
        def pp():
            return 0.5 * (self.side_a + self.side_b + self.side_c)
        return np.sqrt(pp() * (pp() - self.side_a) * (pp() - self.side_b) * (pp() - self.side_c))

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()
