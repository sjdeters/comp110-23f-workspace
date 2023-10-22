"""Summing the elements of a list using different loops."""

__author__ = "730660578"


def w_sum(vals: list[float]) -> float:
    """Sum using while loop."""
    idx: int = 0
    list_sum: float = 0.0
    while idx < len(vals):
        list_sum += vals[idx]
        idx += 1
    return list_sum


def f_sum(vals: list[float]) -> float:
    """Sum using for...in."""
    list_sum: float = 0.0
    for elem in vals:
        list_sum += elem
    return list_sum


def f_range_sum(vals: list[float]) -> float:
    """Sum using for...in range."""
    list_sum: float = 0.0
    for idx in range(0, len(vals), 1):
        list_sum += vals[idx]
    return list_sum