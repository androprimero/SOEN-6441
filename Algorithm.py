#!/usr/bin/python3
import Operations
from decimal import Decimal
# import pdb
"""
Filename: Algorithm.py
Author: Alejandro Bernal
version: 1.0
Description:
Module that has the algorithms used to approximate roots of functions.
Include: Bisection method, Regula-Falsi method and Newton Method.
"""


class Constants:
    """Holds the mathematical constants"""
    pi = Decimal(0.0)
    rootTow = Decimal(0.0)

    def __init__(self):
        """
        Create an object Constants
        """
        self.rootTow = calculate_square_two()
        self.pi = calculate_pi(self.get_square_root_two())
        # pdb.set_trace()

    def get_pi(self):
        """
        Computes the value of  pi if it was not computed before
        :return: the value of the constant pi
        """
        if self.pi == Decimal(0.0):
            self.pi = calculate_pi()
        return self.pi

    def get_square_root_two(self):
        """
        Computes the value of  Square root of two if it was not computed before
        :return: the value of the constant Square root of two
        """
        if self.rootTow == Decimal(0.0):
            self.rootTow = calculate_square_two()
        return self.rootTow


def calculate_pi(square_root_two):
    """
    computes the value of pi
    :return: pi
    """
    inverse = Decimal(0.0)
    for i in range(3):
        auxiliary = Decimal(Operations.factorial(4 * i) * (1103 + 26390 * i))
        auxiliary = auxiliary / (Decimal(Operations.power(
            Operations.factorial(i), 4) * Operations.power(396, 4 * i)))
        inverse = inverse + auxiliary
    inverse = inverse * Decimal(((2 * square_root_two) / 9801))
    pi = Decimal(1 / inverse)
    return pi


def calculate_square_two():
    """
    computes the square root of two
    :return: square root of two
    """
    auxiliary = Decimal(1.4)
    auxiliary_2 = Decimal(1.5)
    s_error = Decimal(0.0000000000001)
    arguments = [auxiliary, auxiliary_2]
    auxiliary_2 = bisection_method(function1, arguments, s_error)
    if auxiliary_2 == 1:
        auxiliary = Decimal(arguments[0])
    else:
        auxiliary = Decimal(arguments[1])
    s_error = Decimal(0.00000000000001)
    auxiliary_3 = newton_method(function1, function2, auxiliary, s_error)
    root_two = Decimal(auxiliary_3)
    return root_two


def function1(x):
    """
    Function x^2 -2
    :param x:
    :return:
    """
    return Decimal(Operations.power(x, 2) - 2)


def function2(x):
    """
    Function 2*x
    :param x:
    :return:
    """
    return Decimal(2 * x)


def bisection_method(function, list, error):
    """
    Bisection method
    :param function: function to find the root
    :param list: interval in which should be a root
    :param error: evaluate the error of iterations
    :return: approximation to the root of function
    """
    x1 = Decimal(list[0])
    x2 = Decimal(list[1])
    f1 = Decimal(function(x1))
    f2 = Decimal(function(x2))
    while Operations.absolute_value(x2 - x1) > error:
        if not Operations.sign(f1, f2):
            auxiliary = Decimal((x2 + x1) / 2)
            function_auxiliary = Decimal(function(auxiliary))
            if not Operations.sign(f1, function_auxiliary):
                x2 = Decimal(auxiliary)
                flag = 1
            else:
                x1 = Decimal(auxiliary)
                flag = 2
        else:
            return 0
    list[0] = Decimal(x1)
    list[1] = Decimal(x2)
    return flag


def newton_method(function, function_derivative, xi, error):
    """
    Newton's Method
    :param function: function to be evaluated
    :param function_derivative: derivative of the function
    :param xi: x initial
    :param error: error to evaluate the change of iterations
    :return:
    """
    x0 = Decimal(xi)
    x1 = Decimal(0.0)
    local_error = Decimal(error)
    previous_error = Decimal(Operations.absolute_value(x1 - x0))
    last_error = Decimal(0.0)
    # if the error increases the algorithm will diverge
    while (previous_error > local_error) and (last_error < previous_error):
        auxiliary = Decimal(function_derivative(x0))
        if auxiliary != 0.0:
            x1 = Decimal(x0 - (function(x0) / auxiliary))
        else:
            # return the last x1 that was sucessfully calulated
            return Decimal(x1)
        last_error = Decimal(previous_error)
        previous_error = Decimal(Operations.absolute_value(x1 - x0))
        x0 = Decimal(x1)
    # if the error increases the last calulation was not good,
    # so the function sends the previus one
    if previous_error > local_error:
        x1 = Decimal(x0)
    return x1


def falsi_method(function, list, error):
    """
    Regula Falsi method
    :param function: function to be evaluated
    :param list: interval to find the root
    :param error: error to evaluate the change of iterations
    :return:
    """
    auxiliary_2 = Decimal(list[0])
    x0 = Decimal(list[0])
    x1 = Decimal(list[1])
    auxiliary = Decimal(0.0)
    while Operations.absolute_value(auxiliary_2 - auxiliary) > error:
        auxiliary_2 = Decimal(auxiliary)  # save the last value
        function0 = Decimal(function(x0))
        function1 = Decimal(function(x1))
        auxiliary = Decimal(function0 * (x1 - x0))
        auxiliary = auxiliary / Decimal(function1 - function0)
        auxiliary = x0 - auxiliary
        if Operations.sign(function(auxiliary), function1):
            x0 = Decimal(auxiliary)
        else:
            x1 = Decimal(auxiliary)
    list[0] = Decimal(x0)
    list[1] = Decimal(x1)
    return Decimal(auxiliary)
