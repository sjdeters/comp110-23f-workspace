"""EX06 - Dictionary Functions."""

__author__: "730660578"


def invert(ini_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    inv_dict = dict()
    dict_check: dict[str, int] = dict()
    for key in ini_dict:
        inv_dict[ini_dict[f"{key}"]] = key
        if ini_dict[f"{key}"] in dict_check:
            dict_check[f"{ini_dict[key]}"] += 1
        else:
            dict_check[f"{ini_dict[key]}"] = 1
    for key3 in dict_check:
        if dict_check[f"{key3}"] > 1:
            raise KeyError("at least one key is entered more than once.")
    return inv_dict


def favorite_colors(color_dict: dict[str, str]) -> str:
    """Returns the majority favorite color of the group."""
    dictionary: dict[str, int] = dict()
    for key in color_dict:
        if color_dict[key] in dictionary:
            dictionary[f"{color_dict[key]}"] += 1
        else:
             dictionary[f"{color_dict[key]}"] = 1
    score_keeper: int = 0
    for key2 in dictionary:
        if dictionary[key2] > score_keeper:
            score_keeper = dictionary[key2]
            fav_color: str = f"{key2}"
    return fav_color        

        
def count(list: list[str]) -> dict[str, int]:
    """"""
    dictionary = dict()
    i: int = 0
    while i < len(list):
        if list[i] in dictionary:
            dictionary[f"{list[i]}"] += 1
            i += 1
        else:
            dictionary[f"{list[i]}"] = 1
            i += 1
    return dictionary


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]: 
    """"""
    dictionary = dict()
    i: int = 0
    while i < len(input_list):
        first_word: str = input_list[i]
        first_chr: str = first_word[0].lower()
        same_chr_list: list[str] = list()
        alt_i: int = 0
        while alt_i < len(input_list):
            alt_word: str = input_list[alt_i]
            alt_chr: str = alt_word[0].lower()
            if first_word != alt_word and first_chr == alt_chr:
                same_chr_list.append(input_list[alt_i])
            alt_i += 1
        same_chr_list.append(input_list[i])
        dictionary[f"{first_chr}"] = same_chr_list
        i += 1
    return dictionary


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """"""
    
    daily_attendance: dict{f"{day}": student}