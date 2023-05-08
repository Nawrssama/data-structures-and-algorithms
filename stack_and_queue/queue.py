from stack_and_queue.node import Node

class Queue:
    """this clas make a queue and can enqueue and dequeue nodes i also check if the queue is empty and can give the fisrt node in the queue"""
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,value):
        node = Node(value)
        #if the queue is empty
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
 
        #if the queue is empty
        if self.front == None:
            raise IndexError("Error : Empty Queue!")   
        # if the queue contains only one node
        if self.front == self.rear:
            self.rear = None
            #self.front = None
        temp = self.front
        self.front = self.front.next
        temp.next = None

        return temp.value

    def peek(self):
        if self.front == None:
            raise IndexError("Error : Empty Queue!")
        return self.front.value
    
    def is_empty(self):
        return self.front== None
    
    def __str__(self):
        output = ""
        if self.front is None:
            output = "Empty Queue!"
        else:
            current = self.front
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output  