#!/usr/bin/python3
"""This file defines the State class,
which represents a state in the system.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class

    Attributes:
        name (str): The state's name.
    """
 
     def __init__(self, *args, **kwargs):
        """
            Initialize clss user with kwargs
            Args:
                *args(positional arg): strings
                **kwargs(keyword arg): dictionary
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.user_id = ""
        self.text = ""