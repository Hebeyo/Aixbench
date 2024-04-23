def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    depth = 0
    for b in brackets:
        if b == '(':
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate('()')
        assert candidate('(()())')
        assert candidate('()()(()())()')
        assert candidate('()()((()()())())(()()(()))')
        assert not candidate('((()())))')
        assert not candidate(')(()')
        assert not candidate('(')
        assert not candidate('((((')
        assert not candidate(')')
        assert not candidate('(()')
        assert not candidate('()()(()())())(()')
        assert not candidate('()()(()())()))()')
'\nStandard answer: \n    depth = 0\n    for b in brackets:\n        if b == "(":\n            depth += 1\n        else:\n            depth -= 1\n        if depth < 0:\n            return False\n    return depth == 0\n'
check(correct_bracketing)