#!/usr/bin/python3
def element_at(my_list, idx):
    lenElements = len(my_list)
    if idx > lenElements:
        return None
    if idx == idx * - 1:
        return None
    return my_list[idx]
