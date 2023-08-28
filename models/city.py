#!/usr/bin/python3
"""This file defines the City class, which represents a city in the system."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class

    Attributes:
        city_id (str): The ID of the city.
        name (str): The city's name.
    """
    def __init__(self, *args, **kwargs):
        """
            Initialize clss user with kwargs
            Args:
                *args(positional arg): strings
                **kwargs(keyword arg): dictionary
        """
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.name = ""
    #state_id = ""
    #name = ""
