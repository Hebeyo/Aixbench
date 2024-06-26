from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    running_max = None
    result = []
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate([]) == []
        assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
        assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
        assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]
'\nStandard answer: \n    running_max = None\n    result = []\n\n    for n in numbers:\n        if running_max is None:\n            running_max = n\n        else:\n            running_max = max(running_max, n)\n\n        result.append(running_max)\n\n    return result\n'
check(rolling_max)