import unittest
from coe_6710110065.catmouse import cat_and_mouse  

class TestCatAndMouse(unittest.TestCase):
    
    def test_cat_a_wins(self):
        self.assertEqual(cat_and_mouse(2, 1, 3), "Cat A")

    def test_cat_b_wins(self):
        self.assertEqual(cat_and_mouse(1, 2, 3), "Cat B")

    def test_mouse_escapes(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")

    def test_edge_case_same_distance(self):
        self.assertEqual(cat_and_mouse(5, 7, 6), "Mouse C")

    def test_large_numbers(self):
        self.assertEqual(cat_and_mouse(50, 300, 175), "Mouse C")

