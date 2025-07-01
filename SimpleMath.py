import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def soustraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    # Tests pour addition
    def test_addition_integers(self):
        self.assertEqual(SimpleMath.addition(5, 4), 9)

    def test_addition_negative_numbers(self):
        self.assertEqual(SimpleMath.addition(-3, -7), -10)

    def test_addition_mixed_signs(self):
        self.assertEqual(SimpleMath.addition(-5, 10), 5)

    def test_addition_zero(self):
        self.assertEqual(SimpleMath.addition(0, 0), 0)
        self.assertEqual(SimpleMath.addition(0, 9), 9)

    def test_addition_floats(self):
        self.assertAlmostEqual(SimpleMath.addition(1.5, 2.3), 3.8, places=5)

    def test_addition_large_numbers(self):
        self.assertEqual(SimpleMath.addition(1_000_000_000, 2_000_000_000), 3_000_000_000)

    # Tests pour soustraction
    def test_soustraction_integers(self):
        self.assertEqual(SimpleMath.soustraction(10, 4), 6)

    def test_soustraction_negative_numbers(self):
        self.assertEqual(SimpleMath.soustraction(-3, -7), 4)

    def test_soustraction_mixed_signs(self):
        self.assertEqual(SimpleMath.soustraction(-5, 10), -15)

    def test_soustraction_zero(self):
        self.assertEqual(SimpleMath.soustraction(0, 0), 0)
        self.assertEqual(SimpleMath.soustraction(0, 9), -9)

    def test_soustraction_floats(self):
        self.assertAlmostEqual(SimpleMath.soustraction(5.5, 2.2), 3.3, places=5)

    def test_soustraction_large_numbers(self):
        self.assertEqual(SimpleMath.soustraction(2_000_000_000, 1_000_000_000), 1_000_000_000)

if __name__ == '__main__':
    unittest.main()
