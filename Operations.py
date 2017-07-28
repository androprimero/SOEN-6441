#!/usr/bin/python3
from decimal import Decimal
"""
Filename: Operations.py
Author: Alejandro Bernal
version: 1.0
Description:
Module that has the arithmetic and trigonometric operations.
"""
result = 0
DictFactorial = {0: 1, 1: 1}


def power(base, exponent):
    """
    Computes the power base^exponent
    :param base:
    :param exponent:
    :return:
    """
    if exponent == 0:
        return 1
    else:
        aux = Decimal(power(Decimal(base), int(exponent / 2)))
        if int(exponent) % 2 == 0:
            return aux * aux
        else:
            return base * aux * aux


def factorial(number):
    """
    computes the factorial of a number
    :param number:
    :return:
    """
    if number in DictFactorial:
        return DictFactorial.get(number)
    else:
        # base case are in DictFactorial from beginning
        DictFactorial[number] = number * factorial(number - 1)
        return Decimal(DictFactorial[number])


def absolute_value(number):
    """
    Computes the absolute value of a number
    :param number:
    :return:
    """
    if number > 0:
        return number
    else:
        return -1 * number


def sign(number1, number2):
    """
    compares the sign of number1 with the sign of number2
    :param number1:
    :param number2:
    :return: True if both have the same sign else return false
    """
    if (number1 < 0 and number2 < 0) or (number1 > 0 and number2 > 0):
        return True
    else:
        return False


def sin(number):
    """
    computes the sine of number
    :param number:
    :param x:
    :return: sine of the number
    """
    n = 0
    x = Decimal(number)
    sine = Decimal(0)
    signed = Decimal(1)
    while n < 60:
        auxiliary = signed * Decimal(power(x, 2 * n + 1))
        auxiliary2 = Decimal(factorial(2 * n + 1))
        sine = sine + (auxiliary/auxiliary2)
        signed = signed * -1
        n = n + 1
    return Decimal(sine)


def cos(number):
    """
    computes the cosine of number
    :param number:
    :param x:
    :return: cosine of the number
    """
    n = 0
    cosine = Decimal(number * 0)
    x = Decimal(number)
    signed = Decimal(1)
    while n < 60:
        auxiliary = signed * Decimal(power(x, 2 * n))
        auxiliary2 = Decimal(factorial(2*n))
        cosine = cosine + (auxiliary/auxiliary2)
        signed = signed * -1
        n = n + 1
    return Decimal(cosine)
