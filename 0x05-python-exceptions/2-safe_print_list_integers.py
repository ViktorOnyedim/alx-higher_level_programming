#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        printed = 0
        for i in range(x):
            if int(my_list[i]):
                print("{:d}".format(my_list[i]), end="")
                printed += 1
            else:
                continue
    except ValueError:
        pass
    return printed
