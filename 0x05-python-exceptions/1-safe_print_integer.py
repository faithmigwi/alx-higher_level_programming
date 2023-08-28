#!/usr/bin/python3
def safe_print_integer(value):
    """ prints an int with .format """
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
