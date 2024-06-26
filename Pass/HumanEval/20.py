from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = None
    distance = None
    for (idx, elem) in enumerate(numbers):
        for (idx2, elem2) in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance < distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))
    return closest_pair
METADATA = {'author': 'jt', 'dataset': 'test'}

def check(candidate):
    for item in range(31):
        assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
        assert candidate([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
        assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
        assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
        assert candidate([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1)
'\nStandard answer: \n    closest_pair = None\n    distance = None\n\n    for idx, elem in enumerate(numbers):\n        for idx2, elem2 in enumerate(numbers):\n            if idx != idx2:\n                if distance is None:\n                    distance = abs(elem - elem2)\n                    closest_pair = tuple(sorted([elem, elem2]))\n                else:\n                    new_distance = abs(elem - elem2)\n                    if new_distance < distance:\n                        distance = new_distance\n                        closest_pair = tuple(sorted([elem, elem2]))\n\n    return closest_pair\n'
check(find_closest_elements)