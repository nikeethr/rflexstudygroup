#!/bin/python3

import sys

def find_all_paths(m, n):
    """ 
        (N, N) -> N

        Returns the number of possible paths to trace a matrix form start to end
        by only traversing right and down.

        (m, n) - rows by columns
        
        example:
        find_all_paths(3, 2)
        >>> 3
        
        AWAY can be represented as a 3 x 2 matrix
        
        A W
        W A
        A Y
        
        which can be traversed 3 ways
        
        A W
          A
          Y
        ---
        A
        W A
          Y
        ---
        A
        W
        A Y    
    """

    if min(n, m) <= 0:
        return 0
    elif min(n, m) == 1:
        return 1
    elif min(n, m) == 2:
        ret = max(n, m)
    else:
        x_0 = range(2, n+1)
        y_0 = range(2, m+1)

        for i in range(3, min(n, m)):
            x_1 = []
            x_1.append(x_0[1] + y_0[1])

            for j in range(i, n):
                x_1.append(x_1[j-i] + x_0[j-i+2])

            y_1 = []
            y_1.append(y_0[1] + x_0[1])

            for k in range(i, m):
                y_1.append(y_1[k-i] + y_0[k-i+2])

            x_0 = x_1
            y_0 = y_1

        if m > n:
            ret = x_0[1] + sum(y_0[1:])
        elif n < m:
            ret = y_0[1] + sum(x_0[1:])
        else:
            ret = y_0[1] + x_0[1]
            
        max_ret = 10**9 + 7
        return ret if ret <= max_ret else ret % max_ret


if __name__ == '__main__':
    t = int(input())
    test_cases = []

    for i in range(t):
        x = tuple(map(int, input().strip().split(' ')))
        test_cases.append(x)

    for test_case in test_cases:
        m = test_case[0]
        n = test_case[1]

        print(find_all_paths(m, n))
