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

        op = "d"
        self.assertEqual(model.take_in(op), [R(RT.DS, alist)])

class Test_Fifth_Section(unittest.TestCase):
    def test_5_1(self):
        model = SRPN_Model()
        self.assertEqual(model.process_sp_math_ops("11+1+1+d"), " 11+1+1 +d")
        self.assertEqual(model.process_sp_math_ops("-11+1+1+d"), " -11+1+1 +d")
        self.assertEqual(model.process_sp_math_ops("+-11+1+1+d"), " +-11+1+1 +d")


    def test_5_2(self):
        model = SRPN_Model()
        self.assertEqual(model.process_rp_r("9r"), "9 r")
        self.assertEqual(model.process_rp_r("9rr"), "9 r r")
        self.assertEqual(model.process_rp_r("9rr"), "9 r r")
        self.assertEqual(model.process_rp_r("9rd"), "9 r d")
        self.assertEqual(model.process_rp_r("9rr9"), "9 r r 9")
        self.assertEqual(model.process_rp_r("rrrr"), "r r r r")
        self.assertEqual(model.process_rp_r("+rr9"), "+r r 9")

    def test_5_3(self):
        model = SRPN_Model()
        self.assertEqual(model.replace_r("9 r"), "9 1804289383")

    def test_5_5_test_randoms(self):
        model = SRPN_Model()
        self.assertEqual(model.replace_r("r r r"), "1804289383 846930886 1681692777")

    def test_5_5_test_all_randoms(self):
        model = SRPN_Model()
        self.assertEqual(model.replace_r("r r r"),"1804289383 846930886 1681692777")
        self.assertEqual(model.replace_r("r r r"),"1714636915 1957747793 424238335")
        self.assertEqual(model.replace_r("r r r"),"719885386 1649760492 596516649")
        self.assertEqual(model.replace_r("r r r"),"1189641421 1025202362 1350490027")
        self.assertEqual(model.replace_r("r r r"),"783368690 1102520059 2044897763")
        self.assertEqual(model.replace_r("r r r"),"1967513926 1365180540 1540383426")
        self.assertEqual(model.replace_r("r r r"),"304089172 1303455736 35005211")
        self.assertEqual(model.replace_r("r r r"),"521595368 1804289383 846930886")

    def test_5_3_test_processing(self):
        model = SRPN_Model()
        self.assertEqual(model.process("rrr"),["1804289383",\
                                                "846930886",\
                                                "1681692777"])

class Test_Sixth_Section(unittest.TestCase):
    def test_octal_function(self):
        model = SRPN_Model()
        self.assertEqual(model.octal_transform("020"),"16")
        self.assertEqual(model.octal_transform("-020"),"-16")
        self.assertEqual(model.octal_transform("+-00000020"),"+-16")

class Test_Seventh_Section(unittest.TestCase):
    """
    evaluate if the power is working accordingly
    """
    def test_4_2(self): 
        """
        1
        2
        ^
        =
        """
        model = SRPN_Model()
        alist = []

        nr1 = 1
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model.take_in(str(nr1)), [r1])

        nr1 = 2
        r1 = R(RT.IN, nr1)
        alist.append(nr1)
        self.assertEqual(model.take_in(str(nr1)), [r1])

        op = "^"
        alist[-2] = pow(alist[-2] ,alist[-1])
        alist.pop(-1)
        self.assertEqual(model.take_in(op), [R(RT.OP, alist[-1])])

        op = "="
        self.assertEqual(model.take_in(op), [R(RT.DT, alist[-1])])

        op = "d"
        self.assertEqual(model.take_in(op), [R(RT.DS, alist)])

class TestPrintMethods(unittest.TestCase):

    def test_initial_message(self):
        view = SRPN_View()
        self.assertEqual(view.disp_wlcm(), "You can now start interacting with the SRPN calculator" )

if __name__ == '__main__':
    unittest.main()
