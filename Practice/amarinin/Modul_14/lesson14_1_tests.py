import unittest
from lesson14_1_roma import to_roman


class TestUM(unittest.TestCase):
    def setUp(self):
        print("Погнали!")

    def tearDown(self):
        print("Приехали")

    def test_number(self):
        for v, s in {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                     90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
                     4: 'IV', 1: 'I', 0: 'Должно быть 1 - 5000',
                     5001: 'Должно быть 1 - 5000', 'r': 'Должно быть число'}.items():
            self.assertTrue(to_roman(str(v)), s)
            print(f"test {v} - {s}")


if __name__ == "__main__":
    unittest.main()
