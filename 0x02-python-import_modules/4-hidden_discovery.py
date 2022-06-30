#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as pyc
    for name in dir(pyc):
        if name[:2] != "__":
            print("{:s}".format(name))
