#!/usr/bin/python3
"""a module that defines a square class"""
from . import rectangle

Rectangle = rectangle.Rectangle
validate_prop = rectangle.validate_prop


class Square(Rectangle):
    """a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """the constructor function for the square class"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """updates some(or all) attributes of the rectangle class"""
        attr_map = {0: "id", 1: "size", 2: "x", 3: "y"}
        for ind, attr in enumerate(args):
            if ind > 3:
                break
            self.__setattr__(attr_map[ind], attr)
        if (args):
            return
        for (key, value) in kwargs.items():
            self.__setattr__(key, value)

    @property
    def size(self):
        """a public instance method for accessing the size"""
        return self.width

    @size.setter
    def size(self, val):
        """a setter method for the public instance method 'size'"""
        validate_prop("width", val)
        self.width = val
        self.height = val

    def __str__(self):
        """returns the string representation of an instance"""
        f_string = "[Square] ({}) {}/{} - {}"
        return f_string.format(self.id, self.x, self.y, self.width)

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
                    if key.startswith("_") and key[key.rfind("_") + 1:]
                    != "width" and key[key.rfind("_") + 1:] != "height"
                }
        all_attributes.update(unmangled_attributes)
        all_attributes.update({"size": self.width})
        return all_attributes
