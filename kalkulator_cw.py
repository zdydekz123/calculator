import unittest
from calculator import calculate
class TestCalculator(unittest.TestCase):
    def test_dodawanie(self):
        r = calculate(1, 2, '+')
        self.assertEqual(r, 3)
    def test_odejmowanie(self):
        r = calculate(200, 500, '-')
        self.assertEqual(r,-300)
    def test_dzielenie(self):
        r = calculate(30, 10, "/")
        self.assertEqual(r, 3)
    def test_modulo(self):
        r = calculate(25, 10, "%")
        self.assertEqual(r, 5)
    def test_potegowanie(self):
        r = calculate(2, 3, "**")
        self.assertEqual(r, 8)

def calculate(a, b, operacja):
    if operacja == "+":
        return a + b
    if operacja == "-":
        return a - b
    if operacja == "/":
        return a / b
    if operacja == "%":
        return a % b
    if operacja == "**":
        return a ** b
