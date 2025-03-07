from coe_6710110065.alternating_character import alternatingCharacters
import unittest

class TestAlternatingCharacters(unittest.TestCase):
    
    def test_given_AAAA_should_return_3(self):
        result = alternatingCharacters("AAAA")
        self.assertEqual(result, 3)

    def test_given_BBBBB_should_return_4(self):
        result = alternatingCharacters("BBBBB")
        self.assertEqual(result, 4)

    def test_given_empty_should_return_0(self):
        result = alternatingCharacters("")
        self.assertEqual(result, 0)

    def test_given_BABABA_should_return_0(self):
        result = alternatingCharacters("BABABA")
        self.assertEqual(result, 0)

    def test_given_AAABBB_should_return_4(self):
        result = alternatingCharacters("AAABBB")
        self.assertEqual(result, 4)

    def test_given_A_should_return_0(self):
        result = alternatingCharacters("A")
        self.assertEqual(result, 0)

    def test_given_AA_should_return_1(self):
        result = alternatingCharacters("AA")
        self.assertEqual(result, 1)

    def test_given_large_A_sequence_should_return_999(self):
        result = alternatingCharacters("A" * 1000)
        self.assertEqual(result, 999)