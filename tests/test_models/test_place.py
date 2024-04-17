#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """for the places file """

    def __init__(self, *args, **kwargs):
        """ initialisation of the file module"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """testing the city id """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ testing user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ testing the name """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """testing the desc """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """NBR of rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """testing bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ testing max_guests"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ testing pricepe nght"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ latitude test check"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """repeated """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """testing amenity """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
