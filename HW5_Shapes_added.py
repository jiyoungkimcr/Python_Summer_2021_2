'''
Please use the Shape structures and extend it by:
1. adding a Triangle and EquilateralTriangle - they may inherit from each other
2. adding perimeter calculation to every structure
3. adding a Square that inherits from Rectangle and uses its calc_surface implementation
4. providing some code that tests the new functionality and structures
Code writer: Jiyoung Kim
'''

class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

    def calc_perims(self):
        return (self._a + self.b) * 2

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def calc_perims(self):
        return self._a * math.pi * 2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))


# Added part
class Triangle(Shape):
    def __init__(self, a, b, c):
       self.set_params(a, b, c)

    def set_params(self, a, b, c):
        self._a = a
        self.b = b
        self.c = c

    def calc_surface(self):
        s = (self._a + self.b + self.c) / 2
        return (s*(s-self._a)*(s-self.b)*(s-self.c)) ** 0.5

    def calc_perims(self):
        return self._a + self.b + self.c

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + ", " + str(self.b) + ", " + str(self.c)+ "] at " +str(hex(id(self)))


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        self.set_params(a)

    def set_params(self, a):
        self._a = a

    def calc_surface(self):
        s = (self._a + self._a + self._a) / 2
        return (s*(s-self._a)*(s-self._a)*(s-self._a)) ** 0.5

    def calc_perims(self):
        return self._a * 3

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + ", " + str(self._a) + ", " + str(self._a) + "] at " +str(hex(id(self)))


class Square(Rectangle):
    def __init__(self, a):
        self._a = a
        self.b = a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + "] at " + str(hex(id(self)))

a = None

r = Rectangle(5, 6)
print(r)
print('Surface is: ' + str(r.calc_surface()))
print('Perimeter is: ' + str(r.calc_perims()))
print('--------------' + '\n')

c = Circle(7)
print(c)
print('Surface is: ' + str(c.calc_surface()))
print('Perimeter is: ' + str(c.calc_perims()))
print('--------------' + '\n')

t = Triangle(8,6,5)
print(t)
print('Surface is: ' + str(t.calc_surface()))
print('Perimeter is: ' + str(t.calc_perims()))
print('--------------' + '\n')

et = EquilateralTriangle(5)
print(et)
print('Surface is: ' + str(et.calc_surface()))
print('Perimeter is: ' + str(et.calc_perims()))
print('--------------' + '\n')

s = Square(6)
print(s)
print('Surface is: ' + str(s.calc_surface()))
print('Perimeter is: ' + str(s.calc_perims()))