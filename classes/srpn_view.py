# Main VIEW

from classes.result import Result 

class SRPN_View:

    def disp_error(self, result):
        """
        A tidy way to handle errors 
        """
        if result.data.e_type == 0:
            return("Stack empty.")

        elif result.data.e_type == 1:
            return("Stack overflow.")

        elif result.data.e_type == 2:
            return("Stack underflow.")
    
        elif result.data.e_type == 3:
            return('Unrecognised operator or operand "{}".'.format(reslt.data.e_message))

    def disp_wlcm(self):
        welcome_message = "You can now start interacting with the SRPN calculator"
        return (welcome_message)


    def disp_top(self, top):
        """
        Get the last element if there is one
        If the stack is under display the error code
        """
        return top

    def disp_stack(self,stack):
        """
        Create a String of the numbers to be displayed
        """
        out_string = ""
        for number in stack:
            out_string += number.to_string() + " "
        return out_string
