#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for item in range(list_length):
        try:
            result = my_list_1[item] / my_list_2[item]
        except IndexError:
            print("out of range")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        finally:
            new_list.append(result)
    return new_list
