import pytest
from stack_and_queue.stack import Stack
from stack_and_queue.queue import Queue

def test_queue1():
    with pytest.raises(Exception):
        queue = Queue()
        str(queue)
        

def test_queue2():
    queue= Queue()
    queue.enqueue_queue("B")
    queue.enqueue_queue("K")
    queue.enqueue_queue("A")
    expected = "Front --> B  K  A "
    actual = str(queue)
    assert expected == actual
def test_queue3():
    queue=Queue()
    queue.enqueue_queue("B")
    queue.enqueue_queue("K")
    queue.enqueue_queue("A")
    assert queue.peek_queue() == "B"
    assert queue.dequeue_queue() == "B"
    assert queue.peek_queue() == "K"
def test_queue4():
    queue=Queue()
    with pytest.raises(Exception):
        queue.enqueue_queue("B")
        queue.enqueue_queue("K")
        queue.enqueue_queue("A")
        queue.dequeue_queue()
        queue.dequeue_queue()
        queue.dequeue_queue()
        queue.peek_queue()

    
def test_stack1():
        with pytest.raises(Exception):
            stack = Stack()
            str(stack)

def test_stack2():
    stack=Stack()
    stack.push_stack("B")
    stack.push_stack("K")
    stack.push_stack("A")
    expected = "Top --> A  K  B "
    actual = str(stack)
    assert expected == actual
def test_stack3():
    stack=Stack()
    stack.push_stack("B")
    stack.push_stack("K")
    stack.push_stack("A")
    assert stack.peek_stack() == "A"
    assert stack.pop_stack() == "A"
    assert stack.peek_stack() == "K"
def test_stack4():
        with pytest.raises(Exception):
            stack=Stack()
            stack.push_stack("B")
            stack.push_stack("K")
            stack.push_stack("A")
            stack.pop_stack()
            stack.pop_stack()
            stack.pop_stack()
            stack.pop_stack()

