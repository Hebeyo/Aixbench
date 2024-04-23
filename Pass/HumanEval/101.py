def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    """
    s_list = []
    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)
    s_list = ''.join(s_list)
    return s_list.split()

def check(candidate):
    for item in range(31):
        assert True, 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate('Hi, my name is John') == ['Hi', 'my', 'name', 'is', 'John']
        assert candidate('One, two, three, four, five, six') == ['One', 'two', 'three', 'four', 'five', 'six']
        assert candidate('Hi, my name') == ['Hi', 'my', 'name']
        assert candidate('One,, two, three, four, five, six,') == ['One', 'two', 'three', 'four', 'five', 'six']
        assert True, 'This prints if this assert fails 2 (also good for debugging!)'
        assert candidate('') == []
        assert candidate('ahmed     , gamal') == ['ahmed', 'gamal']
'\nStandard answer: \n    if not s:\n        return []\n\n    s_list = []\n\n    for letter in s:\n        if letter == \',\':\n            s_list.append(\' \')\n        else:\n            s_list.append(letter)\n\n    s_list = "".join(s_list)\n    return s_list.split()\n'
check(words_string)