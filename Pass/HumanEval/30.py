def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e > 0]
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate([-1, -2, 4, 5, 6]) == [4, 5, 6]
        assert candidate([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 3, 9, 123, 1]
        assert candidate([-1, -2]) == []
        assert candidate([]) == []
'\nStandard answer: \n    return [e for e in l if e > 0]\n'
check(get_positive)