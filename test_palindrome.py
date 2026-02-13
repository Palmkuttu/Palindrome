import palindrome
def test_true():
    assert palindrome.is_palindrome("laval") is True
def test_false():
    assert palindrome.is_palindrome("toronto") is False
