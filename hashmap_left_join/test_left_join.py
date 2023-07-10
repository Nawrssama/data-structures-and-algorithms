import pytest
from hashmap_left_join.hashmap_left_join import left_join


@pytest.fixture
def synonyms():
    return {
        "happy": "joyful",
        "sad": "unhappy",
        "big": "large",
        "small": "tiny"
    }

@pytest.fixture
def antonyms():
    return {
        "happy": "sad",
        "big": "small",
        "rich": "poor"
    }

def test_left_join_with_matching_keys(synonyms, antonyms):
    result = left_join(synonyms, antonyms)
    assert result["happy"] == ("joyful", "sad")
    assert result["big"] == ("large", "small")

def test_left_join_with_missing_antonyms(synonyms, antonyms):
    result = left_join(synonyms, antonyms)
    assert result["sad"] == ("unhappy", None)

def test_left_join_with_missing_synonyms(synonyms, antonyms):
    result = left_join(synonyms, antonyms)
    assert "rich" not in result  # Verify that the key is not present in the result

def test_left_join_with_empty_hashmaps():
    empty_synonyms = {}
    empty_antonyms = {}
    result = left_join(empty_synonyms, empty_antonyms)
    assert result == {}

def test_left_join_with_empty_synonyms_hashmap(synonyms, antonyms):
    empty_synonyms = {}
    result = left_join(empty_synonyms, antonyms)
    print(result)
    assert result == {}

