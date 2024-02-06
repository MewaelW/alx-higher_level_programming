#!/usr/bin/python3
"""A module which defines the class Student
"""


class Student:
    """ A class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ A special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ A method that returns directory description """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list

        return obj

    def reload_from_json(self, json):
        """ This replaces all attributes of the Student instance """
        for atr in json:
            self.__dict__[atr] = json[atr]
