def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef
ghijklm")
    'bcdf
ghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([c for c in text if c.lower() not in vowels])
METADATA = {}

def check(candidate):
    for item in range(31):
        assert candidate('') == ''
        assert candidate('abcdef\nghijklm') == 'bcdf\nghjklm'
        assert candidate('fedcba') == 'fdcb'
        assert candidate('eeeee') == ''
        assert candidate('acBAA') == 'cB'
        assert candidate('EcBOO') == 'cB'
        assert candidate('ybcd') == 'ybcd'
'\nStandard answer: \n    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])\n'
check(remove_vowels)