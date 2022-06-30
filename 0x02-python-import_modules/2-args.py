#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = 1
    myArgs = sys.argv
    len_myArgs = len(myArgs) - 1
    if len_myArgs == 1:
        print("{:d} argument:".format(len_myArgs))
    elif len_myArgs >= 2:
        print("{:d} arguments:".format(len_myArgs))
    else:
        print("{:d} arguments.".format(len_myArgs))
    for arg in myArgs:
        if arg != myArgs[0]:
            print("{:d}: {}".format(index, arg))
            index += 1
