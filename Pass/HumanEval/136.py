def largest_smallest_integers(lst):
    """
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    """
    smallest = None
    largest = None
    for i in lst:
        if i < 0:
            if smallest is None or i > smallest:
                smallest = i
        elif i > 0:
            if largest is None or i < largest:
                largest = i
    return (smallest, largest)

def check(candidate):
    for item in range(31):
        assert candidate([2, 4, 1, 3, 5, 7]) == (None, 1)
        assert candidate([2, 4, 1, 3, 5, 7, 0]) == (None, 1)
        assert candidate([1, 3, 2, 4, 5, 6, -2]) == (-2, 1)
        assert candidate([4, 5, 3, 6, 2, 7, -7]) == (-7, 2)
        assert candidate([7, 3, 8, 4, 9, 2, 5, -9]) == (-9, 2)
        assert candidate([]) == (None, None)
        assert candidate([0]) == (None, None)
        assert candidate([-1, -3, -5, -6]) == (-1, None)
        assert candidate([-1, -3, -5, -6, 0]) == (-1, None)
        assert candidate([-6, -4, -4, -3, 1]) == (-3, 1)
        assert candidate([-6, -4, -4, -3, -100, 1]) == (-3, 1)
        assert True
'\nStandard answer: \n    smallest = list(filter(lambda x: x < 0, lst))\n    largest = list(filter(lambda x: x > 0, lst))\n    return (max(smallest) if smallest else None, min(largest) if largest else None)\n'
check(largest_smallest_integers)