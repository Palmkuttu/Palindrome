from collections import deque


def is_palindrome(value):
    """
    Returns True if value is a palindrome, False otherwise.
    Raises ValueError if value is not a string.
    Uses deque and its pop/popleft methods (no reverse/sort).
    """
    if not isinstance(value, str):
        raise ValueError("value must be a string")

    if value == "":
        return False

    # Normalize: case-insensitive and ignore spaces
    normalized = "".join(ch.lower() for ch in value if not ch.isspace())

    if normalized == "":
        return False

    chars = deque(normalized)

    while len(chars) > 1:
        left = chars.popleft()
        right = chars.pop()
        if left != right:
            return False

    return True
import pytest
from palindrome import is_palindrome


def test_raises_value_error_if_not_string():
    with pytest.raises(ValueError):
        is_palindrome(123)


def test_empty_string_returns_false():
    assert is_palindrome("") is False


def test_a_returns_true():
    assert is_palindrome("a") is True


def test_bb_returns_true():
    assert is_palindrome("bb") is True


def test_abc_returns_false():
    assert is_palindrome("abc") is False


def test_laval_returns_true():
    assert is_palindrome("laval") is True


def test_toronto_returns_false():
    assert is_palindrome("toronto") is False


def test_sentence_palindrome_returns_true():
    assert is_palindrome("Able was I ere I saw Elba") is True

