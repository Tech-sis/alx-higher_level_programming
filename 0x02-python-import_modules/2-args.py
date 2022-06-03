#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)
    if i == 0:
        print("{} arguments.".format(i), end="")
    elif i == 1:
        print("{} argument:".format(i), end="\n")
    else:
        print("{} arguments:".format(i), end="\n")
    if i >= 1:
        for i in range(i):
            print("{:d}: {:s}".format(i + 1, str(sys.argv[i])), end="\n")
