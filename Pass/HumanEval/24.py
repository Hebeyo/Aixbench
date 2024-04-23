def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n % i == 0:
            return i
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate(3) == 1
        assert candidate(7) == 1
        assert candidate(10) == 5
        assert candidate(100) == 50
        assert candidate(49) == 7
'\nStandard answer: \n    for i in reversed(range(n)):\n        if n % i == 0:\n            return i\n'
check(largest_divisor)