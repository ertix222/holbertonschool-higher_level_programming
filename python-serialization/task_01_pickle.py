#!/usr/bin/python3
import pickle
"""import pickles module
"""


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error serializing object: {e}")
    
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Error deserializing object: {e}")
            return None