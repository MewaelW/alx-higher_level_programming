#!/usr/bin/python3
""" A module which defines the class Student
"""


class Student:
    """ A class to create student instances """

    def __init__(self, first_name, last_name, age):
        """A special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A method that returns directory description """
        return self.__dict__.copy()
