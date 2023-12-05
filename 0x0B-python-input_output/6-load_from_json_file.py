#!/usr/bin/python3

import json

def from_json_string(my_str):
    """function to 
    desializes a JSON string back to a python object
        -> handles NO exceptions
    """
    return json.loads(my_str)
