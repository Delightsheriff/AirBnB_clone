#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

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
    def __init__(self):
        """
        Initialize the BaseModel object.
        """
        # Generate a unique id for the object
        self.id = str(uuid4())
        # Set the creation and update timestamps
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the object.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the update timestamp.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the object to a dictionary.
        """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = result_dict['created_at'].isoformat()
        result_dict['updated_at'] = result_dict['updated_at'].isoformat()
        return result_dict
