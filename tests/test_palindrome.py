# python test palindrome

from questions import palindrome


def test_is_palindrome():
    test_string = "abcba"
    assert palindrome.is_palindrome(test_string)


def test_is_not_palindrome():
    test_string = "qsfesb"
    assert not palindrome.is_palindrome(test_string)
