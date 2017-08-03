MAXN = (2 * 10**5) + 10
MOD = 10**9 + 7

# Pre-compute factorials and inverses
F = [0] * MAXN
iF = [0] * MAXN
F[0], iF[0] = [1, 1]

for i in range(1, MAXN):
    F[i] = (F[i-1] * i) % MOD
    iF[i] = pow(F[i], MOD - 2, MOD)


def choose(n, k):
    return F[n] * iF[k] * iF[n - k] % MOD


tc = int(input())
for _ in range(tc):
    n, m = [int(x) for x in input().split()]
    print(choose(n + m - 2, n - 1))

