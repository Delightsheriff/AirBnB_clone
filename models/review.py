#!/usr/bin/python3
"""
This file defines the Review class, which represents a review
of a place in the system.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class

    Attributes:
        place_id (str): The ID of the place that the review is for.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text of the review.
    """

    def __init__(self, *args, **kwargs):
        """
            Initialize clss user with kwargs
            Args:
                *args(positional arg): strings
                **kwargs(keyword arg): dictionary
        """
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""