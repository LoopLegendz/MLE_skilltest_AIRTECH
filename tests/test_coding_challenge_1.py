import pytest
from src.coding_challenge_1 import concatenate

def test_ints_sum():
    assert concatenate([1, 5, 3, 4]) == 13

def test_floats_and_ints_sum():
    assert concatenate([5.5, 2, 3.25]) == pytest.approx(10.75)

def test_strings_joined():
    assert concatenate(["i", "am", "victor"]) == "i|am|victor"

def test_bools_to_string():
    assert concatenate([True, False, True]) == "101"
    assert concatenate([False, False]) == "00"

def test_single_list_returns_same_content():
    list = [22, "hello", True]
    assert concatenate([list]) == list

def test_lists_flattened():
    assert concatenate([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]

def test_dicts_merged():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    assert concatenate([d1, d2]) == {"a": 1, "b": 3, "c": 4}

def test_empty_raises_value_error():
    with pytest.raises(ValueError):
        concatenate([])

def test_mixed_types_raise_type_error():
    with pytest.raises(TypeError):
        concatenate([1, "two", 3])

    with pytest.raises(TypeError):
        concatenate([[1, 2], {"a": 1}])
