def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 2.0
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate(5, 3) == 7.5
        assert candidate(2, 2) == 2.0
        assert candidate(10, 8) == 40.0
'\nStandard answer: \n    return a * h / 2.0\n'
check(triangle_area)