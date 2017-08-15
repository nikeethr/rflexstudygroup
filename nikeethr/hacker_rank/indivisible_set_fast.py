def compute_max_indivisible_set(k, S):
    """
        Computes and returns largest subset of S, S' such that there exists no
        (x, y) in S' where (x + y) % k = 0.

        precondition: S consists of unique natural numbers.

        (x + y) % k = 0 <=> (x % k + y % k) % k = 0.

        let f(x, k) = x % k, supposing x is natural number then f(x, k) maps x to a finite space
        [1,...,k].

        for any i in [1,...,k] if f(x,k) = i then for y to be a pair of x, f(y,k) = k-i, as this
        would mean (x + y) % k = (x % k + y % k) % k = (k-i+i) % k = 0.

        If we get rid of all x in S such that f(x,k) = i for some i, then for all y in S where
        f(y,k) = k-i, y will no longer have a pair.

        There are two other special cases to consider:
        - i = 0
        - i = k - i

        In both of the above cases, it is sufficient to remove all but one x in S such that f(x,k) =
        0 or f(x,k) = k-i for them to no longer have pairs.

        Given this, count all the remainders x % k for x in S where f(x,k) = i call this P(i).

        It is then sufficient to sum max(P(i), P(k-i)) for all i in [0,...,(k-1)//2] and,
        add 1 if k is even (to account for the case where k-i = i) and,
        add 1 if P(0) > 0,
        in order to find the maximum length indivisible subset of S.
    """
    C = [0] * k
    L = 0

    for x in S:
        C[x % k] += 1

    for i in range(1,(k-1)//2+1):
        L += max(C[i], C[k-i])

    if k % 2 == 0:
        L += 1

    if C[0] > 0:
        L += 1

    return L

if __name__ == '__main__':
    (n, k) = input().strip().split(' ')
    (n, k) = (int(n), int(k))
    S = map(int, input().strip().split(' '))

    L = compute_max_indivisible_set(k, S)

    print(L)
