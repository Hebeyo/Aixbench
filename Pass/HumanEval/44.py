def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    ret = ''
    while x > 0:
        ret = str(x % base) + ret
        x //= base
    return ret
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate(8, 3) == '22'
        assert candidate(9, 3) == '100'
        assert candidate(234, 2) == '11101010'
        assert candidate(16, 2) == '10000'
        assert candidate(8, 2) == '1000'
        assert candidate(7, 2) == '111'
        for x in range(2, 8):
            assert candidate(x, x + 1) == str(x)
'\nStandard answer: \n    ret = ""\n    while x > 0:\n        ret = str(x % base) + ret\n        x //= base\n    return ret\n'
check(change_base)