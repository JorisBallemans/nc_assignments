from enum import Enum

class Strategy(Enum):
    COOPERATIVE = 1
    DOMINANT = 2
    GREEDY = 3

    def __str__(self):
        return self.name.lower()