#!/usr/bin/python3
"""Task 1: Base class
The goal is to manage id attribute in all futures classes and
avoid duplicatiing the same code."""

import json
import csv
import random
import turtle


class Base:
    """THis class will be the base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_jason_string(list_distionaries):
        """returns json string of the list_dictionaries to a file"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """return list from json files"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instances with all atributes set"""
        dump = cls(1, 1)
        dump.update(**dictionary)
        return dump

    @staticmethod
    def save_to_file(cls, list_objs):
        """this constructor writes the json string of the list_objs"""
        with open(cls.__name__ + ".json", 'w') as jfile:
            list_dict = []
            if list_objs = [x.to_dictionary() for x in list_objs]
            jfile.write(cls.to_json_string(list_dict))

    @classmethod
    def load_from_file(cls):
        """opens a file for reading and returns list of instances"""
        json_list = None
        try:
            with open(cls.__name__ + ".json") as j_file:
                json_list = cls.from_json_string(j_file.read())
        except FileNotFoundError:
            return []
        return [cls.create(**x) for x in json_list]
