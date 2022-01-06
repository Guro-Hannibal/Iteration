from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self):
        pass

    def __total(self):
        pass


class Dress(Clothes):

    def __init__(self, v):
        super().__init__()
        self.v = v

    @property
    def total(self):
        return self.v / 6.5 + 0.5


class Smoking(Clothes):

    def __init__(self, h):
        super().__init__()
        self.h = h

    @property
    def total(self):
        return self.h * 2 + 0.3


smoking = Smoking(3311)

dress = Dress(1133)

print(dress.total)

print(smoking.total)

