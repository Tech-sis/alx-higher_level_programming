#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    arg = sys.argv[1:]
    if len(arg) == 1:
        result = int(arg[0])
    else:
        for i in arg:
            result += int(i)
            print(result)
