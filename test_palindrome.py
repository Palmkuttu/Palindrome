import palindrome

def test_true():
    assert palindrome.is_palindrome("madam") is True

def test_false():
    assert palindrome.is_palindrome("hello") is False

def test_empty_string_returns_false():
    assert is_palindrome("") is False

