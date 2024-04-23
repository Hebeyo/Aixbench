def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate(6) == False
        assert candidate(101) == True
        assert candidate(11) == True
        assert candidate(13441) == True
        assert candidate(61) == True
        assert candidate(4) == False
        assert candidate(1) == False
        assert candidate(5) == True
        assert candidate(11) == True
        assert candidate(17) == True
        assert candidate(5 * 17) == False
        assert candidate(11 * 7) == False
        assert candidate(13441 * 19) == False
'\nStandard answer: \n    if n < 2:\n        return False\n    for k in range(2, n - 1):\n        if n % k == 0:\n            return False\n    return True\n'
check(is_prime)