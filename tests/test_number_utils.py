from coe_6710110065.number_utils import is_prime_list
import unittest
class PrimeListTest(unittest.TestCase):

    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_1_2_3_4_is_not_prime(self):
        prime_list = [1, 2, 3, 4]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    
    def test_give_5_7_9_is_not_prime(self):
        prime_list = [5, 7, 9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    
    def test_give_61_73_97_is_prime(self):
        prime_list = [61, 73, 97]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_1_2_3_4_5_6_7_8_9_is_not_prime(self):
        prime_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
    
    def test_give_4_6_8_10_is_not_prime(self):
        prime_list = [4, 6, 8, 10]   
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)