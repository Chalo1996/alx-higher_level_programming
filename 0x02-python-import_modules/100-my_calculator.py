#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    firstArg = argv[0]
    if len(argv) != 4:
        print("Usage: {:s} <a> <operator> <b>".format(firstArg))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    sign = argv[2]
    operators = ["+", "-", "*", "/"]
    if argv[2] not in operators:
        print("Unknown operator. Available operators: ", end="")
        print("+, -, * and /")
        exit(1)
    if sign in operators:
        if sign == "+":
            print("{:d} {:s} {:d} = {:d}".format(a, sign, b, add(a, b)))
        elif sign == "-":
            print("{:d} {:s} {:d} = {:d}".format(a, sign, b, sub(a, b)))
        elif sign == "*":
            print("{:d} {:s} {:d} = {:d}".format(a, sign, b, mul(a, b)))
        elif sign == "/":
            print("{:d} {:s} {:d} = {:d}".format(a, sign, b, div(a, b)))
