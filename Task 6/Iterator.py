import random


class Iterator:
    def __iter__(self):
        return self

    def __init__(self, size, a, b, func=random.randint):
        self.size = size
        self.elem = 0
        self.a = a
        self.b = b
        self.func = func

    def __next__(self):
        if self.a > self.b:
            self.a, self.b = self.b, self.a
        if self.elem < self.size:
            self.elem += 1
        for i in range(self.size):
            self.size -= 1
            return self.func(self.a, self.b)
        else:
            raise StopIteration


def generator(a, b, size):
    while size != 0:
        size -= 1
        yield random.randint(a, b)
