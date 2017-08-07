import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_no_swaps(self):
        """Test with no swaps"""
        act = [1, 2, 3, 4]
        a1.swap_k(act, 0)
        exp = [1, 2, 3, 4]
        self.assertEqual(act, exp)

    def test_swap_k_one_swap(self):
        """Test with just one swap"""
        act = [1, 2, 3, 4]
        a1.swap_k(act, 1)
        exp = [4, 2, 3, 1]
        self.assertEqual(act, exp)
        
    def test_swap_k_even(self):
        """Test with even length list"""
        act = [1, 2, 3, 4, 5, 6]
        a1.swap_k(act, 3)
        exp = [4, 5, 6, 1, 2, 3]
        self.assertEqual(act, exp)
        
    def test_swap_k_odd(self):
        """Test with odd length list"""
        act = [1, 2, 3, 4, 5]
        a1.swap_k(act, 2)
        exp = [4, 5, 3, 1, 2]
        self.assertEqual(act, exp)
        

if __name__ == '__main__':
    unittest.main(exit=False)
