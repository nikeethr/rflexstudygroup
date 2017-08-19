import unittest


def solve(L):
    """
    (string) -> string

    Given a string as input, forms a grid with minimum area.
    Returns the grid as a space separated string, column first.
    """
    n = len(L)

    lower_bound, upper_bound = None, None
    for x in range(1, n+1):
        if x * x < n:
            lower_bound = x
            upper_bound = x + 1
        elif x * x == n:
            lower_bound = x
            upper_bound = x

    min_area, best_row, best_col = None, None, None
    for row in range(lower_bound, upper_bound + 1):
        for col in range(row, upper_bound + 1):
            area = row * col
            if area >= n and (not min_area or area < min_area):
                min_area = area
                best_row, best_col = row, col

    assert min_area is not None, "Did not find a viable answer."

    result = []
    for col in range(best_col):
        column_string = ''
        for index in range(col, n, best_col):
            column_string += L[index]
        result.append(column_string)

    return ' '.join(result)


class TestEncryption(unittest.TestCase):
    """ Test class for solve function. """

    def test_sample_1(self):
        """Test with sample 1"""
        act = solve('haveaniceday')
        exp = 'hae and via ecy'
        self.assertEqual(exp, act)

    def test_sample_2(self):
        """Test with sample 2"""
        act = solve('feedthedog')
        exp = "fto ehg ee dd"
        self.assertEqual(exp, act)

    def test_sample_3(self):
        """Test with sample 3"""
        act = solve('chillout')
        exp = 'clu hlt io'
        self.assertEqual(exp, act)

    def test_sample_length_one(self):
        """Test with length of one"""
        act = solve('c')
        exp = 'c'
        self.assertEqual(exp, act)


if __name__ == '__main__':
    unittest.main(exit=False)

    L = input()
    print(solve(L))
