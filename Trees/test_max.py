from Trees.Trees import *
import pytest

def test_1(tree1):
    assert tree1.find_maximum_value(tree1.root) == 8  

def test_2():
    empty_tree = Tree()
    assert empty_tree.find_maximum_value(empty_tree.root) == 'tree is empty' 

# def test2(tree2):
#     assert tree2.maximum_value(tree2.root) == -1


  







@pytest.fixture
def tree1():
    BST= Binary_Search_Tree()
    BST.add(BST.root, 5)
    BST.add(BST.root, 3)
    BST.add(BST.root, 2)
    BST.add(BST.root, 4)
    BST.add(BST.root, 7)
    BST.add(BST.root, 6)
    BST.add(BST.root, 8)
    return BST

# @pytest.fixture
# def tree2():
#     BST= Binary_Search_Tree()
#     BST.add(BST.root, -1)
#     BST.add(BST.root, -5)
#     BST.add(BST.root, -4)
#     BST.add(BST.root, -9)
#     BST.add(BST.root, -7)
#     BST.add(BST.root, -3)
#     BST.add(BST.root, -6)
#     return BST