#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    if total < 1:
        print("{:d} arguments.".format(total))
    else:
        if total == 1:
            print("{:d} argument:".format(total), end="\n")
        else:
            print("{:d} arguments:".format(total), end="\n")
        for i in range(total):
            print("{:d}: {}".format(i + 1, sys.argv[i]), end="\n")
