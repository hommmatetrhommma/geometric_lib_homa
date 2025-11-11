import unittest
from square import area, perimeter
class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
       
    def test_square_area(self):
        res = area(10)
        self.assertEqual(res, 100)
    
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
    
    def test_area_negative_side(self):
        self.assertRaises(ValueError, area, -5)
    
    def test_perimeter_negative_side(self):
        self.assertRaises(ValueError, perimeter, -5)
    
    def test_area_string_input(self):
        self.assertRaises(TypeError, area, "10")
    
    def test_perimeter_string_input(self):
        self.assertRaises(TypeError, perimeter, "10")