#https://github.com/suzcube/lab10-swe-SK-KOF.git
# Partner 1: Katie Flanagan
# Partner 2: Suzanne Kerns
import unittest
import calculator
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(calculator.add(2,3), 5)
        self.assertEqual(calculator.add(0, 3), 3)
        self.assertNotEqual(calculator.add(5, 5), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(9, 3), 6)
        self.assertEqual(calculator.subtract(5, 5), 0)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(4, 5), 20)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(3, -9), -3)
        self.assertAlmostEqual(div(3, 1), 0.3333, places=4)


    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertNotEqual(calculator.div(0, 5), -1)
            self.assertNotEqual(calculator.div(0, 4), -1)
            self.assertNotEqual(calculator.div(0, 0), 0)

    #     fill in code

    def test_logarithm(self):
        self.assertEqual(logarithm(10, 10), 1)
        self.assertEqual(logarithm(4, 2), 2)
        self.assertNotEqual(logarithm(20, 100), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertNotEqual(calculator.logarithm(0, 0), 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            self.assertNotEqual(calculator.logarithm(1, -1), 10)

    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(5, 12), 13)
        self.assertEqual(calculator.hypotenuse(3, 4), 5)
        self.assertNotEqual(calculator.hypotenuse(32, 41), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            self.assertNotEqual(calculator.square_root(-4), 3)
        self.assertEqual(calculator.square_root(1), 1)
        self.assertEqual(calculator.square_root(64), 8)



# Do not touch this
if __name__ == "__main__":
    unittest.main()