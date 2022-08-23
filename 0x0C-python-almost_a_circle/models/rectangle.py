#!/usr/bin/python3
"""Contains the Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """Inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor

        Creates private instance attributes
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """defines a width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Defines a width setter
        """
        self.validator_for_all(width, "width", flag=False)

        self.__width = width

    @property
    def height(self):
        """defines a height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Defines a height setter
        """
        self.validator_for_all(height, "height", flag=False)

        self.__height = height

    @property
    def x(self):
        """defines a x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """Defines a x setter
        """
        self.validator_for_all(x, "x", flag=True)

        self.__x = x

    @property
    def y(self):
        """defines a y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """Defines a y setter
        """
        self.validator_for_all(y, "y", flag=True)

        self.__y = y

    def validator_for_all(self, val_input, name, flag=None):
        """Validates the attrs inputs
        """
        if type(val_input) is not int:
            raise TypeError("{} must be an integer".format(name))

        if flag is False:
            if val_input <= 0:
                raise ValueError("{} must be > 0".format(name))

        if flag is True:
            if val_input < 0:
                raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Returns the area of the rectangle
        """
        A = self.width * self.height
        return A

    def display(self):
        """Prints Rectangle instance with '#' character
        """
        for k in range(self.y):
            print()

        for i in range(self.height):
            print("".join([" " for i in range(self.x)]), end="")
            print("".join(["#" for j in range(self.width)]), end="")
            print("")

    def __str__(self):
        """Returns a neatly formatted output
        """
        return "[Rectangle] ({}) {}/{} - \
        {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        if args:
            self.__argpassed(*args)
        else:
            self.__argpassed(**kwargs)

    def __argpassed(self, id=None, width=None, height=None, x=None, y=None):
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle
        """
        return {
            'id': self.id, 'width': self.width,
            'height': self.height, 'x': self.x, 'y': self.y
        }
