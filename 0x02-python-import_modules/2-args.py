#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = 1
    myArgs = sys.argv
    len_myArgs = len(myArgs)
    print("{:d} {:s}{:s}".format(len_myArgs - 1, "argument" if len_myArgs <= 2 else "arguments", "." if len_myArgs == 1 else ":"))
    for arg in myArgs:
        if arg != myArgs[0]:
            print("{:d}: {}".format(index, arg))
            index += 1
