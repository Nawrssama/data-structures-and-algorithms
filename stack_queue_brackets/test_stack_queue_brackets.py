import pytest
from stack_queue_brackets import validatebrackets
def test_one():
    s = "()"
    actual= validatebrackets(s)
    expected =True
    assert actual == expected
def test_two():
    s = "(){"
    actual= validatebrackets(s)
    expected =False
    assert actual == expected
def test_three():
    s = "(){;jaij}"
    actual= validatebrackets(s)
    expected =True
    assert actual == expected
def test_four():
    s = ")[]"
    actual= validatebrackets(s)
    expected =False
    assert actual == expected