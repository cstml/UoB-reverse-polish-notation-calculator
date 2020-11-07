import unittest

try:
    from classes.result import Result as R
    from classes.srpn_model import SRPN_Model
    from classes.srpn_view import SRPN_View
except Exception as e:
    print(e)

class TestStringMethods(unittest.TestCase):
    """
    Unit test for input 
    """

    def test_read_correctly_numbers(self):
        model = SRPN_Model()
        self.assertEqual(model.take_in("1"), [R(2,1)] )
        self.assertEqual(model.take_in("2 3 "), [R(2,2),R(2,3)] )

    def test_saturates_numbers(self):
        model = SRPN_Model()
        self.assertEqual(model.take_in("1111111111111111111111"), [R(2,2147483647)])
        self.assertEqual(model.take_in("-111111111111111111111"), [R(2,-2147483648)])

class TestPrintMethods(unittest.TestCase):

    def test_initial_message(self):
        view = SRPN_View()
        self.assertEqual(view.disp_wlcm(), "You can now start interacting with the SRPN calculator" )

if __name__ == '__main__':
    unittest.main()
