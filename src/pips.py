from enum import Enum, unique

@unique
class Pips(Enum):

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @staticmethod
    def values():
        return {number._value_ for number in Pips.__members__.values()}

if __name__ == "__main__":
    print(Pips.values())
    print(dir(Pips))
    print(list(Pips))
