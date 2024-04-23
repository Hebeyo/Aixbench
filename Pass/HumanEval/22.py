from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    result = []
    for v in values:
        if isinstance(v, int):
            result.append(v)
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate([]) == []
        assert candidate([4, {}, [], 23.2, 9, 'adasd']) == [4, 9]
        assert candidate([3, 'c', 3, 3, 'a', 'b']) == [3, 3, 3]
'\nStandard answer: \n    return [x for x in values if isinstance(x, int)]\n'
check(filter_integers)