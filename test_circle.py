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