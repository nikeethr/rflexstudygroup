"""
Solution:
1. We need only consider each number (mod k).
   Count the number of times each number appears
2. For each i in 0:k, the additive inverse of i is exactly (k - i).
   We cannot take a subset containing both i and (k - i).
   If we were to take one element of i, we should take all of them.
   The same reasoning applies for (k - i).
   Therefore, we should take the higher count out of i and (k - i).
3. Two special cases:
   a. 0 is its own additive inverse
   b. if k is even, (k / 2) is its own additive inverse
4. For the special cases, we can only take at 1 element
"""
import unittest


def solve(n, k, array):
    bucket = [0] * k
    for x in array:
        bucket[x % k] += 1

    total = 0

    # zero case
    total += (bucket[0] >= 1)

    # even case (k // 2)
    total += int((k % 2 == 0) and (bucket[k // 2] >= 1))

    for i in range(1, (k + 1) // 2):
        total += max(bucket[i], bucket[k - i])

    return total


class TestNonDivisibleSubset(unittest.TestCase):
    """ Test class for solve function. """

    def test_sample(self):
        """Test with sample provided"""
        act = solve(4, 3, [1, 7, 2, 4])
        exp = 3
        self.assertEqual(exp, act)

    def test_one_element(self):
        """Test with just one element provided"""
        act = solve(4, 3, [7])
        exp = 1
        self.assertEqual(exp, act)

    def test_odd_k(self):
        """Test with odd k"""
        act = solve(4, 5, [0, 0, 1, 1, 1, 3, 3, 4, 4])
        exp = 1 + 3 + 2
        self.assertEqual(exp, act)

    def test_even_k(self):
        """Test with even k"""
        act = solve(4, 6, [0, 0, 1, 1, 1, 3, 3, 4, 4, 5, 5])
        exp = 1 + 3 + 2 + 1
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main(exit=False)

    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    print(solve(n, k, array))
