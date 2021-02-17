import pytest
import unittest
from pageObjects.unittest.maths_calc import Mathcalculator
from utilities.customLogger import LogGen
import numpy as np

class TestClass(unittest.TestCase):
    logger = LogGen.loggen()
    math_calc = Mathcalculator()
    a = np.inf
    b = -np.inf

    @pytest.mark.unittest
    def test_addition(self):
        """Addition test function"""
        print("\n")
        self.logger.info("****Started Addition Test****")
        self.assertEqual(self.math_calc.add(6, 6), 12)
        self.assertEqual(self.math_calc.add(3, -3), 0)
        self.assertEqual(self.math_calc.add(-3.0, 6.0), 3.0)
        # Non numbers
        self.assertEqual(self.math_calc.add('m', 'n'), False)
        # Infinite numbers
        self.assertEqual(self.math_calc.add(self.a, 4), False)
        # Infinite numbers
        self.assertEqual(self.math_calc.add(6, self.b), False)
        # Non numbers
        self.assertEqual(self.math_calc.add('?', '+'), False)
        self.logger.info("****Ended Addition Test****")

    @pytest.mark.unittest
    def test_multiplication(self):
        """Multiplication test function"""
        print("\n")
        self.logger.info("****Started Multiply Test****")
        self.assertEqual(self.math_calc.multiply(3, 3), 9)
        self.assertEqual(self.math_calc.multiply(3.0, -3.0), -9.0)
        self.assertEqual(self.math_calc.multiply(-3, -3), 9)
        self.assertEqual(self.math_calc.multiply(-6.0, -6.0), 36.0)
        # Non numbers
        self.assertEqual(self.math_calc.multiply('m', 'n'), False)
        # Infinite numbers
        self.assertEqual(self.math_calc.multiply(self.a, 4), False)
        # Infinite numbers
        self.assertEqual(self.math_calc.multiply(6, self.b), False)
        # Non numbers
        self.assertEqual(self.math_calc.multiply('?', '+'), False)
        self.logger.info("****Ended Multiply Test****")

    @pytest.mark.unittest
    def test_division(self):
        """Division test function"""
        print("\n")
        self.logger.info("****Started Division Test****")
        self.assertEqual(self.math_calc.divide(10, 5), 2.0)
        self.assertEqual(self.math_calc.divide(3, 3), 1.0)
        self.assertEqual(self.math_calc.divide(3.0, -3.0), -1.0)
        self.assertEqual(self.math_calc.divide(-3, -3), 1.0)
        # Divide by Zero
        self.assertEqual(self.math_calc.divide(-6, 0), False)
        # Divide by Zero
        self.assertEqual(self.math_calc.divide(0, 0), False)
        self.assertEqual(self.math_calc.divide(0, 6), 0.0)
        # Non numbers
        self.assertEqual(self.math_calc.divide('m', 'n'), False)
        # Infinite numbers
        self.assertEqual(self.math_calc.divide(self.a, 4), False)
        # Infinite numbers
        self.assertEqual(self.math_calc.divide(6, self.b), False)
        # Non numbers
        self.assertEqual(self.math_calc.divide('?', '+'), False)
        self.logger.info("****Ended Division Test****")

    @pytest.mark.unittest
    def test_subtract(self):
        """Addition test function"""
        self.logger.info("****Started Subtraction Test****")
        print("\n")
        self.assertEqual(self.math_calc.subtract(6, 6), 0)
        self.assertEqual(self.math_calc.subtract(3, -3), 6)
        self.assertEqual(self.math_calc.subtract(-3.0, 6.0), -9.0)
        # Non numbers
        self.assertEqual(self.math_calc.subtract('m', 'n'), False)
        # Infinite numbers
        self.assertEqual(self.math_calc.subtract(self.a, 4), False)
        # Infinite numbers
        self.assertEqual(self.math_calc.subtract(6, self.b), False)
        # Non numbers
        self.assertEqual(self.math_calc.subtract('?', '+'), False)
        self.logger.info("****Ended Subtraction Test****")
