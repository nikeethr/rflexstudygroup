import a1
import unittest

class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_1(self):
        """ Test empty list """
        L = []
        k = 0
        a1.swap_k(L, k)
        expected = []
        self.assertEqual(L, expected)

    def test_swap_k_2(self):
        """ Test single element case and k = 0 case """
        L = [1]
        k = 0
        a1.swap_k(L, k)
        expected = [1]
        self.assertEqual(L, expected)

    def test_swap_k_3(self):
        """ Test k = 1 """
        L = [1,2,3,4,5,6]
        k = 1
        a1.swap_k(L, k)
        expected = [6,2,3,4,5,1]
        self.assertEqual(L, expected)

    def test_swap_k_4(self):
        """ Test 1 < k < len(L) // 2 """
        L = [1,2,3,4,5,6]
        k = 2
        a1.swap_k(L, k)
        expected = [5,6,3,4,1,2]
        self.assertEqual(L, expected)

    def test_swap_k_5(self):
        """ Test k = len(L) // 2 """
        L = [1,2,3,4,5,6]
        k = 3
        a1.swap_k(L, k)
        expected = [4,5,6,1,2,3]
        self.assertEqual(L, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
