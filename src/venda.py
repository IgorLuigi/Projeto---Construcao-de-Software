import math

class Dinheiro():

    def __init__(self, value=0.0, decimals=2, coin_name='R$', method='arredondar'):
        self.decimals = decimals
        self.coin_name = coin_name
        self.value = self.handle_value(value, decimals, method)


    @staticmethod
    def handle_value(value, decimals, method='arredondar'):
        if(method == 'arredondar'):
            return round(value, decimals)
        elif(method == 'truncar' or method == 'andar'):
            multiplier = pow(10, decimals)
            value_int = int(value * multiplier)
            return float(value_int/multiplier)
        elif(method == 'arredondarcima'):
            multiplier = pow(10, decimals)
            value_int = int(value * (10 * multiplier))

            if(value_int%10 != 0):
                value_int+=10
            value_int = int(value_int/10)
            return float(value_int/multiplier)


    def applyRound(self, decimals, method='arredondar'):
        self.decimals = decimals
        self.value = self.handle_value(self.value, decimals, method)


    def __add__(self, new):
        if(self.decimals < new.decimals):
            sum_decimals = new.decimals
        else:
            sum_decimals = self.decimals
        
        sum_value = self.value + new.value
        return Dinheiro(sum_value, sum_decimals)


    def __str__(self):
        return self.coin_name + str(self.dinheiro)


    def __repr__(self):
        return f"<Dinheiro {self.value}>"