#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    modifiedList = []
    for i in my_list:
        modifiedList.append(i)
    modifiedList[idx] = element
    return modifiedList
