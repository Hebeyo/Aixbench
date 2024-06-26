def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    result = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            result += lst[i]
    return result

def check(candidate):
    for item in range(31):
        assert candidate([4, 88]) == 88
        assert candidate([4, 5, 6, 7, 2, 122]) == 122
        assert candidate([4, 0, 6, 7]) == 0
        assert candidate([4, 4, 6, 8]) == 12
'\nStandard answer: \n    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])\n'
check(add)