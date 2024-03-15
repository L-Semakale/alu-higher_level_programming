#!/usr/bin/python3
"""
more class base
"""

Rectangle = __import__('9-rectangle').Rectangle

"""
Square class
"""
class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ Initialize Square """
        super().__init__(size, size)
        self.__size = size

    @property
    def size(self):
        """ Getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be greater than 0")
        self.__size = value

    def __str__(self):
        """ String representation of Square """
        return f"[Square] {self.__size}/{self.__size}"
