# Do they add up ?


def do_they_add_up(numbers, number):
    """

    Args:

    Returns:

    Raises: 

    """
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == number:
                return True
    return False
