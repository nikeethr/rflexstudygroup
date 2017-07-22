def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True only if dna sequence is valid. Sequence is valid if and only if
    dna only contains characters in {'A', 'T', 'C', 'G'}.

    >>> is_valid_sequence('BAD')
    False
    >>> is_valid_sequence('GATC')
    True

    """
    valid = True
    valid_char = ['A', 'T', 'C', 'G']

    for c in dna:
        if c not in valid_char:
            valid = False
            break

    return valid

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    Return result of dna2 inserted into dna1 at the given index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
    >>> insert_sequence('CCGG', 'AT', 4)
    'CCGGAT'

    """
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """ (str) -> str
    Return the nucleotide's complement
    note: complement pairs are [(A,T), (C,G)]

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'

    """
    compliment = None

    if nucleotide == 'A':
        compliment = 'T'
    elif nucleotide == 'T':
        compliment = 'A'
    elif nucleotide == 'C':
        compliment = 'G'
    elif nucleotide == 'G':
        compliment = 'C'

    return compliment

def get_complementary_sequence(dna):
    """ (str) -> str
    Return the complementary sequence of dna

    >>> get_complementary_sequence('ATAG')
    'TATC'
    >>> get_complementary_sequence('CCAT')
    'GGTA'

    """
    result = ''

    for c in dna:
        result += get_complement(c)

    return result
