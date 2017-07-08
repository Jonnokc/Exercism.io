def hey(sentence):

    sentence = sentence.strip()
    if sentence.isupper():
        # Yelling
        return 'Whoa, chill out!'
    elif sentence.endswith('?'):
        # Question
        return 'Sure.'
    elif sentence == '':
        # Nothing
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
