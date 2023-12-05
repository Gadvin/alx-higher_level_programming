#!/usr/bin/python3

import json

def to_json_string(my_obj):
    """function that returs json string containing object's
    representation
        -> handles no exceptions in serialization proccess
    """
    return json.dumps(my_obj)
