#!/usr/bin/python3
"""
This script adds all arguments to a Python list,
and then saves them to a file named 'add_item.json'.
"""
from sys import argv
save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
load_from_json_file = _import_('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_items = load_from_json_file(filename)
except FileNotFoundError:
    existing_items = []

existing_items.extend(argv[1:])
save_to_json_file(existing_items, filename)
