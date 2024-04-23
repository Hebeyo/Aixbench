from typing import List

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    value_map = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate('') == ''
        assert candidate('three') == 'three'
        assert candidate('three five nine') == 'three five nine'
        assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
        assert candidate('six five four three two one zero') == 'zero one two three four five six'
"\nStandard answer: \n    value_map = {\n        'zero': 0,\n        'one': 1,\n        'two': 2,\n        'three': 3,\n        'four': 4,\n        'five': 5,\n        'six': 6,\n        'seven': 7,\n        'eight': 8,\n        'nine': 9\n    }\n    return ' '.join(sorted([x for x in numbers.split(' ') if x], key=lambda x: value_map[x]))\n"
check(sort_numbers)