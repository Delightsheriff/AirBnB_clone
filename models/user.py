#!/usr/bin/python3
"""This file defines the User class, which represents a user in the system."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
     def __init__(self, *args, **kwargs):
        """
            Initialize clss user with kwargs
            Args:
                *args(positional arg): strings
                **kwargs(keyword arg): dictionary
        """
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
