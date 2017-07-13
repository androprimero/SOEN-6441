#!/usr/bin/python3
class Operation:
    'Class with some basic operation functions'
    result = 0
    DictFactorial ={ 0: 1,1:1}
    def __init__(self):
        result = 0

    def power(base, exponent):
        if exponent == 0:
            return 1
        else:
            aux = Operation.power(float(base), int(exponent/2))
            if Operation.module_number(float(exponent), 2) == 0:
                return  aux * aux 
            else:
                return base * aux * aux
    power = staticmethod(power)

    def module_number(dividend, divisor):
        auxiliar = float(dividend) / float(divisor)
        auxiliar2 = int(auxiliar)
        auxiliar = auxiliar - auxiliar2
        result = int(auxiliar * divisor)
        return result
    module_number = staticmethod(module_number)
    def Factorial(number):
        if(Operation.DictFactorial.has_key(number)):
            return Operation.DictFactorial.get(number)
        else:
            Operation.DictFactorial[number] = number * Operation.Factorial(number-1)
            return Operation.DictFactorial[number]
    Factorial = staticmethod(Factorial)