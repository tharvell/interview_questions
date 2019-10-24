# Simple interview question palindrome checker


def is_palindrome(string):
    """ Check if a string is a palindrome

    Args:
        string: to be checked for palindrome propertiespip install flake8.

    Returns:
        Boolean

    """
    return string == string[::-1]
