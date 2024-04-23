def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    for c in s0:
        if c not in s1:
            return False
    for c in s1:
        if c not in s0:
            return False
    return True
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
        assert candidate('abcd', 'dddddddabc') == True
        assert candidate('dddddddabc', 'abcd') == True
        assert candidate('eabcd', 'dddddddabc') == False
        assert candidate('abcd', 'dddddddabcf') == False
        assert candidate('eabcdzzzz', 'dddzzzzzzzddddabc') == False
        assert candidate('aabb', 'aaccc') == False
'\nStandard answer: \n    return set(s0) == set(s1)\n'
check(same_chars)