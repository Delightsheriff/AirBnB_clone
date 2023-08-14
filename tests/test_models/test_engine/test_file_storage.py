#!/usr/bin/python3

import unittest
import models
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
        of all the stored instances and that the dictionary
        contains the expected instance.
        """
        dict_of_obj = self.storage.all()
        self.assertIsInstance(dict_of_obj, dict)

        new_model = BaseModel()

        temp = "{}.{}".format(new_model.__class__.__name__, new_model.id)

        self.assertIn(temp, dict_of_obj)
        self.assertEqual(dict_of_obj[temp], new_model)

        for key, obj in dict_of_obj.items():
            self.assertIsInstance(obj, object)

    def test_all_dict_of_obj(self):
        """Test if returns dict of obj"""
        dict_of_obj = FileStorage._FileStorage__objects
        for key, obj in dict_of_obj.items():
            self.assertIsInstance(obj, object)


    def test_new(self):
        """
        This method tests the new method of the FileStorage class.
        It checks that the method adds a new instance
        to the dictionary of stored instances and that the keys
        in the dictionary follow the expected format.
        """
        # Created a new BaseModel instance
        new_model = BaseModel()

        # new method to add the new instance to __objects
        self.storage.new(new_model)

        # Construct the key for the new instance
        key = "{}.{}".format(new_model.__class__.__name__, new_model.id)


        # Retrieve the dictionary of stored instances (__objects)
        dict_of_obj = FileStorage._FileStorage__objects

        # Validate that the key is present in __objects
        self.assertIn(key, dict_of_obj)

        # Retrieve the object associated with the key in __objects
        added_object = dict_of_obj[key]

        # Validate that the added_object is the same as the new_model instance
        self.assertEqual(added_object, new_model)

        # Validate that the key follows the expected format
        self.assertEqual(key, "{}.{}".format(added_object.__class__.__name__, added_object.id))


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
            temp = "{}.{}".format(self.model.__class__.__name__, self.model.id)

            self.assertIn(temp, data)
            self.assertEqual(data[temp], self.model.to_dict())

    def test_reload(self):
        """
        This method tests the reload method of the FileStorage class.
        It checks that the method deserializes the JSON file
        to the dictionary of stored instances and verifies that
        a specific object is correctly reloaded.
        """
        # Remove the existing "file.json" if it exists
        if os.path.exists("file.json"):
            os.remove("file.json")

        # Create a new BaseModel instance
        new_model = BaseModel()

        # the BaseModel instance's dictionary representation to "file.json"
        with open("file.json", 'w', encoding="utf-8") as W_file:
            temp = "{}.{}".format(new_model.__class__.__name__, new_model.id)

            data = {temp: new_model.to_dict()}
            json.dump(data, W_file)

        # FileStorage instance
        file_storage = FileStorage()

        # Added the BaseModel instance to the __objects dictionary
        file_storage.new(new_model)

        # Saved the instance to "file.json"
        file_storage.save()

        # Reload the data from "file.json"
        file_storage.reload()

        # Retrieve the dictionary of objects from the FileStorage instance
        dict_of_obj = file_storage._FileStorage__objects

        # Verify that the previously added BaseModel instance is present
        self.assertIn("BaseModel." + str(new_model.id), dict_of_obj)
