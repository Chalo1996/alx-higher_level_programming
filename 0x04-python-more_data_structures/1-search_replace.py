#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for num in my_list:
        new.append(num)
        if num == search:
            new.remove(search)
            new.append(replace)
    return new
