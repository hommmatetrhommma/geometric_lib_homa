import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
       
    def test_rectangle_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)
    
    def test_zero_perimeter(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_rectangle_perimeter(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)
    
    def test_area_negative_side_a(self):
        self.assertRaises(ValueError, area, -5, 3)
    
    def test_area_negative_side_b(self):
        self.assertRaises(ValueError, area, 5, -3)
    
    def test_area_both_negative(self):
        self.assertRaises(ValueError, area, -5, -3)
    
    def test_area_string_input(self):
        self.assertRaises(TypeError, area, "10", 5)

    def test_perimeter_negative_side_a(self):
        self.assertRaises(ValueError, perimeter, -5, 3)
    
    def test_perimeter_negative_side_b(self):
        self.assertRaises(ValueError, perimeter, 5, -3)
    
    def test_perimeter_both_negative(self):
        self.assertRaises(ValueError, perimeter, -5, -3)
