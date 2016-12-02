def is_odd(num):
    """
    >>> is_odd(1)
    True
    """

    if num % 2 == 0:
        return False
    else:
        return True


def is_divisible(num1, num2):
    """
    >>> is_divisible(4, 3)
    True

    >>>

    """

    if num1 % num2 == 0:
        return True
    else:
        return False

def is_palindrome(word):
    """
    >>> is_palindrome("dad")
    True

    >>>

    """
    return word == word[::-1]

def main():
    print(is_odd(3))
    print(is_divisible(4,3))
    print(is_palindrome("dad"))

main()
