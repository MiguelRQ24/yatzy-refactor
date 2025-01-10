
def sum_number(dice, number):
    return sum(number for die in dice if die == number)  

class Yatzy:

    @staticmethod
    def chance(*dice):
        return sum(dice)
    '''
    En vez de sumarlos uno a uno los sumamos a la vez
    con la funcion sum()
    '''

    @staticmethod
    def yatzy(*dice):
        return 50 if len(set(dice)) == 1 else 0
    '''
    Reduces la lista de dados eliminando las repeticiones de un mismo numero,
    y si la longitud despues de eso es uno entonces son los 5 dados iguales y te da 50 puntos si no 0
    '''

    @staticmethod
    def ones(*dice):
        return sum_number(dice, 1)  
    '''
    Bucle para sumar unidad por cada resultado igual a 1
    '''
    @staticmethod
    def twos(*dice):
        return sum_number(dice, 2)
    '''
    Bucle para sumar unidad por cada resultado igual a 2
    '''  

    @staticmethod
    def threes(*dice):
        return sum_number(dice, 3)
    '''
    Bucle para sumar unidad por cada resultado igual a 3
    '''  


    def __init__(self, d1=0, d2=0, d3=0, d4=0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    def fours(*dice):
        return sum_number(dice, 4)
    '''
    Bucle para sumar unidad por cada resultado igual a 4
    '''  
    def fives(*dice):
        return sum_number(dice, 5)
    '''
    Bucle para sumar unidad por cada resultado igual a 5
    ''' 

    def sixes(*dice):
        return sum_number(dice, 6)
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
    def four_of_a_kind(_1, _2, d3, d4, d5):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1, d2, d3, d4, d5):
        t = [0] * 6
        t[d1 - 1] += 1
        t[d2 - 1] += 1
        t[d3 - 1] += 1
        t[d4 - 1] += 1
        t[d5 - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[d1 - 1] += 1
        tallies[d2 - 1] += 1
        tallies[d3 - 1] += 1
        tallies[d4 - 1] += 1
        tallies[d5 - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0