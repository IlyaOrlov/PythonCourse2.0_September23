import unittest
import to_roma


class TestUM(unittest.TestCase):
    def setUp(self):
        print("Погнали!")

    def tearDown(self):
        print("Приехали")

    def test_number(self):
        for v, s in {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                     90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
                     4: 'IV', 1: 'I'}.items():
            self.assertTrue(to_roma.to_roman(str(v)), s)
            print(f"test {v} - {s}")

    def test_reises(self):
        for i in ["hhh", "0", "5001"]:
            self.assertRaises(x := to_roma.NonValidInput, to_roma.to_roman, i)
            print("Ok", i,  x.__name__)


if __name__ == "__main__":
    unittest.main()
