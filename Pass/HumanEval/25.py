from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    result = []
    i = 2
    while i <= n:
        if n % i == 0:
            result.append(i)
            n //= i
        else:
            i += 1
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate(2) == [2]
        assert candidate(4) == [2, 2]
        assert candidate(8) == [2, 2, 2]
        assert candidate(3 * 19) == [3, 19]
        assert candidate(3 * 19 * 3 * 19) == [3, 3, 19, 19]
        assert candidate(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19]
        assert candidate(3 * 19 * 19 * 19) == [3, 19, 19, 19]
        assert candidate(3 * 2 * 3) == [2, 3, 3]
'\nStandard answer: \n    import math\n    fact = []\n    i = 2\n    while i <= int(math.sqrt(n) + 1):\n        if n % i == 0:\n            fact.append(i)\n            n //= i\n        else:\n            i += 1\n\n    if n > 1:\n        fact.append(n)\n    return fact\n'
check(factorize)