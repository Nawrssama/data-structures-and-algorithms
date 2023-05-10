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
    with pytest.raises(Exception):
        ll.kth_from_end(2)


# def test_kth_from_end_same_length():
#     ll = LinkedList()
#     ll.head = Node(1)
#     ll.head.next = Node(2)
#     assert ll.kth_from_end(0) == 2


def test_kth_from_end_not_positive_integer():
    ll = LinkedList()
    ll.head = Node(1)
    with pytest.raises(Exception):
        ll.kth_from_end(-1)


# def test_kth_from_end_size_1():
#     ll = LinkedList()
#     ll.head = Node(1)
#     assert ll.kth_from_end(0) == 1


def test_kth_from_end_happy_path():
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    assert ll.kth_from_end(2) == 2
    
def test_zipLists1():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list1.append(2)
    linked_list2 = LinkedList()
    linked_list2.append(5)
    linked_list2.append(9)
    linked_list2.append(4)
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> { 4 } -> NONE"

def test_zipLists2():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list2 = LinkedList()
    linked_list2.append(5)
    linked_list2.append(9)
    linked_list2.append(4)
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 4 } -> NONE"

def test_zipLists3():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list1.append(2)
    linked_list2 = LinkedList()
    linked_list2.append(5)
    linked_list2.append(9)
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 5 } -> { 3 } -> { 9 } -> { 2 } -> NONE"

def test_zipLists_one_list_is_null():
    linked_list1 = LinkedList()
    linked_list1.append(1)
    linked_list1.append(3)
    linked_list1.append(2)
    linked_list2 = LinkedList()
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "{ 1 } -> { 3 } -> { 2 } -> NONE"

def test_zipLists_both_lists_are_null():
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()
    zipList = linked_list1.zipLists(linked_list1, linked_list2)
    assert zipList.to_string() == "NONE"



@pytest.fixture
def p():
    p = LinkedList()
    p.insert('A')
    p.insert('B')
    p.insert('C')
    return p
