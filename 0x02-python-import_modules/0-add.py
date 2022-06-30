#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    res = "{:d} + {:d} = {:d}".format(a, b, add(a, b))
    print(res)
