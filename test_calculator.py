import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        # Existing test case
        self.assertEqual(self.calc.add(1, 2), 3)
        # Additional test cases
        self.assertEqual(self.calc.add(-5, -3), -8)  # Adding negatives
        self.assertEqual(self.calc.add(0, 0), 0)     # Adding zeros

    def test_subtract(self):
        # Test case 1
        self.assertEqual(self.calc.subtract(10, 5), 5)
        # Test case 2
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        # Test case 1
        self.assertEqual(self.calc.multiply(3, 2), 6)
        # Test case 2
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    def test_divide(self):
        # Test case 1
        self.assertEqual(self.calc.divide(9, 3), 3)
        # Test case 2 (special case: not divisible evenly)
        self.assertEqual(self.calc.divide(10, 3), 3)  # Integer division
        # Test case for divide by zero
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_modulo(self):
        # Test case 1
        self.assertEqual(self.calc.modulo(10, 3), 1)
        # Test case 2
        self.assertEqual(self.calc.modulo(20, 7), 6)
        # Test case for modulo by zero
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)

if __name__ == '__main__':
    unittest.main()
