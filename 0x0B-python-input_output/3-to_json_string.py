#!/usr/bin/python3
"""
definition of to_json_string method
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
