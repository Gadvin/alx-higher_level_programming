#!/usr/bin/python3
"""Defines a JSON file-reading function.
"""


import json


def load_from_json_file(my_str):
    """function to Create a Python object from a JSON file"""
     with open(my_str) as f:
        return json.load(f)
