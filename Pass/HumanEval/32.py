import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for (i, coeff) in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    assert len(xs) % 2 == 0
    assert xs[-1] != 0
    (begin, end) = (-1.0, 1.0)
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin
METADATA = {}

def check(candidate):
    for item in range(31):
        import math
        import random
        rng = random.Random(42)
        import copy
        for _ in range(100):
            ncoeff = 2 * rng.randint(1, 4)
            coeffs = []
            for _ in range(ncoeff):
                coeff = rng.randint(-10, 10)
                if coeff == 0:
                    coeff = 1
                coeffs.append(coeff)
            solution = candidate(copy.deepcopy(coeffs))
            assert math.fabs(poly(coeffs, solution)) < 0.0001
'\nStandard answer: \n    begin, end = -1., 1.\n    while poly(xs, begin) * poly(xs, end) > 0:\n        begin *= 2.0\n        end *= 2.0\n    while end - begin > 1e-10:\n        center = (begin + end) / 2.0\n        if poly(xs, center) * poly(xs, begin) > 0:\n            begin = center\n        else:\n            end = center\n    return begin\n'
check(find_zero)