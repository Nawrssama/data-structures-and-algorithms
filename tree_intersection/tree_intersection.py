from Trees.Trees import Tree

def tree_intersection(tree1, tree2):
    """
    Returns a list of intersection values between two binary trees.

    Args:
        tree1: The first binary tree.
        tree2: The second binary tree.

    Returns:
        A list of intersection values found in both trees.
    """
    obj = {}
    data = Tree()
    first_tree = data.in_order(tree1)
    for x in first_tree:
        obj[x] = x
    second_tree = data.in_order(tree2)
    return [x for x in second_tree if x in obj]