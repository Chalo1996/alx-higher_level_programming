#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newLst = [i % 2 == 0 for i in my_list]
    return newLst
