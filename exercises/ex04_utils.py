"""EX04 - 'list' Utility Functions."""

__author__ = "730660578"


def all(input_list: list[int], input_int: int) -> bool:
    """Determines if a given intger is seen in every number of a list."""
    if len(input_list) == 0:
        return False
    idx: int = 0
    while idx < len(input_list):
        if input_list[idx] != input_int:
            return False
        else: 
            idx += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest value in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    largest_int: int = input[0]
    while idx < len(input):
        if input[idx] > largest_int:
            largest_int = input[idx]
        idx += 1
    return largest_int


def is_equal(int_list1: list[int], int_list2: list[int]) -> bool:
    """Determines if both lists are the same."""
    if len(int_list1) == 0 and len(int_list2) == 0:
        return True
    if len(int_list1) == 0 or len(int_list2) == 0:
        return False
    sequence_test: bool = True
    idx: int = 0
    while idx < len(int_list1) and idx < len(int_list2):
        if int_list1[idx] != int_list2[idx]:
            sequence_test = False
        idx += 1 
    if sequence_test is True:
        if len(int_list1) != len(int_list2):
            return False
        return True
    else:    
        if len(int_list1) != len(int_list2):
            return False
        return False