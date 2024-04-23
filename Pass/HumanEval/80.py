def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            return False
    return True

def check(candidate):
    for item in range(31):
        assert candidate('a') == False, 'a'
        assert candidate('aa') == False, 'aa'
        assert candidate('abcd') == True, 'abcd'
        assert candidate('aabb') == False, 'aabb'
        assert candidate('adb') == True, 'adb'
        assert candidate('xyy') == False, 'xyy'
        assert candidate('iopaxpoi') == True, 'iopaxpoi'
        assert candidate('iopaxioi') == False, 'iopaxioi'
'\nStandard answer: \n    if len(s) < 3:\n      return False\n\n    for i in range(len(s) - 2):\n      \n      if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:\n        return False\n    return True\n'
check(is_happy)