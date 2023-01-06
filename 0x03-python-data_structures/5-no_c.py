#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for chr in my_string:
        if (chr != 'c' and chr != 'C'):
            new_str = new_str + chr
    return new_str
