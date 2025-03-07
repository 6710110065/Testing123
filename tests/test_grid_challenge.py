from coe_6710110065.grid_challenge import gridChallenge
import unittest

class TestGridChallenge(unittest.TestCase):

    def test_sorted_rows_and_columns(self):
        grid = ["abc", "def", "ghi"]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_single_element(self):
        grid = ["a"]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_single_column(self):
        grid = ["a", "b", "c"]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_single_row(self):
        grid = ["abc"]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_empty_rows(self):
        grid = ["", ""]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_already_sorted_grid(self):
        grid = ["abc", "def", "ghi"]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_same_rows(self):
        grid = ["abc", "abc", "abc"]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_rows_with_identical_characters(self):
        grid = ["aaa", "bbb", "ccc"]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_unsorted_rows(self):
        grid = ["bac", "xyz"]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_unsorted_rows_and_columns(self):
        grid = ["zab", "acb", "cba"]
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_unsorted_columns(self):
        grid = ["abc", "bdf", "ceg"]
        expected_output = "YES"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)

    def test_unsorted_grid(self):
        grid = ["zab", "xyz", "def"]
        expected_output = "NO"
        result = gridChallenge(grid)
        self.assertEqual(result, expected_output)


