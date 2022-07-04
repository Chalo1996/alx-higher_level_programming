#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    revNum = my_list[::-1]
    if my_list:
        for i in revNum:
            print("{:d}".format(i))
