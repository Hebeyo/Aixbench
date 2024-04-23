def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def check(candidate):
    for item in range(31):
        assert candidate('Hello') == True
        assert candidate('abcdcba') == True
        assert candidate('kittens') == True
        assert candidate('orange') == False
        assert candidate('wow') == True
        assert candidate('world') == True
        assert candidate('MadaM') == True
        assert candidate('Wow') == True
        assert candidate('') == False
        assert candidate('HI') == True
        assert candidate('go') == True
        assert candidate('gogo') == False
        assert candidate('aaaaaaaaaaaaaaa') == False
        assert candidate('Madam') == True
        assert candidate('M') == False
        assert candidate('0') == False
'\nStandard answer: \n    l = len(string)\n    if l == 0 or l == 1:\n        return False\n    for i in range(2, l):\n        if l % i == 0:\n            return False\n    return True\n'
check(prime_length)