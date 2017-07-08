def encode(input):

    count = 1
    prev_char = ''
    list = []

    if input is '':
        return ''

    for char in input:
        if char != prev_char:
            if prev_char != '':
                if count is 1:
                    add = (prev_char)
                else:
                    add = (count, prev_char)
                list.append(add)
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        if count is 1:
            list.append(char)
        else:
            add = (count, prev_char)
            list.append(add)

    untuple = [i for sub in list for i in sub]
    values = ''.join(str(v) for v in untuple)
    return values


def decode(input):

    list = []
    num_count = ''

    for char in input:
        if str.isdigit(char):
            num_count += str(char)
        else:
            ltr = char
            if num_count != '':
                ltr_count = int(num_count)
            else:
                ltr_count = 1

            for i in range(ltr_count):
                list.append(ltr)
            num_count = ''
    to_string = ''.join(list)
    return to_string
