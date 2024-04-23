def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]
    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)
    return results[-1]
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate(5) == 4
        assert candidate(8) == 28
        assert candidate(10) == 104
        assert candidate(12) == 386
'\nStandard answer: \n    results = [0, 0, 2, 0]\n    if n < 4:\n        return results[n]\n\n    for _ in range(4, n + 1):\n        results.append(results[-1] + results[-2] + results[-3] + results[-4])\n        results.pop(0)\n\n    return results[-1]\n'
check(fib4)