def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            count += 1
    return count

def check(candidate):
    for item in range(31):
        assert candidate('aBCdEf') == 1
        assert candidate('abcdefg') == 0
        assert candidate('dBBE') == 0
        assert candidate('B') == 0
        assert candidate('U') == 1
        assert candidate('') == 0
        assert candidate('EEEE') == 2
        assert True
'\nStandard answer: \n    count = 0\n    for i in range(0,len(s),2):\n        if s[i] in "AEIOU":\n            count += 1\n    return count\n'
check(count_upper)