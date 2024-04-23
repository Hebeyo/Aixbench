from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = []
    for i in range(len(a)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate('111000', '101010') == '010010'
        assert candidate('1', '1') == '0'
        assert candidate('0101', '0000') == '0101'
"\nStandard answer: \n    def xor(i, j):\n        if i == j:\n            return '0'\n        else:\n            return '1'\n\n    return ''.join(xor(x, y) for x, y in zip(a, b))\n"
check(string_xor)