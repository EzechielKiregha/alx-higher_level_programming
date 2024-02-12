#!/usr/bin/python3
"""a module that defines a rectangle class"""

from . import base
Base = base.Base


def validate_prop(name, value):
    if name in ("width", "height"):
        dimension = name
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value <= 0:
            raise ValueError(f"{dimension} must be > 0")
    elif name in ("x", "y"):
        point = name
        if not isinstance(value, int):
            raise TypeError(f"{point} must be an integer")
        if value < 0:
            raise ValueError(f"{point} must be >= 0")


class Rectangle(Base):
    """a class that defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the constructor function"""
        super().__init__(id)
        validate_prop("width", width)
        self.__width = width
        validate_prop("height", height)
        self.__height = height
        validate_prop("x", x)
        self.__x = x
        validate_prop("y", y)
        self.__y = y

    def area(self):
        """returns the area of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """prints the visual representation of the Rectangle class"""
        pad_x = " " * self.x
        pad_y = "\n" * self.y
        print(pad_y, end="")
        for _ in range(self.height):
            print(pad_x, end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """updates some(or all) attributes of the rectangle class"""
        attr_map = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        for ind, attr in enumerate(args):
            if ind > 4:
                break
            self.__setattr__(attr_map[ind], attr)
        if (args):
            return
        for (key, value) in kwargs.items():
            self.__setattr__(key, value)

    @property
    def width(self):
        """a public instance attribute for accessing the width"""
        return self.__width

    @property
    def height(self):
        """a public instance attribute for accessing the height"""
        return self.__height

    @property
    def x(self):
        """a public instance attribute for accessing the x attribute"""
        return self.__x

    @property
    def y(self):
        """a public instance attribute for accessing the y attribute"""
        return self.__y

    @width.setter
    def width(self, w):
        """a setter method for the public instance attribute 'width'"""
        validate_prop("width", w)
        self.__width = w

    @height.setter
    def height(self, h):
        """a setter method for the public instance attribute 'height'"""
        validate_prop("height", h)
        self.__height = h

    @x.setter
    def x(self, val):
        """a setter method for the public instance attribute 'x'"""
        validate_prop("x", val)
        self.__x = val

    @y.setter
    def y(self, val):
        """a setter method for the public instance attribute 'y'"""
        validate_prop("y", val)
        self.__y = val

    def __str__(self):
        """returns the string representation of an instance"""
        f_string = "[Rectangle] ({}) {}/{} - {}/{}"
        return f_string.format(self.id, self.x, self.y,
                               self.width, self.height)

    def to_dictionary(self):
        """returns the dictionary representation of an instance"""
        all_attributes = {
                    key: value
                    for key, value in vars(self).items()
                    if not key.startswith("_")
                }
        unmangled_attributes = {
                    key[key.rfind("_") + 1:]: value
                    for key, value in vars((self)).items()
                    if key.startswith("_")
                }
        all_attributes.update(unmangled_attributes)
        return all_attributes
