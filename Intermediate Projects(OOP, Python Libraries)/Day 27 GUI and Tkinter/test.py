import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_miles_to_km(self):
        calculator = Calculator()

        result = calculator.miles_to_km(1)
        self.assertEqual(result, 1.61)  

    def test_miles_to_km_zero(self):
        calculator = Calculator()
        result = calculator.miles_to_km(0)
        self.assertEqual(result, 0)

    def test_miles_to_km_negative(self):
        calculator = Calculator()
        result = calculator.miles_to_km(-2)
        self.assertEqual(result, -3.22)

    def test_miles_to_km_decimal(self):
        calculator = Calculator()
        result = calculator.miles_to_km(2.5)
        self.assertEqual(result, 4.02)

if __name__ == '__main__':
    unittest.main()