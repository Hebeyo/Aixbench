def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    result = set()
    for c in string.lower():
        result.add(c)
    return len(result)
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate('') == 0
        assert candidate('abcde') == 5
        assert candidate('abcde' + 'cade' + 'CADE') == 5
        assert candidate('aaaaAAAAaaaa') == 1
        assert candidate('Jerry jERRY JeRRRY') == 5
'\nStandard answer: \n    return len(set(string.lower()))\n'
check(count_distinct_characters)