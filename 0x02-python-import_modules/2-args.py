#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv)

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))
    
    if i >= 1:
        for i in range(i):
                print("{:d}: {}".format(i + 1, sys.argv[i]))
