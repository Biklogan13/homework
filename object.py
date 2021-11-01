class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def print(self):
        print('(', str(self.x), ',', str(self.y), ',', str(self.z), ')')

a = Vector(1, 2, 3)
a.print()

b = Vector(3, 5, 7)
b.print()

c = a + b
c.print()

d = c * 3
d.print()