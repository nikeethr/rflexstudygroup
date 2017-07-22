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
    return dna1.find(dna2) != -1

def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if DNA sequence dna contains only
    characters from 'ATCG'

    >>> is_valid_sequence('GATTACA')
    True
    >>> is_valid_sequence('Floyd')
    False

    """

    return get_length(dna) == sum(c in 'ATCG' for c in dna)

def insert_sequence(dna1, dna2, index):
    """ (str,str,int) -> str

    Return the DNA sequence formed by inserting dna2 into
    dna2 at the specified index

    >>> insert_sequence('AAAA', 'TT', 2)
    AATTAA
    >>> insert_sequence('AAAA', 'TT', 0)
    TTAAAA
    >>> insert_sequence('AAAA', 'TT', 4)
    AAAATT

    """
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    """ (str) -> str

    Return the complement of nucleotide

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    >>> get_complement('G')
    C

    """
    if nucleotide == 'A': return 'T'
    if nucleotide == 'T': return 'A'
    if nucleotide == 'C': return 'G'
    return 'C'

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the complementary DNA sequence of dna

    >>> get_complementary_sequence('GATTACA')
    CTAATGT
    >>> get_complementary_sequence('AT')
    TA

    """
    complement = ''
    for c in dna:
        complement += get_complement(c)
    return complement
