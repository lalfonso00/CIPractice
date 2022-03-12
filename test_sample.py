# content of test_sample.py
import pytest
from app import sortWords


def func(x):
    sorts = sortWords()
    return sorts.sortInput(x)


def test_answer():
    assert func("Good Morning") == ['good', 'morning']


def test_answer_2():
    assert func("Kindness always pays off") == [
        'always', 'kindness', 'off', 'pays']


# def test_answer_3():
#     assert func("Kindness always pays off") == [
#         'always', 'kindness', 'off', 'pays']
