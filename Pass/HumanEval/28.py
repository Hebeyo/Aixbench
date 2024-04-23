from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for s in strings:
        result += s
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate([]) == ''
        assert candidate(['x', 'y', 'z']) == 'xyz'
        assert candidate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'
"\nStandard answer: \n    return ''.join(strings)\n"
check(concatenate)