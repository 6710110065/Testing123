from coe_6710110065.staircase import staircase
import unittest

class TestStaircase(unittest.TestCase):

    def test_give_2_with_hash_should_be_hh(self):
        # Arrange
        n = 2
        pattern = '#'
        expected_output = "#\n##"  
        # Act
        result = staircase(n, pattern)
        # Assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_3_with_star_should_be_star_stair(self):
        # Arrange
        n = 3
        pattern = '*'
        expected_output = "*\n**\n***"   
        # Act
        result = staircase(n, pattern)
        # Assert
        self.assertEqual(result, expected_output, f'Should be {expected_output}')

    def test_give_0_should_raise_error_invalid_n(self):
        # Arrange
        n = 0  
        # Act & Assert
        with self.assertRaises(ValueError):
            staircase(n, '#')  

    def test_give_31_should_raise_error_invalid_n(self):
        # Arrange
        n = 31  
        # Act & Assert
        with self.assertRaises(ValueError):
            staircase(n, '#')


