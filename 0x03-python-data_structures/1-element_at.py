#!/usr/bin/python3
def element_at(my_list, idx):
    lenElements = len(my_list)
    if idx > lenElements - 1:
        return None
    if idx == idx * - 1:
        return None
    else:
        return idx + 1
