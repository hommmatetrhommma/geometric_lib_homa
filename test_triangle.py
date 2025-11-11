import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_triangle_area(self):
        res = area(10, 5)
        self.assertEqual(res, 25)
    
    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
        
    def test_triangle_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_area_negative_base(self):
        self.assertRaises(ValueError, area, -5, 3)
    
    def test_area_negative_height(self):
        self.assertRaises(ValueError, area, 5, -3)
    
    def test_area_both_negative(self):
        self.assertRaises(ValueError, area, -5, -3)
    
    def test_perimeter_negative_side_a(self):
        self.assertRaises(ValueError, perimeter, -5, 3, 4)
    
    def test_perimeter_negative_side_b(self):
        self.assertRaises(ValueError, perimeter, 5, -3, 4)
    
    def test_perimeter_negative_side_c(self):
        self.assertRaises(ValueError, perimeter, 5, 3, -4)
    
    def test_perimeter_all_negative(self):
        self.assertRaises(ValueError, perimeter, -5, -3, -4)
    
    def test_area_string_input(self):
        self.assertRaises(TypeError, area, "10", 5)