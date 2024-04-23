def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    ret = []
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.append(e1)
    return sorted(list(set(ret)))
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
        assert candidate([5, 3, 2, 8], [3, 2]) == [2, 3]
        assert candidate([4, 3, 2, 8], [3, 2, 4]) == [2, 3, 4]
        assert candidate([4, 3, 2, 8], []) == []
'\nStandard answer: \n    ret = set()\n    for e1 in l1:\n        for e2 in l2:\n            if e1 == e2:\n                ret.add(e1)\n    return sorted(list(ret))\n'
check(common)