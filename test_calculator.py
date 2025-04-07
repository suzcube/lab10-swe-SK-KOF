import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self):
        pass

    def test_subtract(self):
        pass
    
    # Partner 1
    def test_multiply(self):
        pass

    def test_divide(self):
        pass
    
    # Partner 2
    def test_divide_by_zero(self):
        # call division function inside
        with self.assertRaises(ValueError):
            pass

    def test_logarithm(self):
        pass
    
    # Partner 1
    def test_hypotenuse(self):
        pass

    def test_hypotenuse_neg_sides(self):
        # Test for invalid side lengths
        with self.assertRaises(ValueError):
            pass
    
    # Can add more tests if you want

# Do not touch this
if __name__ == "__main__":
    unittest.main()