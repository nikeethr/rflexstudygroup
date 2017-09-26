import math

def can_fill(a, b, c):
    """
    Let a be the capacity of jug A, c the capacity of jug B.
    Assume a >= b.
    Then we can fill A and transfer it to B multiple times until A is empty.
    
    Doing so we have the following quantities covered:
    {x | x = a - kb, for all natural k where 0 <= x <= a}

    When a is completely empty, b will have x remaining in it.
    We can then repeat the process of filling A and transferring it to B.
    This time, we have,

    {y | y = a - (b-x) - lb, for all natural l where 0 <= y <= a}

    If B has some remaining quantity of water, the first time transfer from A to
    B, we only reduce the contents of A by (b-x) from A, subsequently we reduce
    it by b each time.

    Substituting x into y,

    y = a - b + (a - kb) - lb
      = 2a - (k + 1 + l)b
      = 2a - mb
    
    for all m such that 0 <= y <= a

    We can repeat this process again and we note that the following quantities
    will be covered by simply transfering from A to B until A is empty.

    i.e. x = na - mb, for all natural n,m such that 0 <= x <= a.

    Therefore, (n-1)a < mb < na and we can restrict to looking at:
    (n-1)a // b < m < na // b + 1 for all n

    We note that when n = b, x = 0 for some m. At this point both jugs will be
    empty so we have reached the starting point and the pattern will repeat.
    This will be our exit condition (x = 0)
    """
    if a < b:
        a,b = b,a

    for n in range(b):
        M = range(n*a//b, (n+1)*a//b + 1)
        for m in M:
            x = (n+1)*a - (m+1)*b
            if x == 0:
                break
            if x > a:
                continue
            if x > 0 and x <= a and x == c:
                return True

    return False

if __name__ == "__main__":
    k = int(input().strip())

    for i in range(k):
        x = [int(x) for x in input().strip().split(' ')]
        print('YES') if can_fill(*x) else print('NO')
