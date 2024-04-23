def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    return max(l)
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate([1, 2, 3]) == 3
        assert candidate([5, 3, -5, 2, -3, 3, 9, 0, 124, 1, -10]) == 124
'\nStandard answer: \n    m = l[0]\n    for e in l:\n        if e > m:\n            m = e\n    return m\n'
check(max_element)