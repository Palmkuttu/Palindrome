# palindrome.py
from collections import deque

def is_palindrome(value):
    """
    Return True if `value` is a palindrome, else False.

    Rules for this assignment:
    - Raise ValueError if value is not a str
    - Return False for empty string
    - Ignore spaces and case for phrase palindromes
    - Use deque and its methods (popleft/pop) to compare ends
    """
    if not isinstance(value, str):
        raise ValueError("value must be a string")

    # Remove spaces and normalize case (so phrases work)
    cleaned = "".join(ch.lower() for ch in value if not ch.isspace())

    if cleaned == "":
        return False

    d = deque(cleaned)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

