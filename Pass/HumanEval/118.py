def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'U', 'I'}
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            if word[i + 1] not in vowels and word[i - 1] not in vowels:
                return word[i]
    return ''

def check(candidate):
    for item in range(31):
        assert candidate('yogurt') == 'u'
        assert candidate('full') == 'u'
        assert candidate('easy') == ''
        assert candidate('eAsy') == ''
        assert candidate('ali') == ''
        assert candidate('bad') == 'a'
        assert candidate('most') == 'o'
        assert candidate('ab') == ''
        assert candidate('ba') == ''
        assert candidate('quick') == ''
        assert candidate('anime') == 'i'
        assert candidate('Asia') == ''
        assert candidate('Above') == 'o'
        assert True
'\nStandard answer: \n    if len(word) < 3:\n        return ""\n\n    vowels = {"a", "e", "i", "o", "u", "A", "E", \'O\', \'U\', \'I\'}\n    for i in range(len(word)-2, 0, -1):\n        if word[i] in vowels:\n            if (word[i+1] not in vowels) and (word[i-1] not in vowels):\n                return word[i]\n    return ""\n'
check(get_closest_vowel)