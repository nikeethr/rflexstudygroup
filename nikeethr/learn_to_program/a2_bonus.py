import a2

def can_be_combined(xs):
    ids = range(len(xs))
    N = get_total_length(ids, xs)

    sequence = set()

    # N is odd
    if N % 2 != 0:
        return False

    # There exists x_i such that len(x_i) > N // 2
    for x in xs:
        if not a2.is_valid_sequence(x):
            return False
        if a2.get_length(x) > N // 2:
            return False

    for i in ids:
        construct_node([i], sequence, xs, ids, N)
    
    # find intersection of complimentary sets
    sequence_complement = set()

    for s in sequence:
        sequence_complement.add(a2.get_complementary_sequence(s))

    sequence_intersection = sequence.intersection(sequence_complement)

    if len(sequence_intersection) > 0:
        return True
    else:
        return False


def construct_node(node, sequence, xs, ids, N):
    l = get_total_length(node, xs)

    if l == N // 2:
        sequence.add(combine_seq(node, xs))
        return

    for i in ids:

        if i in node:
            continue

        if l + len(xs[i]) > N // 2:
            continue

        construct_node(node + [i], sequence, xs, ids, N)

def get_total_length(ids, xs):
    l = 0
    for i in ids:
        l += len(xs[i])
    return l

def combine_seq(ids, xs):
    c = ''
    for i in ids:
        c += xs[i]
    return c

if __name__ == '__main__':
    xs = ['A', 'T']
    result = can_be_combined(xs)
    exit(0)
