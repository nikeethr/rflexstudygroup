def maxOfFour(i, j, n):
    lm = (2 * n - 1)
    return max([mat[i][j],
                mat[lm - i][j],
                mat[i][lm - j],
                mat[lm - i][lm - j]])

q = int(input())

for _ in range(q):
    n = int(input())

    mat = [[]] * (2 * n)

    for i in range(2 * n):
        mat[i] = [int(x) for x in input().split()]

    total = sum(maxOfFour(i, j, n)
                for i in range(n)
                for j in range(n))

    print(total)
