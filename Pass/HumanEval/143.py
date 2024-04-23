def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    new_lst = []
    for word in sentence.split():
        flg = 0
        if len(word) == 1:
            flg = 1
        for i in range(2, len(word)):
            if len(word) % i == 0:
                flg = 1
        if flg == 0 or len(word) == 2:
            new_lst.append(word)
    return ' '.join(new_lst)

def check(candidate):
    for item in range(31):
        assert candidate('This is a test') == 'is'
        assert candidate('lets go for swimming') == 'go for'
        assert candidate('there is no place available here') == 'there is no place'
        assert candidate('Hi I am Hussein') == 'Hi am Hussein'
        assert candidate('go for it') == 'go for it'
        assert candidate('here') == ''
        assert candidate('here is') == 'is'
'\nStandard answer: \n    new_lst = []\n    for word in sentence.split():\n        flg = 0\n        if len(word) == 1:\n            flg = 1\n        for i in range(2, len(word)):\n            if len(word)%i == 0:\n                flg = 1\n        if flg == 0 or len(word) == 2:\n            new_lst.append(word)\n    return " ".join(new_lst)\n'
check(words_in_sentence)