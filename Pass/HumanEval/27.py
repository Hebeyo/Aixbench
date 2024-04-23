def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''
    for c in string:
        if c.islower():
            result += c.upper()
        else:
            result += c.lower()
    return result
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate('') == ''
        assert candidate('Hello!') == 'hELLO!'
        assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'
'\nStandard answer: \n    return string.swapcase()\n'
check(flip_case)