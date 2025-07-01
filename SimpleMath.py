import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(5, 4)
        self.assertEqual(result, 9)

# Pour lancer le test si le fichier est exécuté directement
if __name__ == '__main__':
    unittest.main()