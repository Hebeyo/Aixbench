def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    results = [0, 0, 1]
    if n < 3:
        return results[n]
    for _ in range(3, n + 1):
        results.append(results[-1] + results[-2] + results[-3])
        results.pop(0)
    return results[-1]
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate(2) == 1
        assert candidate(1) == 0
        assert candidate(5) == 4
        assert candidate(8) == 24
        assert candidate(10) == 81
        assert candidate(12) == 274
        assert candidate(14) == 927
'\nStandard answer: \n    if n == 0:\n        return 0\n    if n == 1:\n        return 0\n    if n == 2:\n        return 1\n    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)\n'
check(fibfib)