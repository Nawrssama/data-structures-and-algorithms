import pytest
from linked_list.linked_list import LinkedList

def test_one():
    ll = LinkedList()
    assert str(ll) == "Empty LinkeList"

def test_two(p):
    assert str(p) == "C -> B -> A ->  None"


def test_three():
    p = LinkedList()
    p.insert("A")
    p.insert("B")
    assert str(p) == "B -> A ->  None"


def test_four(p):
    assert p.includes('A') == True

def test_five(p):
    assert p.includes('D') == False

def test_six(p):
    assert p.head.value == "C"    

    
@pytest.fixture
def p():
    p = LinkedList()
    p.insert('A')
    p.insert('B')
    p.insert('C')
    return p