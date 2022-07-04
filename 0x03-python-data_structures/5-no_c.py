#!/usr/bin/python3
def no_c(my_string):
    anotherString = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            anotherString += i
    return anotherString
