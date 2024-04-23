def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    a = []
    for i in range(1, n + 1):
        a.append(i * i - i + 1)
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count

def check(candidate):
    for item in range(31):
        assert candidate(5) == 1
        assert candidate(6) == 4
        assert candidate(10) == 36
        assert candidate(100) == 53361
'\nStandard answer: \n    A = [i*i - i + 1 for i in range(1,n+1)]\n    ans = []\n    for i in range(n):\n        for j in range(i+1,n):\n            for k in range(j+1,n):\n                if (A[i]+A[j]+A[k])%3 == 0:\n                    ans += [(A[i],A[j],A[k])]\n    return len(ans)\n'
check(get_max_triples)