import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_empty(self):
        """Test with empty list"""
        act = a1.stock_price_summary([])
        exp = (0.0, 0.0)
        # assertEqual(exp, act) cannot be used due to floating point errors
        self.assertEqual(type(act), type(exp))
        self.assertEqual(len(act), len(exp))
        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_all_positive(self):
        """Test with all positive numbers"""
        act = a1.stock_price_summary([0.1, 0.2, 0.3, 0.4])
        exp = (1.0, 0.0)
        self.assertEqual(type(act), type(exp))
        self.assertEqual(len(act), len(exp))
        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_all_negative(self):
        """Test with all negative numbers"""
        act = a1.stock_price_summary([-0.1, -0.2, -0.3, -0.4])
        exp = (0.0, -1.0)
        self.assertEqual(type(act), type(exp))
        self.assertEqual(len(act), len(exp))
        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])

    def test_stock_price_summary_mixture(self):
        """Test with mix of positive and negative numbers"""
        act = a1.stock_price_summary([-0.1, 0.2, -0.3, 0.4])
        exp = (0.6, -0.4)
        self.assertEqual(type(act), type(exp))
        self.assertEqual(len(act), len(exp))
        self.assertAlmostEqual(act[0], exp[0])
        self.assertAlmostEqual(act[1], exp[1])


if __name__ == '__main__':
    unittest.main(exit=False)
