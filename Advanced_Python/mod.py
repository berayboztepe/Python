from math import sqrt


class math:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __str__(self):
        return str(self.num)

    def __sub__(self, other):
        return self.num - other.num

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num / other.num

    def __abs__(self):
        return abs(self.num)

    def __pow__(self, power, modulo=None):
        return self.num ** power.num

    def __sqrt__(self):
        return sqrt(self.num)


wel = "Welcome to my Calculator"
wel1 = "...This calculator is made with dunder methods, oop. Importing the module..."
