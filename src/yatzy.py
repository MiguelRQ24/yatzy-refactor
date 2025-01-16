from src.pips import Pips 

class Yatzy:

    FAIL = 0
    MAX_POINTS = 50
    SMALL_STRAIGHT_NUMBERS = Pips.values(6)
    LARGE_STRAIGHT_NUMBERS = Pips.values(1)

    @staticmethod
    def chance(*dice):
        return sum(dice)
    '''
    En vez de sumarlos uno a uno los sumamos a la vez
    con la funcion sum()
    '''

    @staticmethod
    def yatzy(*dice):
        return Yatzy.MAX_POINTS if len(set(dice)) == 1 else Yatzy.FAIL
    '''
    Reduces la lista de dados eliminando las repeticiones de un mismo numero,
    y si la longitud despues de eso es uno entonces son los 5 dados iguales y te da 50 puntos si no 0
    '''

    @staticmethod
    def __sum_one_number(dice: tuple, number):
        return dice.count(number) * number 
    
    @classmethod
    def ones(cls, *dice):
        return cls.__sum_one_number(dice, Pips.ONE.value)  
    '''
    Bucle para sumar unidad por cada resultado igual a 1
    '''
    @classmethod
    def twos(cls, *dice):
        return cls.__sum_one_number(dice, Pips.TWO.value)
    '''
    Bucle para sumar unidad por cada resultado igual a 2
    '''  

    @classmethod
    def threes(cls, *dice):
        return cls.__sum_one_number(dice, Pips.THREE.value)
    '''
    Bucle para sumar unidad por cada resultado igual a 3
    '''  

    @classmethod
    def fours(cls, *dice):
        return cls.__sum_one_number(dice, Pips.FOUR.value)
    '''
    Bucle para sumar unidad por cada resultado igual a 4
    '''  
    
    @classmethod
    def fives(cls, *dice):
        return cls.__sum_one_number(dice, Pips.FIVE.value)
    '''
    Bucle para sumar unidad por cada resultado igual a 5
    ''' 

    @classmethod
    def sixes(cls, *dice):
        return cls.__sum_one_number(dice, Pips.SIX.value)
    '''
    Bucle para sumar unidad por cada resultado igual a 6
    '''

    def score_pair(*dice):
        return max(die * 2 if dice.count(die) > 1  else 0 for die in dice)

    @staticmethod
    def two_pair(*dice):
        pairs = [die * 2 for die in set(dice) if dice.count(die) >= 2]
        return sum(pairs) if len(pairs) == 2 else Yatzy.FAIL
        
    @staticmethod
    def four_of_a_kind(*dice):
        return sum(die * 4 for die in set(dice) if dice.count(die) > 3)

    @staticmethod
    def three_of_a_kind(*dice):
        return sum(die * 3 for die in set(dice) if dice.count(die) > 2)

    @staticmethod
    def small_straight(*dice):
        return 15 if set(dice) == Yatzy.SMALL_STRAIGHT_NUMBERS else Yatzy.FAIL

    @staticmethod
    def large_straight(*dice):
        return 20 if set(dice) == Yatzy.LARGE_STRAIGHT_NUMBERS else Yatzy.FAIL
  
    @staticmethod
    def full_house(*dice):
        return sum(dice.count(die) * die for die in set(dice) if (4 > dice.count(die) > 1) and len(set(dice)) == 2)
    