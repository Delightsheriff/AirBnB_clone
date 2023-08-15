#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
import models

"""
A class BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel:
    """
        BaseModel class that defines attributes/methods for other classes.

        Attributes:
            id (str): The unique identifier of the model instance.
            created_at (datetime): The creation time of the model instance.
            updated_at (datetime): The update time of the model instance.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel object.
        """
        if kwargs:
            # Check if each key in kwargs is `created_at` or `updated_at`.
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    # Convert the value to a datetime object
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")

                if arg != '__class__':
                    # Set the attribute with the given name to the given value,
                    # if the key is not `__class__`.
                    setattr(self, arg, val)
        else:
            # Generate a unique id for the object
            self.id = str(uuid4())
            # Set the creation and update timestamps
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the update timestamp.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the object to a dictionary.
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = type(self).__name__
        result_dict['created_at'] = result_dict['created_at'].isoformat()
        result_dict['updated_at'] = result_dict['updated_at'].isoformat()
        return result_dict
