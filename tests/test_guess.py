import unittest
from unittest.mock import patch
from coe_6710110065.guess import guess_int,guess_float

class TestStubGuessFunctions(unittest.TestCase):
    
    @patch('coe_6710110065.guess.randint')
    def test_guess_int(self, mock_randint):
        mock_randint.return_value = 10

        result = guess_int(5, 15)
        self.assertEqual(result, 10)
        mock_randint.assert_called_once_with(5, 15)
    
    @patch('coe_6710110065.guess.uniform')
    def test_guess_float(self, mock_uniform):
        mock_uniform.return_value = 4.56

        result = guess_float(2.0, 6.0)
        self.assertEqual(result, 4.56)
        mock_uniform.assert_called_once_with(2.0, 6.0)
    
    @patch('coe_6710110065.guess.randint')
    def test_guess_int_range(self, mock_randint):
        mock_randint.return_value = 18

        result = guess_int(15, 25)
        self.assertEqual(result, 18)
        self.assertTrue(15 <= result <= 25)
    
    @patch('coe_6710110065.guess.uniform')
    def test_guess_float_range(self, mock_uniform):
        mock_uniform.return_value = 5.75

        result = guess_float(4.0, 7.0)
        self.assertEqual(result, 5.75)
        self.assertTrue(4.0 <= result <= 7.0)
    
    @patch('coe_6710110065.guess.randint')
    def test_guess_int_multiple_calls(self, mock_randint):
        mock_randint.side_effect = [6, 14, 2]

        self.assertEqual(guess_int(1, 20), 6)
        self.assertEqual(guess_int(1, 20), 14)
        self.assertEqual(guess_int(1, 20), 2)
        self.assertEqual(mock_randint.call_count, 3)
