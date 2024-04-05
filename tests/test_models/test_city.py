#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)

    def test_state_id(self):
        """ """
        new = City()
        new.state_id = ""
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = City()
        new.name = "City"
        self.assertEqual(type(new.name), str)
