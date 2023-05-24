from stack_and_queue.queue import Queue
class Node:
    '''
    Represents a node in a binary tree.
    Attributes:
    value: The value stored in the node.
    left: Reference to the left child node.
    right: Reference to the right child node.
    
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    """
    Represents a binary tree.

    Attributes:
    root: Reference to the root node of the tree.
    """
    def __init__(self):
        self.root = None
        self.max = None

    def pre_order(self, root, list = None):
        """
        Performs a pre-order traversal of the tree and returns a list of node values.

        Args:
        root: The root node of the current traversal.
        list: A list to store the node values (optional).

        Returns:
        A list of node values in pre-order traversal.
        """
        if list is None:
            list = []
        if root is not None:
            list.append(root.value)
         
            self.pre_order(root.left, list)
         
            self.pre_order(root.right, list)
        return list

    def in_order(self, root, list = None):
        """
        Performs an in-order traversal of the tree and returns a list of node values.

        Args:
        root: The root node of the current traversal.
        list: A list to store the node values (optional).

        Returns:
        A list of node values in in-order traversal.
        """
        if list is None:
            list = []
        if root is not None:
            self.in_order(root.left, list)

            list.append(root.value)

            self.in_order(root.right, list)
        return list
    
    def post_order(self, root, list = None):
        """
        Performs a post-order traversal of the tree and returns a list of node values.

        Args:
        root: The root node of the current traversal.
        list: A list to store the node values (optional).

        Returns:
        A list of node values in post-order traversal.
        """
        if list is None:
            list = []
        if root is not None:
            self.post_order(root.left, list)

            self.post_order(root.right, list)

            list.append(root.value)
        return list

    def find_maximum_value(self, root):
        '''
        Finds the maximum value in the tree.

        this function travers into the tree and compare the root value with the max_value variable and if the root is bigger the variable will take the value of the root

        Args:
        root: The root node of the current traversal.

        Returns:
        The maximum value in the tree.
        '''
        if root is None:
            return 'tree is empty'
        if self.max is None:
            self.max = root.value
        if root is not None:
            if root.value > self.max:
                self.max = root.value
            if root.left:
                self.find_maximum_value(root.left)
            if root.right:
                self.find_maximum_value(root.right)
        return self.max
    
  
class Binary_Search_Tree(Tree): # inhertenc
    """
    Represents a binary search tree (BST), which is a type of binary tree.
    """
    def __init__(self):
        super().__init__()# to pass everything that is need to be done from the parents
        
    def add(self, root, value):
        '''
        Inserts a new node with the given value into the BST.
        '''
        if root is None: # root from bst.root will take the root of def __init__ 
            # print(root)
            self.root = Node(value)
            
        else:
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                 
                else:
                    self.add(root.left,value)
            else :
                if root.right is None:
                    root.right = Node(value)
                 
                else:
                    self.add(root.right,value)
        
    def Contains(self, root, value):
        '''
        Checks if a node with the given value exists in the BST.
        '''
        if root is None:
            return False
        elif value == root.value:
            return True
        elif value < root.value:
            return self.Contains(root.left, value)
        else:
            return self.Contains(root.right, value)


def breadth_first(tree):
    """
    Perform breadth-first traversal on a binary tree and return a list of its values.

    Args:
        tree: The binary tree to traverse.

    Returns:
        A list of values in the binary tree in breadth-first order.
    """
    queue = Queue()
    values = []
    if tree.root is None:
        return 'the tree is empty'
    queue.enqueue(tree.root)
    while not queue.is_empty():
        node = queue.dequeue()
        values.append(node.value)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
    return values

if __name__ == '__main__':
    tree1 = Tree()

    node1 = Node(5)
    tree1.root = node1

    node2 = Node(4)
    tree1.root.left = node2

    node3 = Node(9)
    tree1.root.right = node3

    node4 = Node(12)
    tree1.root.left.left = node4

    node5 = Node(6)
    tree1.root.left.right = node5

    node6 = Node(15)
    tree1.root.right.left = node6
    # print(tree1.find_maximum_value())
    print(breadth_first(tree1))