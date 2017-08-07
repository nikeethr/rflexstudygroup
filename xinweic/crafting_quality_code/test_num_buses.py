import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_zero(self):
        """Test num_buses with the zero case"""
        act = a1.num_buses(0)
        exp = 0
        self.assertEqual(exp, act)

    def test_num_buses_one(self):
        """Test num_buses with one person"""
        act = a1.num_buses(1)
        exp = 1
        self.assertEqual(exp, act)

    def test_num_buses_50_people(self):
        """Test num_buses with exactly 50 people (1 bus limit)"""
        act = a1.num_buses(50)
        exp = 1
        self.assertEqual(exp, act)

    def test_num_buses_51_people(self):
        """Test num_buses with 51 people (lowest to require 2 buses)"""
        act = a1.num_buses(51)
        exp = 2
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main(exit=False)
