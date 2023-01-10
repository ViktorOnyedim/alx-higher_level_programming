#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ()):
        sentence[0] = None
    str_len = len(sentence)
    first_chr = sentence[0]
    new_tuple = (str_len, first_chr)
    return new_tuple
