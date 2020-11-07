#!/usr/bin/env python3
# SRPN Controller
#
# Comment: I decided to go down the path of an MVC to be better abbl to test
# the code 

from classes.srpn_view  import SRPN_View
from classes.srpn_model import SRPN_Model
from classes.result     import Result
from classes.result     import Result_Type as RT

class SRPN_Controller:
    """
    SRPMN Controller is an itermediary between the user, the model and the 
    """

    view = SRPN_View()
    model = SRPN_Model()

    def __init__(self):
        self.model = SRPN_Model()
        print(self.view.disp_wlcm())
        while True :
            self.read_input()

    def read_input(self):
        """
        reads the user input and sends it to the model
        """
        rw_input = ""
        rw_input = input()
        result_list = self.model.take_in(rw_input)
        self.serve(result_list)
    
    def serve(self, result_list):
        """
        takes the list of results and based on the code sends to the view
        the data
        """
        for i in range(len(result_list)):
            print ("step {}data: {} code: {}".format(\
                    i,result_list[i].code,result_list[i].data)) #[DEBUG]

        for result in result_list:

            if result.code == RT.DT:    # single number
                print(self.view.disp_top(result))
                return 0

            elif result.code == RT.DS:  # list
                print(self.view.disp_stack(result))
                return 0

            elif result.code == RT.IN:  # insertion
                return 0

            elif result.code == RT.ER:  # error
                print(self.view.disp_error(result))
                return 0

            elif result.code == 5:  # opperation
                return 0

