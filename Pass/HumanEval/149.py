def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i) % 2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)

def check(candidate):
    for item in range(31):
        assert candidate(['aa', 'a', 'aaa']) == ['aa']
        assert candidate(['school', 'AI', 'asdf', 'b']) == ['AI', 'asdf', 'school']
        assert candidate(['d', 'b', 'c', 'a']) == []
        assert candidate(['d', 'dcba', 'abcd', 'a']) == ['abcd', 'dcba']
        assert candidate(['AI', 'ai', 'au']) == ['AI', 'ai', 'au']
        assert candidate(['a', 'b', 'b', 'c', 'c', 'a']) == []
        assert candidate(['aaaa', 'bbbb', 'dd', 'cc']) == ['cc', 'dd', 'aaaa', 'bbbb']
'\nStandard answer: \n    lst.sort()\n    new_lst = []\n    for i in lst:\n        if len(i)%2 == 0:\n            new_lst.append(i)\n    return sorted(new_lst, key=len)\n'
check(sorted_list_sum)