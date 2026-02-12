import pytest
from palindrome import is_palindrome
def test_raises_value_error_when_not_string():
    with pytest.raises(ValueError):
        is_palindrome(123)
def test_empty_string_returns_false():
    assert is_palindrome("") is False
    
def test_single_character_returns_true():
    assert is_palindrome("a") is True

def test_two_same_letters_returns_true():
    assert is_palindrome("bb") is True

def test_simple_false_case():
    assert is_palindrome("abc") is False

def test_simple_true_case():
    assert is_palindrome("laval") is True

def test_non_palindrome_word():
    assert is_palindrome("toronto") is False

def test_phrase_palindrome():
    assert is_palindrome("Able was I ere I saw Elba") is True

def test_case_insensitive():
    assert is_palindrome("RaceCar") is True


def test_string_with_spaces():
    assert is_palindrome("nurses run") is True


