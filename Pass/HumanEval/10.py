def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''
    beginning_of_suffix = 0
    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1
    return string + string[:beginning_of_suffix][::-1]
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate('') == ''
        assert candidate('x') == 'x'
        assert candidate('xyz') == 'xyzyx'
        assert candidate('xyx') == 'xyx'
        assert candidate('jerry') == 'jerryrrej'
"\nStandard answer: \n    if not string:\n        return ''\n\n    beginning_of_suffix = 0\n\n    while not is_palindrome(string[beginning_of_suffix:]):\n        beginning_of_suffix += 1\n\n    return string + string[:beginning_of_suffix][::-1]\n"
check(make_palindrome)