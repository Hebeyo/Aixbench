def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    dict1 = {}
    list1 = test.split(' ')
    t = 0
    for i in list1:
        if list1.count(i) > t and i != '':
            t = list1.count(i)
    if t > 0:
        for i in list1:
            if list1.count(i) == t:
                dict1[i] = t
    return dict1

def check(candidate):
    for item in range(31):
        assert candidate('a b b a') == {'a': 2, 'b': 2}, 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate('a b c a b') == {'a': 2, 'b': 2}, 'This prints if this assert fails 2 (good for debugging!)'
        assert candidate('a b c d g') == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'g': 1}, 'This prints if this assert fails 3 (good for debugging!)'
        assert candidate('r t g') == {'r': 1, 't': 1, 'g': 1}, 'This prints if this assert fails 4 (good for debugging!)'
        assert candidate('b b b b a') == {'b': 4}, 'This prints if this assert fails 5 (good for debugging!)'
        assert candidate('r t g') == {'r': 1, 't': 1, 'g': 1}, 'This prints if this assert fails 6 (good for debugging!)'
        assert candidate('') == {}, 'This prints if this assert fails 7 (also good for debugging!)'
        assert candidate('a') == {'a': 1}, 'This prints if this assert fails 8 (also good for debugging!)'
'\nStandard answer: \n    dict1={}\n    list1=test.split(" ")\n    t=0\n\n    for i in list1:\n        if(list1.count(i)>t) and i!=\'\':\n            t=list1.count(i)\n    if t>0:\n        for i in list1:\n            if(list1.count(i)==t):\n                \n                dict1[i]=t\n    return dict1\n'
check(histogram)