#!/usr/bin/python3
def max_integer(my_list=[]):
    maxNum = 0
    lstlen = len(my_list)
    if lstlen == 0:
        return "None"
    if my_list:
        for i in my_list:
            if i > maxNum:
                maxNum = i
        return ("{:d}".format(maxNum))
