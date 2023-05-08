from stack_and_queue.stack import Stack

class Pseudo_queue:
    """
    A class that implements a queue using two stacks.

    Attributes:
    - inbox (Stack): A stack used to store incoming elements.
    - outbox (Stack): A stack used to store elements in the order they will be dequeued.

    Methods:
    - enqueue(value): Adds a new element to the queue.
    - dequeue(): Removes and returns the first element in the queue, or returns "The Queue is empty" if the queue is empty.
    
    """
    def __init__(self):
       self.inbox = Stack()
       self.outbox = Stack()

    def enqueue(self,value):
         self.inbox.push(value)

    def dequeue(self):
         if self.inbox.is_empty() and self.outbox.is_empty():
              return "Pseude Queue is Empty!"
         if self.outbox.is_empty() and not self.inbox.is_empty():
                  inbox_size = self.inbox.get_size()
                  for x in range(inbox_size):
                        self.outbox.push(self.inbox.pop())
                  return self.outbox.pop()
         if not self.outbox.is_empty():             
               return self.outbox.pop()

