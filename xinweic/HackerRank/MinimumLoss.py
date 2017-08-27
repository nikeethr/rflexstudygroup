"""
    Solution:   Given an initial array A, form the array A2 sorted in decreasing order.
                We need only check adjacent elements for viability (indices in correct order).
                Time complexity: O(n log n)
    Conjecture: The optimal solution is a pair of elements that are adjacent in A2.
    Proof:      Assume that the conjecture is false and that the optimal solution is a pair (a, c)
                such that a and c are not adjacent in A2.
                We can find an element b which lies between a and c. 
                (a > b > c)
                => (b - c) < (a - c) and (a - b) < (a - c)
                Since (a, c) is the optimal solution, the pairs (b, c) and (a, b) must not be viable.
                => The relative order must be c-->b-->a which contradicts a-->c.
                Therefore, conjecture is true.
"""

import unittest

LIMIT = 10**17

def solve(n, A):
    A2 = [(x, i) for i, x in enumerate(A)]
    A2.sort(reverse=True)
    
    ans = LIMIT
    for i in range(0, n-1):
        if A2[i][1] < A2[i+1][1]:
            ans = min(ans, A2[i][0] - A2[i+1][0])

    return ans

class TestMinLoss(unittest.TestCase):
    def test_sample_0(self):
        act = solve(3, [5, 10, 3])
        exp = 2
        self.assertEqual(act, exp)

    def test_sample_1(self):
        act = solve(5, [20, 7, 8, 2, 5])
        exp = 2
        self.assertEqual(act, exp)


if __name__ == '__main__':
    unittest.main(exit=False)
    
    n = int(input())
    A = [int(x) for x in input().split()]
    print(solve(n, A))
