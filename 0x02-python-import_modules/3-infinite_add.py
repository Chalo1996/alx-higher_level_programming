#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sumArgs = 0
    myArgs = sys.argv
    for arg in myArgs:
        if arg != myArgs[0]:
            arg = int(arg)
            sumArgs += arg
    print("{:d}".format(sumArgs))
