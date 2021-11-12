from actions_with_linked_list import *
from some_valid import *
import abc


class Strategy(LinkedList):
    @abc.abstractmethod
    def generate_data(self, data: LinkedList, pos, param):
        pass


class StrategyIter(Strategy):
    def generate_data(self, data: LinkedList, pos, n):
        a, b = segment()
        for i in range(n):
            if data.iterate_elements(n, a, b, pos) is not None:
                data.insert(data.iterate_elements(n, a, b, pos), pos)
                pos += 1


class StrategyFile(Strategy):
    def generate_data(self, data: LinkedList, pos, filename):
        with open(filename, "r") as readfile:
            for elem in readfile:
                for x in elem.split():
                    a = int(x)
                    data.insert(a, pos)
                    pos += 1
        readfile.close()
