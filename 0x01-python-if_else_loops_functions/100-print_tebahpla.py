#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{:c}".format((i - (ord('a') - ord('A'))) if i % 2 else i), end='')
