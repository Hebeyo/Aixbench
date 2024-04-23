def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    result = []
    for word in s.split(' '):
        result.append(''.join(sorted(list(word))))
    return ' '.join(result)

def check(candidate):
    for item in range(31):
        assert candidate('Hi') == 'Hi'
        assert candidate('hello') == 'ehllo'
        assert candidate('number') == 'bemnru'
        assert candidate('abcd') == 'abcd'
        assert candidate('Hello World!!!') == 'Hello !!!Wdlor'
        assert candidate('') == ''
        assert candidate('Hi. My name is Mister Robot. How are you?') == '.Hi My aemn is Meirst .Rboot How aer ?ouy'
        assert True
"\nStandard answer: \n    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])\n"
check(anti_shuffle)