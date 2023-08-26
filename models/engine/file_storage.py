#!/usr/bin/python3
"""
A class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State


class FileStorage:
    """
    This class is responsible for storing and retrieving instances
    of the BaseModel class to a JSON file.
    """
       __file_path = "file.json"  # file path to JSON file
    __objects = {}  # stores all dictionary objects by the class name id


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
                    # Check if the class inherits from BaseModel
                    cls_name = obj["__class__"]
                    temp = models.base_model.BaseModel
                    if issubclass(models.__dict__[cls_name], temp):
                        # Create an instance of the class with **kwargs
                        cls.__objects[key] = models.__dict__[cls_name](**obj)
        except FileNotFoundError:
            pass
