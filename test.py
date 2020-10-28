import unittest
from main import Calculator

class TestStringMethods(unittest.TestCase):

    def read_correctly(self):
        calculator = Calculator()
        self.assertEqual(calculator.read("1"),['1'])
        self.assertEqual(calculator.read("1"),['1','1'])
        self.assertEqual(calculator.read("2"),['1','1','2'])

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
