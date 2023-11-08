"""Test my zip function."""

__author__ = "730660578"

from lessons.zip import zip


def test_lists_len_of_one() -> None:
    """zip(["Friday"], [1]) should return {"Friday": 1}."""
    assert zip(["Friday"], [1]) == {"Friday": 1}


def test_lists_len_of_two() -> None:
    """zip(["Monday", "Tuesday"], [1, 2]) should return {"Monday": 1, "Tuesday": 2}."""
    assert zip(["Monday", "Tuesday"], [1, 2]) == {"Monday": 1, "Tuesday": 2}


def test_empty_list() -> None:
    """zip([], []) should return an empty list."""
    assert zip([], []) == {}


def test_length_lists() -> None:
    """zip(["Monday", "Tuesday", "Wednesday"], [1, 2]) should return an empty list."""
    assert zip(["Monday", "Tuesday", "Wednesday"], [1, 2]) == {}