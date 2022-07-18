#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lstlen = 0

    try:
        for item in my_list:
            if item in range(x + 1):
                lstlen += 1
                print("{}".format(item), end="")
        print("")
        return lstlen

    except IndexError:
        if x > lstlen:
            return
