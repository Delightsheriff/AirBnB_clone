#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import os
import json


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """
        This method runs before each test and creates a BaseModel instance
        and a FileStorage instance.
        """
        self.model = BaseModel()
        self.storage = FileStorage()

    def tearDown(self):
        """
        This method runs after each test and deletes the BaseModel instance
        and the FileStorage instance.
        """
        del self.model
        del self.storage

    def test_init_with_defaults(self):
        """
        This method tests the __init__ method of the
        BaseModel class with default values.
        It checks that the method creates an object
        with a unique id and current timestamps.
        """
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_init_with_kwargs(self):
        """
        This method tests the __init__ method of the
        BaseModel class with keyword arguments.
        It checks that the method creates an object with the
        given attributes and converts the timestamps to datetime objects.
        """
        kwargs = {
            "id": "123456",
            "name": "Alice",
            "created_at": "2023-08-12T16:33:29.000000",
            "updated_at": "2023-08-12T16:33:29.000000"
        }

        new_model = BaseModel(**kwargs)

        self.assertEqual(new_model.id, kwargs["id"])
        self.assertEqual(new_model.name, kwargs["name"])
        temp = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(new_model.created_at, temp)
        temps = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(new_model.updated_at, temps)

    def test_str_representation(self):
        """
        This method tests the __str__ method of the BaseModel class.
        It checks that the method returns a string representation
        of the object in the format [<class name>] (<id>) <dictionary>.
        """
        temp = {self.model.__class__.__name__}
        expected_str = f"[{temp}] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """
        This method tests the save method of the BaseModel class.
        It checks that the method updates the updated_at
        attribute and saves the object to a JSON file.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r', encoding="utf-8") as R_file:
            data = json.load(R_file)
            temp = f"{self.model.__class__.__name__}.{self.model.id}"
            self.assertIn(temp, data)
            self.assertEqual(data[temp], self.model.to_dict())

    def test_to_dict_method(self):
        """
        This method tests the to_dict method of the BaseModel class.
        It checks that the method returns a dictionary
        representation of the object with the class name and
        ISO-formatted timestamps.
        """
        result_dict = self.model.to_dict()
        self.assertIsInstance(result_dict, dict)
        x = self.model.__class__.__name__
        y = self.model.created_at.isoformat()
        z = self.model.updated_at.isoformat()
        self.assertEqual(result_dict['__class__'], x)
        self.assertEqual(result_dict['created_at'], y)
        self.assertEqual(result_dict['updated_at'], z)
