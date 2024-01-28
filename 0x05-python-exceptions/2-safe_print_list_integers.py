#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    number_printed = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
            number_printed += 1
        except (ValueError, TypeError):
            continue
    print()
    return number_printed
