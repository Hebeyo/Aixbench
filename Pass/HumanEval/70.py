def strange_sort_list(lst):
    """
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    """
    res = []
    while lst:
        res.append(min(lst))
        lst.remove(res[-1])
        if lst:
            res.append(max(lst))
            lst.remove(res[-1])
    return res

def check(candidate):
    for item in range(31):
        assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
        assert candidate([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
        assert candidate([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
        assert candidate([5, 6, 7, 8, 9, 1]) == [1, 9, 5, 8, 6, 7]
        assert candidate([5, 5, 5, 5]) == [5, 5, 5, 5]
        assert candidate([]) == []
        assert candidate([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 8, 2, 7, 3, 6, 4, 5]
        assert candidate([0, 2, 2, 2, 5, 5, -5, -5]) == [-5, 5, -5, 5, 0, 2, 2, 2]
        assert candidate([111111]) == [111111]
        assert True
'\nStandard answer: \n    res, switch = [], True\n    while lst:\n        res.append(min(lst) if switch else max(lst))\n        lst.remove(res[-1])\n        switch = not switch\n    return res\n'
check(strange_sort_list)