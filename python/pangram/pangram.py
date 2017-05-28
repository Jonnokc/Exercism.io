def is_pangram(sentence=''):

    import string

    for char in string.ascii_lowercase:
        if str.lower(char) not in str.lower(sentence):
            return False
    return True
