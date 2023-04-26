import pytest
from linked_list.linked_list import LinkedList, Node


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


def test_kth_from_end_greater_than_length():
    ll = LinkedList()
    ll.head = Node(1)
    assert ll.kth_from_end(2) == None


def test_kth_from_end_same_length():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    assert ll.kth_from_end(2) == 1


def test_kth_from_end_not_positive_integer():
    ll = LinkedList()
    ll.head = Node(1)
    assert ll.kth_from_end(-1) == None


def test_kth_from_end_size_1():
    ll = LinkedList()
    ll.head = Node(1)
    assert ll.kth_from_end(1) == 1


def test_kth_from_end_happy_path():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    assert ll.kth_from_end(2) == 3


@pytest.fixture
def p():
    p = LinkedList()
    p.insert('A')
    p.insert('B')
    p.insert('C')
    return p
