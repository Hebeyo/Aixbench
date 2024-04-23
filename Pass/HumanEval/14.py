from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []
    for i in range(len(string)):
        result.append(string[:i + 1])
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate('') == []
        assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
        assert candidate('WWW') == ['W', 'WW', 'WWW']
'\nStandard answer: \n    result = []\n\n    for i in range(len(string)):\n        result.append(string[:i+1])\n    return result\n'
check(all_prefixes)