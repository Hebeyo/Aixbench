def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    suf = ['txt', 'exe', 'dll']
    lst = file_name.split(sep='.')
    if len(lst) != 2:
        return 'No'
    if not lst[1] in suf:
        return 'No'
    if len(lst[0]) == 0:
        return 'No'
    if not lst[0][0].isalpha():
        return 'No'
    t = len([x for x in lst[0] if x.isdigit()])
    if t > 3:
        return 'No'
    return 'Yes'

def check(candidate):
    for item in range(31):
        assert candidate('example.txt') == 'Yes'
        assert candidate('1example.dll') == 'No'
        assert candidate('s1sdf3.asd') == 'No'
        assert candidate('K.dll') == 'Yes'
        assert candidate('MY16FILE3.exe') == 'Yes'
        assert candidate('His12FILE94.exe') == 'No'
        assert candidate('_Y.txt') == 'No'
        assert candidate('?aREYA.exe') == 'No'
        assert candidate('/this_is_valid.dll') == 'No'
        assert candidate('this_is_valid.wow') == 'No'
        assert candidate('this_is_valid.txt') == 'Yes'
        assert candidate('this_is_valid.txtexe') == 'No'
        assert candidate('#this2_i4s_5valid.ten') == 'No'
        assert candidate('@this1_is6_valid.exe') == 'No'
        assert candidate('this_is_12valid.6exe4.txt') == 'No'
        assert candidate('all.exe.txt') == 'No'
        assert candidate('I563_No.exe') == 'Yes'
        assert candidate('Is3youfault.txt') == 'Yes'
        assert candidate('no_one#knows.dll') == 'Yes'
        assert candidate('1I563_Yes3.exe') == 'No'
        assert candidate('I563_Yes3.txtt') == 'No'
        assert candidate('final..txt') == 'No'
        assert candidate('final132') == 'No'
        assert candidate('_f4indsartal132.') == 'No'
        assert candidate('.txt') == 'No'
        assert candidate('s.') == 'No'
"\nStandard answer: \n    suf = ['txt', 'exe', 'dll']\n    lst = file_name.split(sep='.')\n    if len(lst) != 2:\n        return 'No'\n    if not lst[1] in suf:\n        return 'No'\n    if len(lst[0]) == 0:\n        return 'No'\n    if not lst[0][0].isalpha():\n        return 'No'\n    t = len([x for x in lst[0] if x.isdigit()])\n    if t > 3:\n        return 'No'\n    return 'Yes'\n"
check(file_name_check)