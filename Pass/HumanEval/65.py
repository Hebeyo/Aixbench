def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    x = str(x)
    if shift > len(x):
        return x[::-1]
    else:
        return x[len(x) - shift:] + x[:len(x) - shift]

def check(candidate):
    for item in range(31):
        assert candidate(100, 2) == '001'
        assert candidate(12, 2) == '12'
        assert candidate(97, 8) == '79'
        assert candidate(12, 1) == '21', 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate(11, 101) == '11', 'This prints if this assert fails 2 (also good for debugging!)'
'\nStandard answer: \n    s = str(x)\n    if shift > len(s):\n        return s[::-1]\n    else:\n        return s[len(s) - shift:] + s[:len(s) - shift]\n'
check(circular_shift)