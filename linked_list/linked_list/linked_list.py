class Node:
    def __init__(self, value):
        """
        Initialize a Node instance.

        Parameters:
        - value: Any data type
          The value to be stored in the node.
        """
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        """
        Initialize a LinkedList instance.
        """
        self.head = None

    def insert(self, value):
        """
        Insert a node with the given value at the beginning of the linked list.

        Parameters:
        - value: Any data type
          The value to be stored in the new node.
        """

        node = Node(value)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def includes(self, key):
        """
        Check whether the linked list contains a node with the given value.

        Parameters:
        - key: Any data type
          The value to search for.

        Returns:
        - bool
          True if the value is found in any node of the linked list, False otherwise.
        """

        temp = self.head
        if temp is None:
            return False
        while temp is not None:
            if temp.value == key:
                return True
            temp = temp.next
        return False

    def append(self, value):
        """
        Insert a node with the given value at the end of the linked list.

        Parameters:
        - value: Any data type
          The value to be stored in the new node.
        """

        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert_after(self, target, value):
        """
       Insert a node with the given value after the first node with the given target value.

       Parameters:
       - target: Any data type
         The value of the node after which the new node should be inserted.
       - value: Any data type
         The value to be stored in the new node.
       """

        if self.includes(target):
            node = Node(value)
            if self.head == None:
                self.insert(value)

            else:
                currnet = self.head
                while currnet.value is not target:
                    currnet = currnet.next
                target = currnet
                node.next = target.next
                target.next = node
        else:
            print("this target value does not exists")

    def insert_before(self, target, value):
        """
       Insert a node with the given value before the first node with the given target value.

       Parameters:
       - target: Any data type
         The value of the node before which the new node should be inserted.
       - value: Any data type
         The value to be stored in the new node.
       """

        if self.includes(target):
            node = Node(value)
            if self.head == None or self.head.value == target:
                self.insert(value)

            else:
                currnet = self.head
                while currnet.next.value is not target:
                    currnet = currnet.next
                target = currnet
                node.next = target.next
                target.next = node
        else:
            print("this target value does not exists")

    def __str__(self):
        """
        Generate a string representation of the linked list.

        Returns:
        - str
          A string representation of the linked list.
        """
        output = ""
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while (current):
                output += f'{current.value} -> '
                current = current.next

            output += " None"
        return output

    def kth_from_end(self, k):
        """
    Returns the value of the kth node from the end of the linked list.

    Args:
    - self: the linked list object
    - k (int): the position of the node, counting from the end of the list

    Returns:
    - The value of the kth node from the end of the list, or None if k is less than or equal to 0, or if k is greater than the length of the list.

        """
        if k <= 0:
            return None

        # Get the length of the linked list
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next

        if k > length:
            return None

        # Calculate the position of the kth node from the beginning
        position = length - k

        # Traverse the linked list to find the kth node from the beginning
        current = self.head
        for i in range(position):
            current = current.next

        return current.value

    def find_middle(self):
        """
    Returns the value of the middle node of the linked list.

    Args:
    - self: the linked list object

    Returns:
    - The value of the middle node of the list, or None if the list is empty.

        """
        if not self.head:
            return None

        slow = self.head
        fast = self.head

        # Traverse the linked list using two pointers,
        # one moving at half the speed of the other.
        # When the fast pointer reaches the end of the
        # list, the slow pointer will be at the middle node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.value
