#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """ Rectangle class"""
    number_of_instances = 0
    """int: number of instances"""

    print_symbol = "#"
    """any type: symbol for printing rectangle"""

    def __init__(self, width=0, height=0):
        """Initialiazes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns a string rep of the rectangle"""
        if self.__height == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        '''Returns formal string representation...'''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Called when deleting an instance of rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest of the two rectangles.
        Args:
            rect_1: The first rectangle.
            rect_2: The second rectangle.
            Raises:
            TypeError: If rect_1, rect_2 are not instances of Rectangle.
        Returns:
            The rectangle with the larger area.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1
