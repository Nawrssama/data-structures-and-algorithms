import pytest
from repeated_word.repeated import repeated_word

def test_repeated_word_basic():
    input_string = "This is a test string to test the function."
    result = repeated_word(input_string)
    assert result == "test"

def test_repeated_word_no_repeated_word():
    input_string = "There are no repeated words in this sentence."
    result = repeated_word(input_string)
    assert result is None

def test_repeated_word_case_insensitive():
    input_string = "The weather is sunny. The weather is SUnny."
    result = repeated_word(input_string)
    assert result == "the"

def test_repeated_word_with_punctuation():
    input_string = "This, is! a test string. It has punctuation, but test it we shall!"
    result = repeated_word(input_string)
    assert result == "test"