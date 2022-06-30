#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = 1
    myArgs = sys.argv
    len_myArgs = len(myArgs)
    print("{:d} arguments:".format(len_myArgs - 1))
    for arg in myArgs:
        if arg != myArgs[0]:
            print("{:d}: {}".format(index, arg))
            index += 1
