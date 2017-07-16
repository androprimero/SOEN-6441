#!/usr/bin/python3
'Module with common operations'
result = 0
DictFactorial ={ 0: 1,1:1}

def power(base, exponent):
      if exponent == 0:
            return 1
      else:
            aux = power(float(base), int(exponent/2))
            if exponent % 2 == 0:
                  return  aux * aux 
            else:
                  return base * aux * aux

def Factorial(number):
      if(DictFactorial.has_key(number)):
            return DictFactorial.get(number)
      else:
            DictFactorial[number] = number * Factorial(number-1)
            return DictFactorial[number]
      
def AbsoluteValue(number):
      if(number > 0):
            return number
      else:
            return (-1* number)

def sign(number1,number2):
      if((number1 < 0 and number2 < 0) or (number1>0 and number2>0)):
            return True
      else:
            return False