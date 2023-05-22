import pytest
from Trees.Trees import *

def test_1():
    tree= Tree()
    actual = tree.pre_order(tree.root)
    expected = []
    assert actual==expected

def test_2():
    tree= Binary_Search_Tree()
    tree.add(tree.root, 5)
    tree.add(tree.root, 4)
    tree.add(tree.root, 7)
    actual = tree.in_order(tree.root)
    expected = [4,5,7]
    assert actual==expected   

def test_3(BST):
    assert BST.pre_order(BST.root) == [5,3,2,4,7,6,8]


def test_4(BST):
    assert BST.in_order(BST.root) == [2,3,4,5,6,7,8]

def test_5(BST):
    assert BST.post_order(BST.root) == [2,4,3,6,8,7,5]    


def test_6(BST):
    assert BST.Contains(BST.root, 8) == True

def test_7(BST):
    assert BST.Contains(BST.root, 9) == False     
  

@pytest.fixture
def BST():
    BST= Binary_Search_Tree()
    BST.add(BST.root, 5)
    BST.add(BST.root, 3)
    BST.add(BST.root, 2)
    BST.add(BST.root, 4)
    BST.add(BST.root, 7)
    BST.add(BST.root, 6)
    BST.add(BST.root, 8)
    return BST