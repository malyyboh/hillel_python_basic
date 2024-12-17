class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    def __add__(self, other):
        new_square = self.get_square() + other.get_square()
        width = self.get_square()
        height = new_square / width
        return Rectangle(width, height)

    def __mul__(self, n):
        width = self.get_square()
        height = n
        return Rectangle(width, height)

    def __str__(self):
        return f"Прямокутник з шириною {self.width} і висотою {self.height} має площу {self.get_square()}"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert r3.get_square() == 26, 'Test3'

r4 = r1 * 4
assert r4.get_square() == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'