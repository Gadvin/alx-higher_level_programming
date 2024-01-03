#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_string(my_str):
    """function to 
    desializes a JSON string back to a python object
        -> handles NO exceptions
    """
    return json.loads(my_str)
