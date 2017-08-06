import a1
import unittest

class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_1(self):
        """ Test empty list """
        price_changes = []
        actual = a1.stock_price_summary(price_changes)
        expected = (0,0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_2(self):
        """ Test only gains """
        price_changes = [1,1.2]
        actual = a1.stock_price_summary(price_changes)
        expected = (2.2,0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_3(self):
        """ Test only losses """
        price_changes = [-1,-1.2]
        actual = a1.stock_price_summary(price_changes)
        expected = (0,-2.2)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_4(self):
        """ Test only zeros """
        price_changes = [0,0]
        actual = a1.stock_price_summary(price_changes)
        expected = (0,0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_5(self):
        """ Test mixture of zero, positive and negative price changes """
        price_changes = [0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]
        actual = a1.stock_price_summary(price_changes)
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
