from stack_and_queue.node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __str__(self):
        if self.front:
            queue_str = "Front -->"
            node = self.front
            while node:
              queue_str += f" {node.value} "
              node = node.next
            return queue_str    
        else:
            raise Exception("Empty Queue")

   
    def enqueue_queue(self,value):
        """
        adds a new node with the given value to the back of the queue with an O(1) Time performance.
        
        """
        node = Node(value)

        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size +=1    


    def dequeue_queue(self):
        """
        Removes the node from the front of the queue
  
        """
        if self.front == None:
            raise Exception("Error : This queue is empty") 

        if self.front == self.rear:
            self.rear = None

        temp = self.front
        self.front = self.front.next
        temp.next = None
        self.size -=1
        return temp.value


    def peek_queue(self):
        """
        Gives the value of the node at the front of the queue
    
        """
        if not self.front:
            raise Exception("Error : This queue is empty") 
        return self.front.value    
    

    def is_empty_queue(self):
        """
        Checks if the queue is empty or not
    
        """
        return True if self.size == 0 else False