# SRPN Controller
# Author: Vlad P. Luchian

from srpn_view  import SRPN_View
from srpn_model import SRPN_Model
from result     import Result

class SRPN_Controller:
    """
    SRPMN Controller is an itermediary between the user, the model and the 
    """

    model = SRPN_Model()

    def __init__(self):
        view = SRPN_View()
        self.model = SRPN_Model()
        print(view.disp_wlcm())
        while True :
            self.read_input()

    def read_input(self):
        """
        reads the user input and sends it to be processed 
        """
        rw_input = ""
        rw_input = input()
        self.proc_input(rw_input)
    
    def proc_input(self, rw_input):
        """
        processes the user input and either 
        chunks it down or simply sends it to the model
        the received result is then passed to a serve function
        """
        if isinstance(rw_input,str):
            rw_input.replace('d',' d ')
            rw_input.replace('r',' r ')
            pr_input = rw_input.split()

        if isinstance(pr_input, list): # if it is a list of input
            for chunk in pr_input:
                result = self.model.take_in(chunk)
                self.serve(result)
        else:
            result = self.model.take_in(eval(pr_input))
            self.serve(result)
        return 0
    
    def serve(self, result):
        """
        takes the result and based on the code prints what the view function 
        tells it  to print 
        """
        view = SRPN_View()

        print ("data: {} code: {}".format(result.data, result.code))

        if result.code == 0:    # single number
            print(view.disp_top(result.data))
            return 0

        elif result.code == 1:  # list
            print(view.disp_stack(result.data))
            return 0

        elif result.code == 2:  # number added no problemo
            return 0

        elif result.code == 3:  # error
            print(view.disp_error(result.data))
            return 0

        elif result.code == 5:  # addition
            print("Number Added")
            return 0
