#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """
    This class contains tests for the FileStorage class.
    """

    def setUp(self):
        """
        This method runs before each test and creates a FileStorage instance
        and a BaseModel instance.
        """
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """
        This method runs after each test and deletes the FileStorage instance
        and the BaseModel instance.
        """
        del self.storage
        del self.model

    def test_all(self):
        """
        This method tests the all method of the FileStorage class.
        It checks that the method returns a dictionary
        of all the stored instances.
        """
        self.assertIsInstance(self.storage.all(), dict)
        temp = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(temp, self.storage.all())
        self.assertEqual(self.storage.all()[temp], self.model)

    def test_new(self):
        """
        This method tests the new method of the FileStorage class.
        It checks that the method adds a new instance
        to the dictionary of stored instances.
        """
        new_model = BaseModel()
        self.storage.new(new_model)
        temp = f"{self.model.__class__.__name__}.{self.model.id}"
        self.assertIn(temp, self.storage.all())
        self.assertEqual(self.storage.all()[temp], new_model)

    def test_save(self):
        """
        This method tests the save method of the FileStorage class.
        It checks that the method serializes the
        dictionary of stored instances to a JSON file.
        """
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", 'r', encoding="utf-8") as R_file:
            data = json.load(R_file)
            temp = f"{self.model.__class__.__name__}.{self.model.id}"
            self.assertIn(temp, data)
            self.assertEqual(data[temp], self.model.to_dict())

    def test_reload(self):
        """
        This method tests the reload method of the FileStorage class.
        It checks that the method deserializes the JSON file
        to the dictionary of stored instances.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

        new_model = BaseModel()

        with open("file.json", 'w', encoding="utf-8") as W_file:
            temp = f"{new_model.__class__.__name__}.{new_model.id}"
            data = {temp: new_model.to_dict()}
            json.dump(data, W_file)
