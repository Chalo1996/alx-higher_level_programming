#!/usr/bin/python3
"""Contains the load_from_json_file function
"""


from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

try:
    python_list = load_from_json_file(filename)
except FileNotFoundError:
    python_list = []

for arg in argv:
    if arg != argv[0]:
        python_list.append(arg)

save_to_json_file(python_list, filename)
