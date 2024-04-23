def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for c in s:
        if c in alphabet:
            result += alphabet[(alphabet.index(c) + 2 * 2) % 26]
        else:
            result += c
    return result

def check(candidate):
    for item in range(31):
        assert candidate('hi') == 'lm', 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate('asdfghjkl') == 'ewhjklnop', 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate('gf') == 'kj', 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate('et') == 'ix', 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate('faewfawefaewg') == 'jeiajeaijeiak', 'This prints if this assert fails 1 (good for debugging!)'
        assert candidate('hellomyfriend') == 'lippsqcjvmirh', 'This prints if this assert fails 2 (good for debugging!)'
        assert candidate('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh') == 'hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', 'This prints if this assert fails 3 (good for debugging!)'
        assert candidate('a') == 'e', 'This prints if this assert fails 2 (also good for debugging!)'
"\nStandard answer: \n    d = 'abcdefghijklmnopqrstuvwxyz'\n    out = ''\n    for c in s:\n        if c in d:\n            out += d[(d.index(c)+2*2) % 26]\n        else:\n            out += c\n    return out\n"
check(encrypt)