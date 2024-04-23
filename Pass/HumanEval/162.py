def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

def check(candidate):
    for item in range(31):
        assert candidate('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
        assert candidate('') == None
        assert candidate('A B C') == '0ef78513b0cb8cef12743f5aeb35f888'
        assert candidate('password') == '5f4dcc3b5aa765d61d8327deb882cf99'
        assert True
"\nStandard answer: \n    import hashlib\n    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None\n"
check(string_to_md5)