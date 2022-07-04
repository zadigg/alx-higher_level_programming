#!/usr/bin/python3


def no_c(my_string):
    """
    Function that removes  all character c and C
    Parameters:
    @my_string: the list
    Return: the copy of the original if failed
    """
    if my_string is not None:
        return ''.join(filter(lambda c: c.lower() != 'c', my_string))
    return None