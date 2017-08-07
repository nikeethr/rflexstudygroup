import a1
import unittest

class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_1(self):
        """ Test 0 people to transport """
        n = 0
        actual = a1.num_buses(n)
        expected = 0
        self.assertEqual(actual, expected)

    def test_num_buses_2(self):
        """ Test boundary case of 50 people to transport """
        n = 50
        actual = a1.num_buses(n)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_3(self):
        """ Test 125 people to transport to check for appropriate rounding """
        n = 125
        actual = a1.num_buses(n)
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
