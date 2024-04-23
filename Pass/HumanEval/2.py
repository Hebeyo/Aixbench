def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate(3.5) == 0.5
        assert abs(candidate(1.33) - 0.33) < 1e-06
        assert abs(candidate(123.456) - 0.456) < 1e-06
'\nStandard answer: \n    return number % 1.0\n'
check(truncate_number)