# Dunder -> __x__
import math


class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Readable description of the object"

    def __repr__(self):
        return f"Unambiguous description for developers"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


class MyContainer:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        del self.items[key]


class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class ComplexNumber:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.im + other.im)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.im - other.im)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise Exception('Only pass in Vector object')
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise Exception('Only pass in Vector object')
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector X: {self.x}, Y: {self.y}"

    def __len__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __call__(self, *args, **kwargs):
        print("Vector called, returning x and y")
        return self.x, self.y

