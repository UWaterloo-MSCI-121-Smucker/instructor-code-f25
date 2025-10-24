import pytest
from list_functions import count
from list_functions import reverse


def test_reverse():
    values = [1,2,3]
    reverse(values)
    assert values == [3, 2, 1]
 


def test_count_multiples():
    values = [5, 2, 8, 8, 0, -1, 10]
    assert count(values, 8) == 2
    assert count(values, 5) == 1
    assert count(values, 10) == 1

def test_count_empty():
    empty_list = list()
    assert count(empty_list, 10) == 0

def test_count_one():
    one_elt = [5]
    assert count(one_elt, 5) == 1
    assert count(one_elt, 6) == 0
