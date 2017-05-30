import string


def word_count(sentence):

   new_sentence = sentence.translate(string.maketrans("",""), string.punctuation)

    print(sentence)

    words = sentence.split()
    word_dict = {}

    print(words)
    print(word_dict)

    for word in words:
        word_num = 0

        if str.isalpha(word) or str.isnumeric(word):
            for in_word in words:
                if word == in_word:
                    word_num += 1
            if word not in word_dict:
                word_dict[word] = word_num

    return word_dict
