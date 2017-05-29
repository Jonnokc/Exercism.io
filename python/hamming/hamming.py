def distance(dna_1, dna_2):

    dif_count = 0
    if len(dna_1) == len(dna_2):
        for dna_1, dna_2 in zip(dna_1, dna_2):
            if dna_1 != dna_2:
                dif_count += 1
        return dif_count
    else:
        raise ValueError()
