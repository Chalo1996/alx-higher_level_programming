#!/usr/bin/python3
def element_at(my_list, idx):
    lenElements = len(my_list) - 1
    if idx > lenElements:
        return None
    if idx == idx * - 1:
        return None
    else:
        return my_list[idx]
