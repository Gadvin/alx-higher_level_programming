#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_string(my_obj):
    """function that returs json string containing object's
    representation
        -> handles no exceptions in serialization proccess
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
