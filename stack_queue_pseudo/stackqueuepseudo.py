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

    def enqueue(self, value):
        self.inbox.push_stack(value)

    def dequeue(self):
        if self.outbox.is_empty_stack():
            if self.inbox.is_empty_stack():
                return "The Queue is empty"
            while not self.inbox.is_empty_stack():
                self.outbox.push_stack(self.inbox.pop_stack())
        return self.outbox.pop_stack()
        

