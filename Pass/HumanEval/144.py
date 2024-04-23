def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    (a, b) = x.split('/')
    (c, d) = n.split('/')
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if numerator / denom == int(numerator / denom):
        return True
    return False

def check(candidate):
    for item in range(31):
        assert candidate('1/5', '5/1') == True, 'test1'
        assert candidate('1/6', '2/1') == False, 'test2'
        assert candidate('5/1', '3/1') == True, 'test3'
        assert candidate('7/10', '10/2') == False, 'test4'
        assert candidate('2/10', '50/10') == True, 'test5'
        assert candidate('7/2', '4/2') == True, 'test6'
        assert candidate('11/6', '6/1') == True, 'test7'
        assert candidate('2/3', '5/2') == False, 'test8'
        assert candidate('5/2', '3/5') == False, 'test9'
        assert candidate('2/4', '8/4') == True, 'test10'
        assert candidate('2/4', '4/2') == True, 'test11'
        assert candidate('1/5', '5/1') == True, 'test12'
        assert candidate('1/5', '1/5') == False, 'test13'
'\nStandard answer: \n    a, b = x.split("/")\n    c, d = n.split("/")\n    numerator = int(a) * int(c)\n    denom = int(b) * int(d)\n    if (numerator/denom == int(numerator/denom)):\n        return True\n    return False\n'
check(simplify)