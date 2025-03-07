from coe_6710110065.two_character import alternate
import unittest

class TestAlternateFunction(unittest.TestCase):
    
    def test_simple_alternating(self):
        s = "ababab"
        expected_output = 6
        result = alternate(s)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_no_alternation(self):
        s = "aaaa"
        expected_output = 0
        result = alternate(s)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_empty_string(self):
        s = ""
        expected_output = 0
        result = alternate(s)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_single_character(self):
        s = "a"
        expected_output = 0
        result = alternate(s)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_repeated_alternating(self):
        s = "abababababab"
        expected_output = 12
        result = alternate(s)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_alternating_at_end(self):
        s = "xxabab"
        expected_output = 4
        result = alternate(s)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
    
    def test_alternating_at_start(self):
        s = "ababxx"    
        expected_output = 4
        result = alternate(s)
        self.assertEqual(result, expected_output, f'Should be {expected_output}')
