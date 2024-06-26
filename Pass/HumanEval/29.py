from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    result = []
    for s in strings:
        if s.startswith(prefix):
            result.append(s)
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate([], 'john') == []
        assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
'\nStandard answer: \n    return [x for x in strings if x.startswith(prefix)]\n'
check(filter_by_prefix)