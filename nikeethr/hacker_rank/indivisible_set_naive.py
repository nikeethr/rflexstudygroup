def compute_max_indivisible_set(k, S):
    """
        Computes and returns largest subset of S, S' such that there exists no
        (x, y) in S' where (x + y) % k = 0.

        precondition: S consists of unique natural numbers.

        Let P = {(x,y) in S | x != y and (x + y) % k = 0}
        Let f(x) = {x in S | number of occurences of x in P} 

        for each x in S, if we compute f(x), then we would have the max
        occurences for each element in S that satisfies the elementhood test in
        P.

        If we discard all x in S that appear in P then we would have an
        indivisible set, but not the biggest. In order to have the biggest
        indivisible set, we would have to remove the least elements in set S. 
        This is equivilent to removing the least number of elements in S such
        that all pairs in P are removed.
        
        Let w = arg max f(x).

        Given that S has unique elements, then removing x != w will reduce the
        occurance of f(x) elements in P by one. This is less optimal than
        removing f(w) elements in P by one since f(w) >= f(x).

        Thus, the least number of removals from S to empty P would be to remove
        arg max f(x) at each iteration.
    """
    S_ = list(S)
    N = len(S_)

    P = dict()
    C = [0 for x in range(N)]

    for i in range(N):
        for j in range(i+1,N):
            if (S_[i] + S_[j]) % k == 0:
                if i not in P:
                    P[i] = dict()
                P[i][j] = True
                C[i] += 1
                C[j] += 1

    while 1:
        i, c = max(enumerate(C), key=lambda x: x[1])

        if c == 0:
            break

        for j in range(N):
            if (i in P and j in P[i] and P[i][j]) or (j in P and i in P[j] and P[j][i]):
                C[j] = 0 if C[j] == 0 else C[j] - 1

        C[i] = 0

        S.remove(S_[i])

if __name__ == '__main__':
    (n, k) = input().strip().split(' ')
    (n, k) = (int(n), int(k))
    S = map(int, input().strip().split(' '))

    compute_max_indivisible_set(k, S)

    print(len(S))
