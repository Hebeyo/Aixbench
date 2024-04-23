from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i != j:
                if abs(numbers[i] - numbers[j]) < threshold:
                    return True
    return False
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
        assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
        assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
        assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
        assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
        assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
        assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False
'\nStandard answer: \n    for idx, elem in enumerate(numbers):\n        for idx2, elem2 in enumerate(numbers):\n            if idx != idx2:\n                distance = abs(elem - elem2)\n                if distance < threshold:\n                    return True\n\n    return False\n'
check(has_close_elements)