def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    times = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            times += 1
    return times
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate('', 'x') == 0
        assert candidate('xyxyxyx', 'x') == 4
        assert candidate('cacacacac', 'cac') == 4
        assert candidate('john doe', 'john') == 1
'\nStandard answer: \n    times = 0\n\n    for i in range(len(string) - len(substring) + 1):\n        if string[i:i+len(substring)] == substring:\n            times += 1\n\n    return times\n'
check(how_many_times)