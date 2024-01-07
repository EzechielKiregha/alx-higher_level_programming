#!/usr/bin/python3
import sys

c = len(sys.argv) - 1

def run():
    if c == 0:
        print("0 arguments.")
    else:
        if c == 1:
            print("1 argument :")
            print("1: {}".format(sys.argv[1]))
        else:
            print("{} arguments :".format(c))
            for arg in range(1, c + 1):
                print("{}: {}".format(arg, sys.argv[arg]))

if __name__ == '__main__':
    run()
