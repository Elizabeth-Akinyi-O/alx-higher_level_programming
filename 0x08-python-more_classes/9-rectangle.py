#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """Define the Rectangle class.
    Attributes:
        number_of_instances (int): Number of Rectangle instances.
        print_symbol: Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/Set the width of the Rectangle instance."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle instance.
        Args:
            value: value of the width, must be a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of the Rectangle instance."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance.
        Args:
            value: value of the height, must be a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return the printable representation of the
            Rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect_str = ""
        for a in range(self.__height):
            for b in range(self.__width):
                rect_str += str(self.print_symbol)
            rect_str += "\n"
        return rect_str[:-1]

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes a Rectangle and prints a message."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Finds the biggest Rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return (rect_1)
        if rect_1.area() < rect_2.area():
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle with width == height == size.
        Args:
            size (int): Width and height of the new rectangle.
        """
        return (cls(size, size))
