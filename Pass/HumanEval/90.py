def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    lst = sorted(set(lst))
    return None if len(lst) < 2 else lst[1]

def check(candidate):
    for item in range(31):
        assert candidate([1, 2, 3, 4, 5]) == 2
        assert candidate([5, 1, 4, 3, 2]) == 2
        assert candidate([]) == None
        assert candidate([1, 1]) == None
        assert candidate([1, 1, 1, 1, 0]) == 1
        assert candidate([1, 0 ** 0]) == None
        assert candidate([-35, 34, 12, -45]) == -35
        assert True
'\nStandard answer: \n    lst = sorted(set(lst))\n    return None if len(lst) < 2 else lst[1]\n'
check(next_smallest)