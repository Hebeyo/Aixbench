def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    return 18 * 10 ** (n - 2)

def check(candidate):
    for item in range(31):
        assert True, 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate(1) == 1
        assert candidate(2) == 18
        assert candidate(3) == 180
        assert candidate(4) == 1800
        assert candidate(5) == 18000
        assert True, 'This prints if this assert fails 2 (also good for debugging!)'
'\nStandard answer: \n    if n == 1: return 1\n    return 18 * (10 ** (n - 2))\n'
check(starts_one_ends)