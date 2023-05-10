import pytest
from stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter
 
def test_1 (AA):
    assert AA.dequeue("cat") == {"species" : "cat" , "name": "ash"}

def test_2 (AA):
    assert AA.dequeue("dog") == {"species" : "dog" , "name": "warwick"}

def test_3():
    AS = AnimalShelter()
    assert AS.dequeue("wolf") == None


@pytest.fixture
def AA():
    AA = AnimalShelter()
    AA.enqueue({"species" : "cat" , "name": "ash"})
    AA.enqueue({"species" : "cat" , "name": "lux"})
    AA.enqueue({"species" : "cat" , "name": "neeko"})
    AA.enqueue({"species" : "dog" , "name": "warwick"})
    AA.enqueue({"species" : "dog" , "name": "garen"})
    AA.enqueue({"species" : "dog" , "name": "viego"})
    return AA   