#!/usr/bin/python3
"""
finds the peak in a list of unsortef integers
"""


def find_peak(list_of_integers):
    """
    function to find the peak value
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]

    # max = 0
    # if len(list_of_integers) < 1:
    #     return None
    # for x in list_of_integers:
    #     if x > max:
    #         max = x
    # return max
