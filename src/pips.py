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
    def values(*numbers_to_exlude):
        """
        Returns a set of Pips values excluding the specified numbers.
        Args:
            *numbers: Variable length argument list of numbers to exclude.
        Returns:
            set: A set of Pips values excluding the specified numbers.
        """

        return {number._value_ for number in Pips.__members__.values()} - set(numbers_to_exlude)

    '''
    @classmethod
    def remove_from_values(cls, *numbers):
        return cls.values() - set(numbers)
    '''
if __name__ == "__main__":
    print(Pips.values())
    print(dir(Pips))
    print(list(Pips))
