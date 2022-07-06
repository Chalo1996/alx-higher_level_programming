#!/usr/bin/python3
def uniq_add(my_list=[]):
    sumof = 0
    for num in set(my_list):
        sumof += num
    return sumof
