def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    return sum((ord(char) if char.isupper() else 0 for char in s))

def check(candidate):
    for item in range(31):
        assert True, 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate('') == 0, 'Error'
        assert candidate('abAB') == 131, 'Error'
        assert candidate('abcCd') == 67, 'Error'
        assert candidate('helloE') == 69, 'Error'
        assert candidate('woArBld') == 131, 'Error'
        assert candidate('aAaaaXa') == 153, 'Error'
        assert True, 'This prints if this assert fails 2 (also good for debugging!)'
        assert candidate(' How are yOu?') == 151, 'Error'
        assert candidate('You arE Very Smart') == 327, 'Error'
'\nStandard answer: \n    if s == "": return 0\n    return sum(ord(char) if char.isupper() else 0 for char in s)\n'
check(digitSum)