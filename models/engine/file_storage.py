#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    """String - path to the JSON file"""
    __file_path = 'file.json'
    """dictionary - empty but will store ojects by <class name>.id"""
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return self.__objects
        else:
            dic_result = {}
            for key, val in self.__objects.items():
                name = key.split('.')
                if name[0] == cls.__name__:
                    dic_result.update({key: val})
            return dic_result

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes the file path to JSON file path"""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if its inside"""
        if obj:
            for key in self.__objects:
                idn = key.split('.')
                if obj.id == idn[1]:
                    del self.__objects[key]
                    break
            self.save()

    def close(self):
        """ calls reload() method for deseializing the JSON file to objects
        """
        self.reload()
