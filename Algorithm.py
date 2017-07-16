#!/usr/bin/python3
import Operations
from decimal import *
import math
class constants:
    'Holds the mathematical constants'
    pi = 0.0
    rootTow = 0.0
    def __init__(self):
        self.rootTow = calcSquareTwo()
        self.pi = calcPi()
    
    def getPi(self):
        if self.pi == 0.0:
            self.pi = calcPi()
        return self.pi
    
    def getSquareRootTwo(self):
        if self.rootTow == 0.0:
            self.rootTow = calcSquareTwo()
        return self.rootTow

def calcPi():
    inverse = 0.0
    aux = 0.0
    for i in range(3):
        aux = Operations.Factorial(4 * i)*(1103 +26390 * i)
        aux = aux / (Operations.power(Operations.Factorial(i),4) * Operations.power(396,4*i))
        inverse = inverse + aux
    inverse = Decimal(inverse) * ((2*calcSquareTwo())/9801)
    pi = Decimal(1 / inverse)
    return pi
    
def calcSquareTwo():
    auxiliar = Decimal(1.4)
    auxiliar2 = Decimal(1.5)
    serror = Decimal(0.0000000000001)
    argum = [auxiliar,auxiliar2]
    auxiliar2 = bisectionMethod(function1,argum,serror)
    if auxiliar2 == 1:
        auxiliar = argum[0]
    else:
        auxiliar = argum[1]
    serror = Decimal(0.00000000000001)
    auxiliar3 = NewtonMethod(function1,function2,auxiliar,serror)
    rootTow = Decimal(auxiliar3)
    return rootTow
    
def function1(x):
    return Decimal((Operations.power(x,2) - 2))
    
def function2(x):
    return Decimal(2*x)

    
def bisectionMethod(func,list,error):
    x1 = list[0]
    x2 = list[1]
    f1 = func(x1)
    f2 = func(x2)
    while(Operations.AbsoluteValue(x2-x1) > error):
        if((f1 < 0.0) and (f2 > 0.0)) or ((f1 > 0.0) and (f2 < 0.0)):
            aux = (x2+ x1)/2
            faux = func(aux)
            if(((f1 < 0.0) and (faux > 0.0)) or ((f1 > 0.0) and (faux < 0.0))):
                x2 = aux
                band = 1
            else:
                x1 = aux
                band = 2
    list[0]= x1
    list[1] = x2
    return band
    
def NewtonMethod(func,funcd,xi,error):
    x0 = xi
    x1 = Decimal(0.0)
    while(Operations.AbsoluteValue(x1 - x0) > error):
        if x1 != Decimal(0.0):
            x0 = x1
        x1 = x0 -(func(x0)/funcd(x0))
    return Decimal(x1)

def falsiMethod(func,list,error):
    aux2 = Decimal(list[0])
    aux = Decimal(0.0)
    while (Operations.AbsoluteValue(aux2-aux) > error):
        aux2 = aux # save the last value
        func0 = func(list[0])
        func1 = func(list[1])
        aux = func0*(list[1] - list[0])
        aux = aux / (func1 - func0)
        aux = list[0] - aux
        if(Operations.sign(func(aux),func1)):
            list[0] = aux
        else:
            list[1] = aux    
    return Decimal(aux)
        
#test for operations
test = raw_input("desea salir y/n ")
pi = 0.0
rootTow = 0.0
aux = constants()
while(str(test) != "y"):
    print("the result of algorithm \n")
    print(str(aux.getPi()))
    test = raw_input("desea salir y/n ")