def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    ret = []
    for (i, x) in enumerate(xs):
        if i == 0:
            continue
        ret.append(i * x)
    return ret
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
        assert candidate([1, 2, 3]) == [2, 6]
        assert candidate([3, 2, 1]) == [2, 2]
        assert candidate([3, 2, 1, 0, 4]) == [2, 2, 0, 16]
        assert candidate([1]) == []
'\nStandard answer: \n    return [(i * x) for i, x in enumerate(xs)][1:]\n'
check(derivative)