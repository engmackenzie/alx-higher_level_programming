#!/usr/bin/python3
"""Square module"""


class Square:
    """defines a square with private instance attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: Length of the side of a square
            position: position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter - sets the value of size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter - sets the value of size"""

        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """public instance method returns current sqr area"""

        return self.__size ** 2

    def my_print(self):
        """prints the square to stdout with char #"""

        if self.__size == 0:
            print()

        if (self.__position[1] > 0):
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
