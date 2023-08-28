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
        review_id (str): The ID of review.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text of the review.
    """
    def __init__(self, *args, **kwargs):
        """
            Initialize class user with kwargs
            Args:
                *args(positional arg): strings
                **kwargs(keyword arg): dictionary
        """
        super().__init__(*args, **kwargs)
        self.review_id = ""
        self.user_id = ""
        self.text = ""
