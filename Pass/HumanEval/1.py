from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_string = []
    current_depth = 0
    for c in paren_string:
        if c == '(':
            current_depth += 1
            current_string.append(c)
        elif c == ')':
            current_depth -= 1
            current_string.append(c)
            if current_depth == 0:
                result.append(''.join(current_string))
                current_string.clear()
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
        assert candidate('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
        assert candidate('(()(())((())))') == ['(()(())((())))']
        assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
"\nStandard answer: \n    result = []\n    current_string = []\n    current_depth = 0\n\n    for c in paren_string:\n        if c == '(':\n            current_depth += 1\n            current_string.append(c)\n        elif c == ')':\n            current_depth -= 1\n            current_string.append(c)\n\n            if current_depth == 0:\n                result.append(''.join(current_string))\n                current_string.clear()\n\n    return result\n"
check(separate_paren_groups)