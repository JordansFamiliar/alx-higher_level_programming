#!/usr/bin/python3
"""A script that adds all arguments to a Python list
and then save them to a file.
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list_items = sys.argv[1:]
filename = "add_item.json"

if os.path.exists(filename):
    temp_list = load_from_json_file(filename)
    for items in list_items:
        temp_list.append(items)
    list_items = temp_list
save_to_json_file(list_items, filename)
