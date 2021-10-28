from Strategy import *


class Context:

    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def generate_list(self, lst, pos, amount):
        self._strategy.generate_data(lst, pos, amount)
