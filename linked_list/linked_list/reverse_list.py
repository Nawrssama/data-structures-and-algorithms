class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node




def reverse_list(head):
    """
    Reverse a singly linked list and return its new head node.

    """
    if not head:
        return None
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev