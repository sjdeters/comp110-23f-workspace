"""Dictionary related utility functions."""

from csv import DictReader

__author__ = "730660578"


# Define your functions below
def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read a csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    for row in table:
        # Append every value under key header.
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Changes data from list of row into a dict of columns."""
    result: dict[str, list[str]] = dict()
    i: int = 0
    while i < len(table):
        group = table[i]
        for key in group:
            column_name: str = key
            values: list[str] = column_values(table, column_name)
            result[f"{column_name}"] = values
        i += 1
    return result


def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produces a new table with only the first 'N' number of rows."""
    result: dict[str, list[str]] = dict()
    for key in table:
        new_list: list[str] = []
        i: int = 0
        while (i < N) and (i < len(table)):
            new_list.append(table[f'{key}'][i])
            i += 1
        result[f"{key}"] = new_list
    return result


def select(table: dict[str, list[str]], chosen_columns: list[str]) -> dict[str, list[str]]:
    """Produces a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = dict()
    for elem in chosen_columns:
        result[f'{elem}'] = table[f'{elem}']
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = dict()
    for key in table1:
        result[f'{key}'] = table1[f'{key}']
    for key2 in table2:
        if f'{key2}' in result:
            result[f'{key2}'] += table2[f'{key2}']
        else: 
            result[f'{key2}'] = table2[f'{key2}']
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in an input list."""
    result: dict[str, int] = dict()
    for elem in input_list:
        if elem in result:
            result[f'{elem}'] += 1
        else:
            result[f'{elem}'] = 1
    return result