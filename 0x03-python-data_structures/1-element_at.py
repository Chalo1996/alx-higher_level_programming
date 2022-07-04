#!/usr/bin/python3
def element_at(my_list, idx):
    lenElements = len(my_list)
    if idx < 0 or idx >= lenElements:
        return None
    return idx + 1
