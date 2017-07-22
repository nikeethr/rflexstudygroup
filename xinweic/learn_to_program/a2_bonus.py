import itertools
import a2

def can_be_combined(fragments):
    """ (list str) -> bool

    Returns True if and only if fragments can be combined
    into two complementary dna strands

    >>> can_be_combined(['A', 'AC', 'TG', 'CTG'])
    True
    >>> can_be_combined(['A', 'T', 'AA', 'TC'])
    False

    """
    length = sum(len(s) for s in fragments)
    if length % 2 != 0:
        return False

    length //= 2
    for perm in itertools.permutations(fragments):
        middle = 0
        first_dna_strand = ''
        while len(first_dna_strand) < length:
            first_dna_strand += perm[middle]
            middle += 1

        if len(first_dna_strand) > length:
            continue

        second_dna_strand = ''
        for i in range(middle, len(fragments)):
            second_dna_strand += perm[i]

        if a2.get_complementary_sequence(first_dna_strand) == second_dna_strand:
            return True

    return False
