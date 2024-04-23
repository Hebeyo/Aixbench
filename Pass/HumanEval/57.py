def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate([1, 2, 4, 10]) == True
        assert candidate([1, 2, 4, 20]) == True
        assert candidate([1, 20, 4, 10]) == False
        assert candidate([4, 1, 0, -10]) == True
        assert candidate([4, 1, 1, 0]) == True
        assert candidate([1, 2, 3, 2, 5, 60]) == False
        assert candidate([1, 2, 3, 4, 5, 60]) == True
        assert candidate([9, 9, 9, 9]) == True
'\nStandard answer: \n    if l == sorted(l) or l == sorted(l, reverse=True):\n        return True\n    return False\n'
check(monotonic)