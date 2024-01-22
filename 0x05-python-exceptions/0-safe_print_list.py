#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    number_printed = 0
    for item in range(x):
        try:
            print(my_list[item], end="")
            number_printed += 1
        except IndexError:
            break
    print()
    return number_printed
