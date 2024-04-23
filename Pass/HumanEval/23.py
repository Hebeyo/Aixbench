def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    result = 0
    for _ in string:
        result += 1
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate('') == 0
        assert candidate('x') == 1
        assert candidate('asdasnakj') == 9
'\nStandard answer: \n    return len(string)\n'
check(strlen)