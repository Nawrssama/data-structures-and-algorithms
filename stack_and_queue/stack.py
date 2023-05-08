from stack_and_queue.node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0


    def __str__(self):
        if self.top:
            stack_str = "Top -->"
            node = self.top
            while node:
              stack_str += f" {node.value} -->"
              node = node.next
            return stack_str    
        else:
            raise Exception("Empty Queue")


    
    def push_stack(self,value):
        """
        Adds a node to the top of the stack in O(1) time complexity
   
        """
        node = Node(value)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node 
        self.size += 1      

   
    def pop_stack(self):
        """
        Removes the node at the top of the stack with time complexity of O(1)
    
        """   
        if self.top:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.size -= 1
            return temp.value
        else:
            raise Exception("Error : empty stack")

     
    def peek_stack(self):
        """
        Gives the value of the node at the top of the stack
    
        """   
        if self.top:
            return self.top.value
        else:
            raise Exception("Error : empty stack")
        
    def get_size(self):
        return self.size

  
    def is_empty_stack(self):
        """
        checks if the stack is empty or not
        
        """ 
        return True if self.size == 0 else False