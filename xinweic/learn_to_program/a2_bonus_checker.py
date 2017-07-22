# Usage: python a2_bonus_checker.py 'your_answer_here.py'
# 'your_answer_here.py' should contain function can_be_combined()

import sys
import random
import a2
import a2_bonus

LOWER_LENGTH = 10
UPPER_LENGTH = 50

LOWER_FRAGMENTS = 3
UPPER_FRAGMENTS = 8

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


def generate_strands(length, num_fragments, swaps):
    dna1 = [random.choice('ATCG') for _ in range(length)]
    for _ in range(swaps):
        i = random.randint(0, length-1)
        j = random.randint(0, length-1)
        dna1[i], dna1[j] = dna1[j], dna1[i]

    dna1 = ''.join(dna1)
    dna2 = get_complementary_sequence(dna1)
    dna1 += dna2

    indices = [0, length, 2*length] + random.sample([x for x in range(1, 2 * length) if x != length], num_fragments - 2)
    indices.sort()

    fragments = []
    for i in range(num_fragments):
        fragments.append(dna1[indices[i]:indices[i+1]])
    return fragments

if __name__ == '__main__':
    module = __import__(sys.argv[1].replace('.py', ''))

    random.seed(42)
    iterations = 0

    while True:
        length = random.randint(LOWER_LENGTH, UPPER_LENGTH)
        num_fragments = random.randint(LOWER_FRAGMENTS, UPPER_FRAGMENTS)
        swaps = random.randint(0, 1)

        fragments = generate_strands(length, num_fragments, swaps)
        assert(len(fragments) == num_fragments)
        assert(min(len(s) for s in fragments) != 0)

        reference_answer = a2_bonus.can_be_combined(fragments)
        if swaps == 0:
            assert(reference_answer)

        answer = module.can_be_combined(fragments)
        if reference_answer != answer:
            print(fragments)
            print('reference answer = {}, answer = {}'.format(reference_answer, answer))
            sys.exit(0)

        iterations += 1
        if iterations % 10000 == 0:
            print('Total number of test cases = {}'.format(iterations), end='\r')
            sys.stdout.flush()

