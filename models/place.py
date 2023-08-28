#!/usr/bin/python3
"""
This file defines the Place class,
which represents a place in the system.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class

    Attributes:
        city_id (str): The ID of the city that the place is in.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests
        that the place can accommodate.
        price_by_night (float): The price of the place per night.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of IDs of the amenities that the place has.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance object of the Place class.
        Args:
            *args (positional arg): Positional argument.
            **kwargs (keyword arg): Key value pair arguments.
        """

        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
