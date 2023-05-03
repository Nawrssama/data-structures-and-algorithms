import pytest
from linked_list.reverse_list import *


def test_empty_list():
    assert reverse_list(None) == None

def test_single_element_list():
    head = Node(1)
    assert reverse_list(head) == head

def test_multiple_element_list():
    head = Node(1, Node(2, Node(3, Node(4))))
    new_head = reverse_list(head)
    assert new_head.value == 4
    assert new_head.next.value == 3
    assert new_head.next.next.value == 2
    assert new_head.next.next.next.value == 1
    assert new_head.next.next.next.next == None

def test_duplicate_element_list():
    head = Node(1, Node(2, Node(2, Node(1))))
    new_head = reverse_list(head)
    assert new_head.value == 1
    assert new_head.next.value == 2
    assert new_head.next.next.value == 2
    assert new_head.next.next.next.value == 1
    assert new_head.next.next.next.next == None
