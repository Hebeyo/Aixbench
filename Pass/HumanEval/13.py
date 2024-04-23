def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate(3, 7) == 1
        assert candidate(10, 15) == 5
        assert candidate(49, 14) == 7
        assert candidate(144, 60) == 12
'\nStandard answer: \n    while b:\n        a, b = b, a % b\n    return a\n'
check(greatest_common_divisor)