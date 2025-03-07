from coe_6710110065.caesar_cipher import caesarCipher
import unittest

class TestCaesarCipher(unittest.TestCase):
    
    def test_rotation_with_wraparound(self):
        input_str = "xyzXYZ"
        k = 3
        expected_output = "abcABC"
        result = caesarCipher(input_str, k)
        self.assertEqual(result, expected_output)
    
    def test_large_rotation(self):
        input_str = "abcABC"
        k = 29  
        expected_output = "defDEF"
        result = caesarCipher(input_str, k)
        self.assertEqual(result, expected_output)
    
    def test_non_alpha_characters(self):
        input_str = "hello-world!"
        k = 5
        expected_output = "mjqqt-btwqi!"
        result = caesarCipher(input_str, k)
        self.assertEqual(result, expected_output)
    
    def test_no_rotation(self):
        input_str = "unchanged"
        k = 0
        expected_output = "unchanged"
        result = caesarCipher(input_str, k)
        self.assertEqual(result, expected_output)
    
    def test_full_rotation(self):
        input_str = "rotate"
        k = 26  
        expected_output = "rotate"
        result = caesarCipher(input_str, k)
        self.assertEqual(result, expected_output)
    
    def test_mixed_case(self):
        input_str = "AbCzYx"
        k = 4
        expected_output = "EfGdCb"
        result = caesarCipher(input_str, k)
        self.assertEqual(result, expected_output)