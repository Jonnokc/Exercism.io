def to_rna(dna=''):

    new_dna = list(dna)

    for i in range(len(new_dna)):
        if new_dna[i] == 'G':
            new_dna[i] = 'C'
        elif new_dna[i] == 'C':
            new_dna[i] = 'G'
        elif new_dna[i] == 'T':
            new_dna[i] = 'A'
        elif new_dna[i] == 'A':
            new_dna[i] = 'U'
        else:
            return ('')

    return ''.join(new_dna)
