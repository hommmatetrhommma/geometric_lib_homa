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
