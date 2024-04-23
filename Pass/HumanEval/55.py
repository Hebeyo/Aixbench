def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate(10) == 55
        assert candidate(1) == 1
        assert candidate(8) == 21
        assert candidate(11) == 89
        assert candidate(12) == 144
'\nStandard answer: \n    if n == 0:\n        return 0\n    if n == 1:\n        return 1\n    return fib(n - 1) + fib(n - 2)\n'
check(fib)