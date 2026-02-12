import palindrome

def test_true():
    assert palindrome.is_palindrome("madam") == True

def test_false():
    assert palindrome.is_palindrome("hello") == False
