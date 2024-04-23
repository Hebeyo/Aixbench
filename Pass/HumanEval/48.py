def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate('') == True
        assert candidate('aba') == True
        assert candidate('aaaaa') == True
        assert candidate('zbcd') == False
        assert candidate('xywyx') == True
        assert candidate('xywyz') == False
        assert candidate('xywzx') == False
'\nStandard answer: \n    for i in range(len(text)):\n        if text[i] != text[len(text) - 1 - i]:\n            return False\n    return True\n'
check(is_palindrome)