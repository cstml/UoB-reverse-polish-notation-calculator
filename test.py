import unittest

try:
    from classes.error import Error
    from classes.error import Error_Type as ERROR
    from classes.result import Result as R
    from classes.result import Result_Type as RT
    from classes.srpn_model import SRPN_Model
    from classes.srpn_view import SRPN_View
    
except Exception as e:
    print(e)

class TestFirstSection(unittest.TestCase):
    """
    Unit test for input  created based on the lab sheet 
    """

    def test_read_correctly_numbers(self):
        """
        Basic reading numbers 
        single
        multiline
        negtive
        """
        model = SRPN_Model()
        self.assertEqual(model.take_in(1), [R(RT.IN, 1)] )
        self.assertEqual(model.take_in("2 3 "), [R(RT.IN, 2), R(RT.IN, 3)] )
        self.assertEqual(model.take_in(" -3 -5"), [R(RT.IN, -3), R(RT.IN, -5)] )

    def test_saturates_numbers(self):
        """
        Test if it is saturating 
        """
        model = SRPN_Model()
        self.assertEqual(model.take_in("1111111111111111111111"), [R(RT.IN, 2147483647)])
        self.assertEqual(model.take_in("-111111111111111111111"), [R(RT.IN, -2147483648)])

    def test_1_1(self):
        model = SRPN_Model()
        self.assertEqual(model.take_in("10"), [R(RT.IN, 10)])
        self.assertEqual(model.take_in("2"), [R(RT.IN, 2)])
        self.assertEqual(model.take_in("+"), [R(RT.OP, 12)])
        self.assertEqual(model.take_in("="), [R(RT.DT, 12)])


    def test_1_2(self):
        model = SRPN_Model()
        self.assertEqual(model.take_in("11"), [R(RT.IN, 11)])
        self.assertEqual(model.take_in("3"), [R(RT.IN, 3)])
        self.assertEqual(model.take_in("-"), [R(RT.OP, 8)])
        self.assertEqual(model.take_in("="), [R(RT.DT, 8)])

    def test_1_3(self):
        model = SRPN_Model()
        nr = 9
        self.assertEqual(model.take_in(str(nr)), [R(RT.IN, nr)])
        nr = 4
        self.assertEqual(model.take_in(str(nr)), [R(RT.IN, nr)])
        op = "*"
        res = 9*4
        self.assertEqual(model.take_in(op), [R(RT.OP, res)])
        self.assertEqual(model.take_in("="), [R(RT.DT, res)])

    def test_1_4(self):
        model = SRPN_Model()
        nr1 = 11
        self.assertEqual(model.take_in(str(nr1)), [R(RT.IN, nr1)])
        nr2 = 3
        self.assertEqual(model.take_in(str(nr2)), [R(RT.IN, nr2)])
        op = "/"
        res = nr1 // nr2
        self.assertEqual(model.take_in(op), [R(RT.OP, res)])
        self.assertEqual(model.take_in("="), [R(RT.DT, res)])

    def test_1_5(self):
        model = SRPN_Model()
        nr1 = 11
        self.assertEqual(model.take_in(str(nr1)), [R(RT.IN, nr1)])
        nr2 = 3
        self.assertEqual(model.take_in(str(nr2)), [R(RT.IN, nr2)])
        op = "%"
        res = nr1 % nr2
        self.assertEqual(model.take_in(op), [R(RT.OP, res)])
        self.assertEqual(model.take_in("="), [R(RT.DT, res)])

class Test_Second_Section(unittest.TestCase):
    def test_2_1(self):
        model2 = SRPN_Model()
        nr1 = 3
        self.assertEqual(model2.take_in(str(nr1)), [R(RT.IN, nr1)])
        nr2 = 3
        self.assertEqual(model2.take_in(str(nr2)), [R(RT.IN, nr2)])
        op = "*"
        res1 = nr1 * nr2
        self.assertEqual(model2.take_in(op), [R(RT.OP, res1)])

        nr3 = 4
        self.assertEqual(model2.take_in(str(nr3)), [R(RT.IN, nr3)])
        nr4 = 4
        self.assertEqual(model2.take_in(str(nr4)), [R(RT.IN, nr4)])
        op = "*"
        res = nr3 * nr4
        self.assertEqual(model2.take_in(op), [R(RT.OP, res)])
        op = "+"
        res = res1 + res
        self.assertEqual(model2.take_in(op), [R(RT.OP, res)])
        self.assertEqual(model2.take_in("="), [R(RT.DT, res)])

    def test_2_2(self):
        model3 = SRPN_Model()
        alist = []
        nr1 = 1234
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model3.take_in(str(nr1)), [r1])

        nr2 = 2345
        r2 = R(RT.IN, nr2)
        alist.append(nr2)
        self.assertEqual(model3.take_in(str(nr2)), [r2])

        nr3 = 3456
        r3 = R(RT.IN, nr3)
        alist.append(nr3)
        self.assertEqual(model3.take_in(str(nr3)), [r3])

        op = "d"
        self.assertEqual(model3.take_in(op), [R(RT.DS, alist)])

        op = "+"
        alist[-2] += alist[-1]
        alist.pop(-1)
        self.assertEqual(model3.take_in(op), [R(RT.OP, alist[-1])])

        op = "d"
        self.assertEqual(model3.take_in(op), [R(RT.DS, alist)])

        op = "+"
        alist[-2] += alist[-1]
        alist.pop(-1)
        self.assertEqual(model3.take_in(op), [R(RT.OP, alist[-1])])

        op = "d"
        self.assertEqual(model3.take_in(op), [R(RT.DS, alist)])

        op = "="
        self.assertEqual(model3.take_in(op), [R(RT.DT, alist[-1])])

class Test_Third_Section(unittest.TestCase):
    def test_3_1(self):
        model = SRPN_Model()
        alist = []

        nr1 = 2147483647
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model.take_in(str(nr1)), [r1])

        nr2 = 1
        r2 = R(RT.IN, nr2)
        alist.append(nr2)
        self.assertEqual(model.take_in(str(nr2)), [r2])

        op = "+"
        alist[-2] += alist[-1]
        alist[-2] = 2147483647
        alist.pop(-1)
        self.assertEqual(model.take_in(op), [R(RT.OP, alist[-1])])

        op = "="
        self.assertEqual(model.take_in(op), [R(RT.DT, alist[-1])])

    def test_3_2(self):
        model = SRPN_Model()
        alist = []

        nr1 = -2147483647
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model.take_in(str(nr1)), [r1])

        nr2 = 1
        r2 = R(RT.IN, nr2)
        alist.append(nr2)
        self.assertEqual(model.take_in(str(nr2)), [r2])

        op = "-"
        alist[-2] -= alist[-1]
        alist.pop(-1)
        self.assertEqual(model.take_in(op), [R(RT.OP, alist[-1])])

        op = "="
        self.assertEqual(model.take_in(op), [R(RT.DT, alist[-1])])

        nr2 = 20
        r2 = R(RT.IN, nr2)
        alist.append(nr2)
        self.assertEqual(model.take_in(str(nr2)), [r2])

        op = "-"
        alist.pop(-1)
        self.assertEqual(model.take_in(op), [R(RT.OP, alist[-1])])

        op = "="
        self.assertEqual(model.take_in(op), [R(RT.DT, alist[-1])])

    def test_3_3(self):
        model = SRPN_Model()
        alist = []

        nr1 = 100000
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model.take_in(str(nr1)), [r1])

        nr2 = 0
        r2 = R(RT.IN, nr2)
        alist.append(nr2)
        self.assertEqual(model.take_in(str(nr2)), [r2])

        op = "-"
        alist[-2] -= alist[-1]
        alist.pop(-1)
        self.assertEqual(model.take_in(op), [R(RT.OP, alist[-1])])

        op = "d"
        self.assertEqual(model.take_in(op), [R(RT.DS, alist)])

        op = "-"
        self.assertEqual(model.take_in(op), [R(RT.ER, Error(ERROR.ST_UNDRF))])

        op = "="
        self.assertEqual(model.take_in(op), [R(RT.DT, alist[-1])])


class Test_Fourth_Section(unittest.TestCase):
    def test_4_1(self):
        """
        1
        +
        """
        model = SRPN_Model()
        alist = []

        nr1 = 1
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model.take_in(str(nr1)), [r1])

        op = "+"
        self.assertEqual(model.take_in(op), [R(RT.ER, Error(ERROR.ST_UNDRF))])

    def test_4_2(self):
        """
        10
        5
        -5
        +
        /
        """
        model = SRPN_Model()
        alist = []

        nr1 = 10
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model.take_in(str(nr1)), [r1])

        nr1 = 5
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model.take_in(str(nr1)), [r1])

        nr1 = -5
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model.take_in(str(nr1)), [r1])

        op = "+"
        alist[-2] += alist[-1]
        alist.pop(-1)
        self.assertEqual(model.take_in(op), [R(RT.OP, alist[-1])])

        op = "/"
        self.assertEqual(model.take_in(op), [R(RT.ER, Error(ERROR.DIV0))])

class TestPrintMethods(unittest.TestCase):

    def test_initial_message(self):
        view = SRPN_View()
        self.assertEqual(view.disp_wlcm(), "You can now start interacting with the SRPN calculator" )

if __name__ == '__main__':
    unittest.main()
