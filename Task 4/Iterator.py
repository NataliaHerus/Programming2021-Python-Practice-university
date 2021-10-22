from random import randint
from some_valid import input_element


class Iterator:
    def __iter__(self):
        return self

    def __init__(self, size):
        self.size = size
        self.elem = 0

    def __next__(self):
        if self.elem < self.size:
            self.elem += 1
        for i in range(self.size):
            self.size -= 1
            return input_element()
        else:
            raise StopIteration


def generator(a, b, size):
    while size != 0:
        size -= 1
        yield randint(a, b)

