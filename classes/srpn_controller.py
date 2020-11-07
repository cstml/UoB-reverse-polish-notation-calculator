# SRPN Controller
# Author: Vlad P. Luchian
#
# Comment: I decided to go down the path of an MVC to be better abbl to test
# the code 

from srpn_view  import SRPN_View
from srpn_model import SRPN_Model
from result     import Result

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

            if result.code == 0:    # single number
                print(self.view.disp_top(result.data))
                return 0

            elif result.code == 1:  # list
                print(self.view.disp_stack(result.data))
                return 0

            elif result.code == 2:  # insertion
                return 0

            elif result.code == 3:  # error
                print(self.view.disp_error(result))
                return 0

            elif result.code == 5:  # opperation
                return 0

