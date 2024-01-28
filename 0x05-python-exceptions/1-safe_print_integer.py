#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
<<<<<<< HEAD
        return True
    except ValueError:
=======
    except (TypeError, ValueError):
>>>>>>> e8fba4cfbe8bcb91d9cdc79c632bc12aaff2fe94
        return False
    else:
        return True
