#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    res_add = "{:d} + {:d} = {:d}".format(a, b, add(a, b))
    res_sub = "{:d} - {:d} = {:d}".format(a, b, sub(a, b))
    res_mul = "{:d} * {:d} = {:d}".format(a, b, mul(a, b))
    res_div = "{:d} / {:d} = {:d}".format(a, b, div(a, b))
    print(res_add)
    print(res_sub)
    print(res_mul)
    print(res_div)
