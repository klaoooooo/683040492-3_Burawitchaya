# test_area.py
import unittest
from area import calculate_area

class TestAreaCalculation(unittest.TestCase):
    def test_positive_numbers(self):
        # Tests with positive numbers (put in several tests here for different cases)
        self.assertEqual(calculate_area(4, 5), 20)

    def test_zero(self):
        # Test with zero (put in several tests here for different cases)
        self.assertEqual(calculate_area(0, 5), 0)    
        self.assertEqual(calculate_area(5, 0), 0)   
        self.assertEqual(calculate_area(0, 0), 0) 

    def test_negative_numbers(self):
        # Test with negative numbers (put in several tests here for different cases)
        with self.assertRaises(ValueError):
            calculate_area(-5,5)
        with self.assertRaises(ValueError):
            calculate_area(5,-5)
        with self.assertRaises(ValueError):
            calculate_area(-5,-5)
    
    def test_type(self):
        with self.assertRaises(TypeError):
            calculate_area("k", 5)
        with self.assertRaises(TypeError):
            calculate_area(5, "l")
        with self.assertRaises(TypeError):
            calculate_area("a", "o")
        with self.assertRaises(TypeError):
            calculate_area(["k","la"], ["o"])
          
if __name__ == '__main__':
    unittest.main()