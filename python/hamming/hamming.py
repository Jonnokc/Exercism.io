def distance(dna_1, dna_2):

    dna_1 = list(dna_1)
    dna_2 = list(dna_2)
    dif_count = 0

    if len(dna_1) != len(dna_2):
        raise ValueError()

    for index, elem in enumerate(dna_1):
        if dna_1[index] != dna_2[index]:
            dif_count += 1
    return dif_count
