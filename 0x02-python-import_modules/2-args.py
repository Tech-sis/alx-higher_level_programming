#!/usr/bin/python3
import sys
argv = sys.argv
if len(argv) < 1:
    print("{:d} arguments.".format(len(argv)))
for i in range(len(argv)):
    if len(argv) == 1:
        print("{:d} argument:".format(len(argv)), end="\n")
        print("{:d}: {}".format(i + 1, sys.argv[i]), end="\n")
    elif len(argv) > 1:
        print("{:d} arguments:".format(len(argv)), end="\n")
        print("{:d}: {}".format(i + 1, sys.argv[i]), end="\n")
