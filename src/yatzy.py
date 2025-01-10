from src.pips import Pips 

class Yatzy:

    FAIL = 0
    MAX_POINTS = 50

    def __init__(self, d1=0, d2=0, d3=0, d4=0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    
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
        pairs_points = [0]
        for die in dice:
            if dice.count(die) > 1:
                pairs_points.append(die * 2)
        return max(pairs_points)

    @staticmethod
    def two_pair(*dice):
        dice_uncounted = list(dice)
        pairs_points = []
        for die in dice:
            if dice_uncounted.count(die) > 1:
                pairs_points.append(die * 2)
                dice_uncounted.remove(die)
                dice_uncounted.remove(die)
        return sum(pairs_points) if len(pairs_points) == 2 else 0 

    @staticmethod
    def four_of_a_kind(*dice):
        for die in dice:
            if dice.count(die) > 3:
                return die * 4
        return Yatzy.FAIL

    @staticmethod
    def three_of_a_kind(*dice):
        for die in dice:
            if dice.count(die) > 2:
                return die * 3
        return Yatzy.FAIL

    @staticmethod
    def small_straight(*dice):
        return 15 if tuple(set(dice)) == (1, 2, 3, 4, 5) else Yatzy.FAIL

    @staticmethod
    def large_straight(*dice):
        return 20 if tuple(set(dice)) == (2, 3, 4, 5, 6) else Yatzy.FAIL
  
    @staticmethod
    def full_house(*dice):
        return sum(dice.count(die) * die for die in set(dice) if (dice.count(die) == 2 or dice.count(die) == 3) and len(set(dice)) == 2)