#класс есть абстракция, которая создаёт объект, описание
class rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b
    def print_me(self, c):
        print(self.side_a + c)

#вот так создаётся объект
print(rectangle)
#r - реальный объект
r1 = rectangle(2, 10)
#здесь работает позднее связывание. в скобки автоматом подставляется r
r.print_me(20)
