from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    result = strings[0]
    for s in strings:
        if len(s) > len(result):
            result = s
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate([]) == None
        assert candidate(['x', 'y', 'z']) == 'x'
        assert candidate(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'
'\nStandard answer: \n    if not strings:\n        return None\n\n    maxlen = max(len(x) for x in strings)\n    for s in strings:\n        if len(s) == maxlen:\n            return s\n'
check(longest)