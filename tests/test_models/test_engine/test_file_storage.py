#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import os
from console import HBNBCommand


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """ __objects is properly returned """
        new = BaseModel()
        new.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)
    
    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        new.save()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        new.save()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        new.save()
        _id = new.to_dict()['id']
               
        temp = list(storage.all().keys())[0]
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)

    def test_key_val_str_att(self):
        """ Using key="value" syntax is creating the attrebute key """
        cmd = HBNBCommand()
        cmd.do_create('User name="Alien"')
        created_instance = list(storage.all().values())[0]
        self.assertTrue(hasattr(created_instance, "name"))
    
    def test_key_val_str_value(self):
        """ Using key="value" syntax is creating the the right value """
        cmd = HBNBCommand()
        cmd.do_create('User name="Alien"')
        created_instance = list(storage.all().values())[0]
        self.assertEqual(created_instance.name, "Alien")

    def test_key_val_str_value_quote(self):
        """ Using key="value" syntax is creating the the right value if contains quote """
        cmd = HBNBCommand()
        cmd.do_create('User name="Ali"en"')
        created_instance = list(storage.all().values())[0]
        self.assertEqual(created_instance.name, "Ali\"en")

    def test_key_val_str_value_underqcore(self):
        """ Using key="value" syntax is creating the the right value if contains underscores """
        cmd = HBNBCommand()
        cmd.do_create('User wise="Testing_is_everthing!"')
        created_instance = list(storage.all().values())[0]
        self.assertEqual(created_instance.wise, "Testing is everthing!")

    def test_key_val_str_type(self):
        """ Test the feature of key="value" syntax """
        cmd = HBNBCommand()
        cmd.do_create('User name="Alien"')
        created_instance = list(storage.all().values())[0]
        self.assertIsInstance(created_instance.name, str)

    def test_key_val_int_att(self):
        """ Using key=int syntax is creating the attrebute key """
        cmd = HBNBCommand()
        cmd.do_create('User number=69')
        created_instance = list(storage.all().values())[0]
        self.assertTrue(hasattr(created_instance, "number"))
    
    def test_key_val_int_value(self):
        """ Using key=int syntax is creating the the right value """
        cmd = HBNBCommand()
        cmd.do_create('User number=69')
        created_instance = list(storage.all().values())[0]
        self.assertEqual(created_instance.number, 69)

    def test_key_val_int_type(self):
        """ key=int syntax is creating a value of the right type """
        cmd = HBNBCommand()
        cmd.do_create('User number=69')
        created_instance = list(storage.all().values())[0]
        self.assertIsInstance(created_instance.number, int)

    def test_key_val_float_att(self):
        """ Using key=float syntax is creating the attrebute key """
        cmd = HBNBCommand()
        cmd.do_create('User price=69.3')
        created_instance = list(storage.all().values())[0]
        self.assertTrue(hasattr(created_instance, "price"))
    
    def test_key_val_float_value(self):
        """ Using key=float syntax is creating the the right value """
        cmd = HBNBCommand()
        cmd.do_create('User price=69.3')
        created_instance = list(storage.all().values())[0]
        self.assertEqual(created_instance.price, 69.3)

    def test_key_val_float_type(self):
        """ key=float syntax is creating a value of the right type """
        cmd = HBNBCommand()
        cmd.do_create('User price=69.3')
        created_instance = list(storage.all().values())[0]
        self.assertIsInstance(created_instance.price, float)
