import pytest
from stack_queue_pseudo.stackqueuepseudo import Pseudo_queue

def test_PS_1 (AA):
    assert AA.dequeue() == 'A'

def test__PS_2():
    PQ = Pseudo_queue()
    assert PQ.dequeue() == "The Queue is empty"

def test_PS_3(AA):
    
    assert str(AA.inbox) == "Top --> C --> B --> A -->"

def test_PS_4(AA):
    AA.dequeue()
    assert str(AA.outbox) ==  "Top --> B --> C -->" 

@pytest.fixture
def AA():
    AA = Pseudo_queue()
    AA.enqueue('A')
    AA.enqueue('B')
    AA.enqueue('C')
    return AA