from stack_and_queue.node import Node


class Stack:
    """this class make a stack ,add to it ,remove from it ,get the top value,get the size and check if its empty """
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top is not None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            raise ValueError("Error : Empty Stack!")

    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise ValueError("Error : Empty Stack!")
        
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def __str__(self):
        output = ""
        if self.top is None:
            output = "Empty Stack!"
        else:
            current = self.top
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output  