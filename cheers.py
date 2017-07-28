#!/usr/bin/python3
from UserInterfaceModule import UserMainInterface
"""
Filename: cheers.py
Author: Alejandro Bernal
version: 1.0
Description:
Module that has the main method. It starts the user interface.
"""


def main():
    user_interface = UserMainInterface()
    user_interface.start()

if __name__ == "__main__":
    main()
