"""Establishing module for list utility functions"""

__author__: str = "730656976"

def all(input_list: list[int], attempt: int) -> bool:
    """Indicates if all ints in list are equal to the given int."""
    
    is_same: bool = True
    if len(input_list) == 0:
        return False

    for i in range(len(input_list)):
        if input_list[i] != attempt:
            is_same = False
    
    return is_same


def max(input_list: list[int]) -> int:
    """Returns the largest number in a list."""

    if len(input_list) == 0:
        raise ValueError("max() arg is an empty List")
    largest: int = input_list[0]
    for i in range(len(input_list) - 1):
        if input_list[i] < input_list[i + 1]:
            largest = input_list[i +1 ]
    return largest

def is_equal(lst_one: list[int], lst_two: list[int]) -> bool:
    """Checks to see if integer lists have the same contents"""

    if len(lst_one) != len(lst_two):
        raise ValueError("the lists do not have equal size")
    has_same: bool = True
    for i in range(len(lst_one)):
        if lst_one[i] != lst_two[i]:
            has_same = False
    return has_same