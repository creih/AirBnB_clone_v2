#!/usr/bin/python3
"""this module includes all the tests for this whole project repo"""
import os
import unittest
import datetime
import json
from uuid import UUID
from models.base_model import BaseModel


class test_basemodel(unittest.TestCase):
    """this is the test class"""

    def __init__(self, *args, **kwargs):
        """this is the initialisation of the class"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """this is a building block for all other tests"""
        pass

    def tearDown(self):
        """testing the tear func"""
        os.remove('file.json')

    def test_default(self):
        """this is a default test not doing much really if not nothing"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """testing the key word arrguments."""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """testing the integers in kargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """testing the string variables"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """testing the dictionary"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """testing for some kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """testing keys in kwargs"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """tesing the ids of recorded info"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """this test is verifying if created_at variable has dateTime type """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """this test verifies if creation date and update date is the same"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at != new.updated_at)
