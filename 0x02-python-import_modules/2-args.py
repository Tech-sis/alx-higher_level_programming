#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    size = len(sys.argv)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) != 1 else "argument",
                 "." if (size) == 0 else ":"))
    for i in range(size):
        print("{:d}: {:s}".format(i + 1, sys.argv[i]))
