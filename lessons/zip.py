"""Combining two lists into a dictionary."""

__author__ = "730660578"


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Function for adding to lists together."""
    dictionary: dict[str, int] = dict()
    idx: int = 0
    if len(str_list) == 0 or len(int_list) == 0:
        return dictionary
    if len(str_list) != len(int_list):
        return dictionary
    for key in str_list:
        dictionary[str_list[idx]] = int_list[idx]
        idx += 1
    return dictionary