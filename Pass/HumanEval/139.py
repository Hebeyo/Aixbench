def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n + 1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def check(candidate):
    for item in range(31):
        assert candidate(4) == 288, 'Test 4'
        assert candidate(5) == 34560, 'Test 5'
        assert candidate(7) == 125411328000, 'Test 7'
        assert candidate(1) == 1, 'Test 1'
'\nStandard answer: \n    fact_i = 1\n    special_fact = 1\n    for i in range(1, n+1):\n        fact_i *= i\n        special_fact *= fact_i\n    return special_fact\n'
check(special_factorial)