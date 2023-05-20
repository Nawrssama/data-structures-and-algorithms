class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def pre_order(self, root, list = None):
        if list is None:
            list = []
        if root is not None:
            list.append(root.value)
         
            self.pre_order(root.left, list)
         
            self.pre_order(root.right, list)
        return list

    def in_order(self, root, list = None):
        if list is None:
            list = []
        if root is not None:
            self.in_order(root.left, list)

            list.append(root.value)

            self.in_order(root.right, list)
        return list
    
    def post_order(self, root, list = None):
        if list is None:
            list = []
        if root is not None:
            self.post_order(root.left, list)

            self.post_order(root.right, list)

            list.append(root.value)
        return list
    
class Binary_Search_Tree(Tree): # inhertenc
    def __init__(self):
        super().__init__()# to pass everything that is need to be done from the parents
        
    def add(self, root, value):

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
        if root is None:
            return False
        elif value == root.value:
            return True
        elif value < root.value:
            return self.Contains(root.left, value)
        else:
            return self.Contains(root.right, value)


# if __name__ == '__main__':
#     bst = Binary_Search_Tree()
#     bst.add(bst.root ,6)
#     bst.add(bst.root ,3)
#     bst.add(bst.root ,7)
#     bst.add(bst.root ,1)
#     bst.add(bst.root ,4)
#     bst.add(bst.root ,9)
#     print(bst.root.value)
#     print(bst.pre_order(bst.root))
#     print(bst.in_order(bst.root))
#     print(bst.post_order(bst.root))

#     print(bst.Contains(bst.root, 7))
#     print(bst.Contains(bst.root, 10))