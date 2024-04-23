def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

def check(candidate):
    for item in range(31):
        assert candidate(7) == (0, 1)
        assert candidate(-78) == (1, 1)
        assert candidate(3452) == (2, 2)
        assert candidate(346211) == (3, 3)
        assert candidate(-345821) == (3, 3)
        assert candidate(-2) == (1, 0)
        assert candidate(-45347) == (2, 3)
        assert candidate(0) == (1, 0)
        assert True
'\nStandard answer: \n    even_count = 0\n    odd_count = 0\n    for i in str(abs(num)):\n        if int(i)%2==0:\n            even_count +=1\n        else:\n            odd_count +=1\n    return (even_count, odd_count)\n'
check(even_odd_count)