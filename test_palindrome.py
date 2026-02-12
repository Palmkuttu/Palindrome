# test_palindrome.py
import pytest
from palindrome import is_palindrome

def test_raises_value_error_when_not_a_string():
    with pytest.raises(ValueError):
        is_palindrome(123)

def test_empty_string_is_false():
    assert is_palindrome("") is False

def test_single_character_is_true():
    assert is_palindrome("a") is True

def test_two_same_characters_is_true():
    assert is_palindrome("bb") is True

def test_abc_is_false():
    assert is_palindrome("abc") is False

def test_laval_is_true():
    assert is_palindrome("laval") is True

def test_toronto_is_false():
    assert is_palindrome("toronto") is False

def test_phrase_palindrome_is_true():
    assert is_palindrome("Able was I ere I saw Elba") is True

