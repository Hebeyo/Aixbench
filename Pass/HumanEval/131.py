def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product = product * int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product

def check(candidate):
    for item in range(31):
        assert candidate(5) == 5
        assert candidate(54) == 5
        assert candidate(120) == 1
        assert candidate(5014) == 5
        assert candidate(98765) == 315
        assert candidate(5576543) == 2625
        assert candidate(2468) == 0
'\nStandard answer: \n    product = 1\n    odd_count = 0\n    for digit in str(n):\n        int_digit = int(digit)\n        if int_digit%2 == 1:\n            product= product*int_digit\n            odd_count+=1\n    if odd_count ==0:\n        return 0\n    else:\n        return product\n'
check(digits)