from coe_6710110065.fizzbuzz import fizzbuzz
import unittest
class fizzbuzzTest(unittest.TestCase):

    def test_give_7_return_7(self):
        result = fizzbuzz(7)
        self.assertEqual(result, 7)

    def test_give_3_return_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, "Fizz")
    
    def test_give_5_return_buzz(self):
        result = fizzbuzz(5)   
        self.assertEqual(result, "Buzz")
    
    def test_give_15_return_fizzbuzz(self):
        result = fizzbuzz(15)
        self.assertEqual(result, "FizzBuzz")
    
    def test_give_30_return_fizzbuzz(self):
        result = fizzbuzz(30)
        self.assertEqual(result, "FizzBuzz")