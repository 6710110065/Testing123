from coe_6710110065.funnystring import funnyString
import unittest

class TestFunnyString(unittest.TestCase):

    def test_given_acxz_should_return_funny(self):
        result = funnyString("acxz")
        self.assertEqual(result, "Funny")

    def test_given_bcxz_should_return_not_funny(self):
        result = funnyString("bcxz")
        self.assertEqual(result, "Not Funny")
    
    def test_given_abc_should_return_funny(self):
        result = funnyString("abc") 
        self.assertEqual(result, "Funny")

    def test_given_single_char_a_should_return_funny(self):
        result = funnyString("j")
        self.assertEqual(result, "Funny")

    def test_given_aa_should_return_funny(self):
        result = funnyString("jj")
        self.assertEqual(result, "Funny")

    def test_given_racecar_should_return_funny(self):
        result = funnyString("racecar")
        self.assertEqual(result, "Funny")
