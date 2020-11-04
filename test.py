import unittest
from calculator import Calculator

class TestStringMethods(unittest.TestCase):

    def test_read_correctly_numbers(self):
        calculator = Calculator()
        self.assertEqual(calculator.read("1"),["1"])
        self.assertEqual(calculator.read("1"),['1','1'])
        self.assertEqual(calculator.read("2 3 4"),['1','1','2','3','4'])
        self.assertEqual(calculator.read("100"),['1','1','2','3','4','100'])

    def test_read_correctly_signs(self):
        calculator = Calculator()
        self.assertEqual(calculator.read("1"),['1'])
        self.assertEqual(calculator.read("2"),['1','2'])
        self.assertEqual(calculator.read("+"),["3"])

        calculator2 = Calculator()
        self.assertEqual(calculator2.read("+++++"),['+++++'])

if __name__ == '__main__':
    unittest.main()
