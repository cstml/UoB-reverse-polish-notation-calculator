import unittest

from result import Result 
from srpn_model import SRPN_Model 
from srpn_view import SRPN_View 

class TestStringMethods(unittest.TestCase):

    def test_read_correctly_numbers(self):
        model = SRPN_Model()
        result_list = []
        self.assertEqual(model.take_in("1"), [Result(2,1)] )
        self.assertEqual(model.take_in("2 3 "), [Result(2,2),Result(2,3)] )

if __name__ == '__main__':
    unittest.main()
