def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    l = sorted(l)
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 0:
                return True
    return False
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate([1, 3, 5, 0]) == False
        assert candidate([1, 3, -2, 1]) == False
        assert candidate([1, 2, 3, 7]) == False
        assert candidate([2, 4, -5, 3, 5, 7]) == True
        assert candidate([1]) == False
        assert candidate([-3, 9, -1, 3, 2, 30]) == True
        assert candidate([-3, 9, -1, 3, 2, 31]) == True
        assert candidate([-3, 9, -1, 4, 2, 30]) == False
        assert candidate([-3, 9, -1, 4, 2, 31]) == False
'\nStandard answer: \n    for i, l1 in enumerate(l):\n        for j in range(i + 1, len(l)):\n            if l1 + l[j] == 0:\n                return True\n    return False\n'
check(pairs_sum_to_zero)