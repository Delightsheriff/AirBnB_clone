import unittest
from main import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        # Test that the object is initialized correctly
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_str(self):
        # Test that the string representation is correct
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save(self):
        # Test that the save method updates the updated_at attribute
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict(self):
        # Test that the to_dict method returns a
        # dictionary with the correct attributes
        obj = BaseModel()
        result_dict = obj.to_dict()
        self.assertIsInstance(result_dict, dict)
        self.assertEqual(result_dict['__class__'], 'BaseModel')
        self.assertEqual(result_dict['id'], obj.id)
        self.assertEqual(result_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(result_dict['updated_at'], obj.updated_at.isoformat())
