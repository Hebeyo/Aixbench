def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate(1) == 1
        assert candidate(6) == 21
        assert candidate(11) == 66
        assert candidate(30) == 465
        assert candidate(100) == 5050
'\nStandard answer: \n    return sum(range(n + 1))\n'
check(sum_to_n)