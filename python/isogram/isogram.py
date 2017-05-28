def is_isogram(word=''):

    for char in word:
        count = 0
        for let in word:
            if (str.isalpha(char) is True and
                    str.isalpha(let) is True and
                    str.upper(char) == str.upper(let)):
                count = count + 1
        if count >= 2:
            return False
    return True
