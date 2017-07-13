#!/usr/bin/python3
from Operations import Operation
from decimal import *
import math
class Algorithm:
    'Class Algorithm has the implementation of the different functions and constants as pi'
    __pi = 0.0
    __rootTow = 0.0
    __result = 0.0

    def calcPi():
        if Algorithm.__pi != 0.0:
            return Algorithm.__pi
        inverse = 0.0
        aux = 0.0
        for i in range(3):
            aux = Operation.Factorial(4 * i)*(1103 +26390 * i)
            aux2 =  (Operation.power(Operation.Factorial(i),4) * Operation.power(396,4*i))
            aux3 = aux / aux2
            inverse = inverse + aux3
        inverse = inverse * ((2*math.sqrt(2))/9801)
        getcontext().prec = 24
        Algorithm.__pi = Decimal(1 / inverse)
        return Algorithm.__pi
    calcPi = staticmethod(calcPi)
    
    def calcSquareTwo():
        if Algorithm.__rootTow
        return
    
#test for operations
test = raw_input("desea salir y/n ")
while(str(test) != "y"):
    print("the result of algorithm \n")
    print(str(Algorithm.calcPi()))
    test = raw_input("desea salir y/n ")