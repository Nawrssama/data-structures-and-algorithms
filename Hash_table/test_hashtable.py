import pytest
from Hash_table.hash_table import Hashtable

def test_set_get():
    ht = Hashtable()
    ht.set('apple', 5)
    assert ht.get('apple') == 5

def test_set_overwrite_get():
    ht = Hashtable()
    ht.set('apple', 5)
    ht.set('apple', 10)
    assert ht.get('apple') == 10

def test_get_nonexistent_key():
    ht = Hashtable()
    assert ht.get('grape') is None

def test_keys():
    ht = Hashtable()
    ht.set('apple', 5)
    ht.set('banana', 7)
    ht.set('cherry', 3)
    expected_keys = ['apple', 'banana', 'cherry']
    assert sorted(ht.keys()) == expected_keys

def test_collision_handling():
    ht = Hashtable()
    ht.set('dog', 10)
    ht.set('god', 20)
    assert ht.get('dog') == 10
    assert ht.get('god') == 20

def test_hash_range():
    ht = Hashtable()
    key = 'test'
    index = ht.hash(key)
    assert 0 <= index < ht.size

@pytest.fixture
def ht():
    return Hashtable()
