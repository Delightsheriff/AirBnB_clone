#!/usr/bin/python3
"""
A class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import models
from models.base_model import BaseModel


class FileStorage:
    """
    This class is responsible for storing and retrieving instances
    of the BaseModel class to a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        """
        Returns a dictionary of all the stored instances.
        """
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """
        Adds a new instance to the dictionary of stored instances.

        Args:
            obj: The instance to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """
        Serializes the dictionary of stored instances to a JSON file.
        """
        data = {}
        for key, obj in cls.__objects.items():
            data[key] = obj.to_dict()

        with open(cls.__file_path, 'w', encoding="utf-8") as W_file:
            json.dump(data, W_file)

    @classmethod
    def reload(cls):
        """
        Deserializes the JSON file to the dictionary of stored instances.
        """
        try:
            with open(cls.__file_path, 'r', encoding="utf-8") as R_file:
                deserial = json.load(R_file)

                for key, obj in deserial.items():
                    cls.__objects[key] = BaseModel(**obj)
        except FileNotFoundError:
            pass
