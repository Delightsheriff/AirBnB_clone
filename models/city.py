#!/usr/bin/python3
"""This file defines the City class, which represents a city in the system."""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class

    Attributes:
        state_id (str): The ID of the state that the city is in.
        name (str): The city's name.
    """
    state_id = ""
    name = ""
