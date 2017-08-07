import unittest
import hist

class TestEqualizeHistogram(unittest.TestCase):
    def test_equalize_histogram_1(self):
        """ Test pre-conditions against [] and [1] """
        actual = (hist.equalize_histogram([]), hist.equalize_histogram([1]))
        expected = ([], [1])
        self.assertEqual(actual, expected)

    def test_equalize_histogram_2(self):
        """ Test against flat histogram """
        actual = hist.equalize_histogram([2,2,2,2])
        expected = [0,1,2,3]
        self.assertEqual(actual, expected)

    def test_equalize_histogram_3(self):
        """ Test against rising histogram """
        actual = hist.equalize_histogram([1,1,2,2,3,3])
        expected = [0,0,1,2,3,5]
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main(exit=False)
