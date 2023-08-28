#!/usr/bin/python3
"""This file defines the State class,
which represents a state in the system.
"""
from models.base_model import BaseModel
from models.user import User



class State(BaseModel):
    """
    State class

    Attributes:
        name (str): The state's name.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize State instance with kwargs
        Args:
            *args (positional args): strings
            **kwargs (keyword args): dictionary
        """
        super().__init__(*args, **kwargs)
        self.name = ""
