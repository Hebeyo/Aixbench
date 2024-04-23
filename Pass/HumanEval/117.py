def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            if word[i].lower() not in ['a', 'e', 'i', 'o', 'u']:
                n_consonants += 1
        if n_consonants == n:
            result.append(word)
    return result

def check(candidate):
    for item in range(31):
        assert candidate('Mary had a little lamb', 4) == ['little'], 'First test error: ' + str(candidate('Mary had a little lamb', 4))
        assert candidate('Mary had a little lamb', 3) == ['Mary', 'lamb'], 'Second test error: ' + str(candidate('Mary had a little lamb', 3))
        assert candidate('simple white space', 2) == [], 'Third test error: ' + str(candidate('simple white space', 2))
        assert candidate('Hello world', 4) == ['world'], 'Fourth test error: ' + str(candidate('Hello world', 4))
        assert candidate('Uncle sam', 3) == ['Uncle'], 'Fifth test error: ' + str(candidate('Uncle sam', 3))
        assert candidate('', 4) == [], '1st edge test error: ' + str(candidate('', 4))
        assert candidate('a b c d e f', 1) == ['b', 'c', 'd', 'f'], '2nd edge test error: ' + str(candidate('a b c d e f', 1))
'\nStandard answer: \n    result = []\n    for word in s.split():\n        n_consonants = 0\n        for i in range(0, len(word)):\n            if word[i].lower() not in ["a","e","i","o","u"]:\n                n_consonants += 1 \n        if n_consonants == n:\n            result.append(word)\n    return result\n\n'
check(select_words)