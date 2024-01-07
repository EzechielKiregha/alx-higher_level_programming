#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    s = 0
    for arg in argv[1:]:
        if arg:
            s += int(arg)
    print(s)
