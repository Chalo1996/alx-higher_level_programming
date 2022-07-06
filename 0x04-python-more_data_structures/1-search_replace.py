#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    if my_list:
        for i in my_list:
            newList.append(i)
        newList[search] = replace
        return newList
