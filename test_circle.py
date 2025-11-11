import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
        
    def test_circle_area(self):
        res = area(10)
        expected = math.pi * 100
        self.assertEqual(res, expected)
    
    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
        
    def test_circle_perimeter(self):
        res = perimeter(10)
        expected = 2 * math.pi * 10
        self.assertEqual(res, expected)
    
    def test_area_negative_radius(self):
        self.assertRaises(ValueError, area, -5)
    
    def test_perimeter_negative_radius(self):
        self.assertRaises(ValueError, perimeter, -5)
    
    def test_area_string_input(self):
        self.assertRaises(TypeError, area, "10")
    
    def test_perimeter_string_input(self):
        self.assertRaises(TypeError, perimeter, "10")
    
    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)
    
    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)