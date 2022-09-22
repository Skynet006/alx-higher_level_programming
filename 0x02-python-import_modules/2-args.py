#!/usr/bin/python3
from sys import argv
num_args = len(argv)
total = 0
for i in range(1, num_args):
    total += int(argv[1])
    print("{:d}".format(total))
