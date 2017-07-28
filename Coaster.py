#!/usr/bin/python3
from Algorithm import Constants
import Algorithm
import Operations
from decimal import * 
"""
Filename: Coasters.py
Author: Alejandro Bernal
version: 1.0
Description:
Module that contains coaster class, which holds the radius of the coasters and compute the length. To compute
the length it uses Algorithm.py, Constant class and Operation.py.
"""

class Coasters:
    constants = Constants
    radius = Decimal(0.0)

    def __init__(self):
        """
        Create a new coaster
        """
        self.constants = Constants()
        self.radius = Decimal(0.0)
        self.alpha = Decimal(0.0)
        self.length = Decimal(0.0)

    def __str__(self):
        string = "Radius = " + str(self.radius) + "\n Length = " + str(self.length)
        string = string + " \n Pi = " + str(self.constants.get_pi()) + "\n alpha = " + str(self.alpha) +".\n"
        return string
    
    def set_radius(self, radius):
        """
        Set the Radius of each coaster
        :type radius: Decimal
        """
        if radius < 0:
            return False
        else:
            self.radius = Decimal(radius)
            return True

    def get_radius(self):
        """
        Return the Radius of each coaster
        :return: Radius
        """
        return self.radius

    def function_alpha(self, number):
        """
        Function that defines alpha angle.
        :param number: Decimal of the number that will compute the function
        :return: number - sine(number) - pi/2
        """
        x = Decimal(number)
        return Decimal(x - Operations.sin(x) - ((self.constants.get_pi())/2))
    
    def derivate_function_alpha(self, number):
        """
        Function that is the derivative of alpha function.
        :param number: Decimal of the number that will compute the function        
        :return: 1 + cosine(number)
        """
        x = Decimal(number)
        return Decimal(1) + Operations.cos(x)

    def calculate_length(self):
        """
        Function that compute the length between the coasters centers.
        :return: Decimal of the length
        """
        self.length = 2 * self.get_radius()*(1 - Operations.cos(self.alpha / 2))
        return self.length

    def get_length(self):
        """
        Return the length between each coaster center
        :type length: Decimal
        """
        return self.length

    def calculate_alpha(self):
        """
        Compute the value of alpha using the algorithms Bisection and Newton methods
        :return: approximation of alpha
        """
        x1 = Decimal(2.0)
        x2 = Decimal(3.0)
        interval = [x1, x2]
        error = Decimal(0.000000000000000000001)
        flag = Algorithm.bisection_method(self.function_alpha, interval, error)
        if flag != 0:
            if flag == 1:
                x1 = interval[0]
            else:
                x1 = interval[1]
        self.alpha = Algorithm.newton_method(self.function_alpha, self.derivate_function_alpha, x1, error)
        return self.alpha
