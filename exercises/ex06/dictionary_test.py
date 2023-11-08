"""EX07 - 'dict' Unit Test."""

__author__ = "7306060578"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# Tests for the invert function.
def test_invert_dict_len_1() -> None:
    """invert({'apple': 'cat'}) should return {'cat': 'apple'}."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert_dict_len_3() -> None:
    """invert({'a': 'z', 'b' : 'y', 'c': 'x'}) should return {'z': 'a', 'y': 'b', 'x': 'c'}."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_empty_dict() -> None:
    """invert({}) should return {}."""
    assert invert({}) == {}


# Tests for the favorite_color function. 
def test_favorite_color_dict_len_3() -> None:
    """favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) should return 'blue'."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == 'blue'


def test_favorite_color_dict_len_2() -> None:
    """favorite_color({"Sam": "red", "Will": "red"}) should return 'red'."""
    assert favorite_color({"Sam": "red", "Will": "red"}) == 'red'


def test_favorite_color_dict_same_num_of_colors() -> None:
    """favorite_color({"Sam": "blue", "Marcus": "purple"}) should return 'blue'."""
    assert favorite_color({"Sam": "blue", "Marcus": "purple"}) == 'blue'


# Tests for the count function. 
def test_count_list_len_2() -> None:
    """count(["ram", "ram"]) should return {'ram': 2}."""
    assert count(["ram", "ram"]) == {'ram': 2}


def test_count_list_len_4() -> None:
    """count(["ram", "tar", "heels", "tar"]) should return {'ram': 1, 'tar': 2, 'heels': 1}."""
    assert count(["ram", "tar", "heels", "tar"]) == {'ram': 1, 'tar': 2, 'heels': 1}


def test_count_empty_list() -> None:
    """count([]) should return {}."""
    assert count([]) == {}


# Tests for the alphabetizer function.
def test_alphabetizer_list_len_6() -> None:
    """alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) should return {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}."""
    assert alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_list_len_2() -> None:
    """alphabetizer(["turtle", "ladybug"]) should return {'t': ['turtle'], 'l': ['ladybug']}."""
    assert alphabetizer(["turtle", "ladybug"]) == {'t': ['turtle'], 'l': ['ladybug']}


def test_alphabetizer_empty_list() -> None:
    """alphabetizer([]) should return {}."""
    assert alphabetizer([]) == {}


# Tests for the update_attendance function. 
attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}


def test_update_attendance_add_student() -> None:
    """update_attendance(attendance_log, "Tuesday" , "Vrinda") should return {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}."""
    assert update_attendance(attendance_log, "Tuesday", "Vrinda") == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_add_student_and_day() -> None:
    """update_attendance(attendance_log, "Wednesday" , "Kaleb") should return {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}."""
    assert update_attendance(attendance_log, "Wednesday", "Kaleb") == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}


def test_update_attendance_empty_dict() -> None:
    """update_attendance({}, "Wednesday", "Kaleb") should return {'Wednesday': ['Kaleb']}."""
    assert update_attendance({}, "Wednesday", "Kaleb") == {'Wednesday': ['Kaleb']}