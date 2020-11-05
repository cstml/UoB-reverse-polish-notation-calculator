import unittest
from result import Result
from srpn_model import SRPN_Model

class TestStringMethods(unittest.TestCase):

    def test_read_correctly_numbers(self):
        model = SRPN_Model()
        self.assertEqual(model.take_in("1"),1)
        self.assertEqual(model.take_in("12 13"),12)

if __name__ == '__main__':
    unittest.main()
