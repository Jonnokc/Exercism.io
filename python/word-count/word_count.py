import string
import re


def word_count(sentence):

    s = " "
    puncuation_cleaner = str.maketrans('', '', string.punctuation)

    seperated_sentence = re.split('[ _,]+', sentence)
    combined_sentence = s.join(seperated_sentence)
    cleaned_sentence = (combined_sentence.translate(puncuation_cleaner))
    words = cleaned_sentence.split()
    word_dict = {}

    for word in words:
        word_num = 0

        if str.isalpha(word) or str.isnumeric(word):
            for in_word in words:
                if str.upper(word) == str.upper(in_word):
                    word_num += 1
            if str.upper(word) not in map(str.upper, word_dict):
                    word_dict[word] = word_num

    return word_dict
