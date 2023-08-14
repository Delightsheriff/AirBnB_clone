#!/usr/bin/python3
"""
This file defines the Amenity class,
which represents an amenity in the system.
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""
