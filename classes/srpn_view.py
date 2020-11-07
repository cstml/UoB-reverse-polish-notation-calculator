# Main VIEW

import Result from result

class SRPN_View:

    def disp_error(self, result):
        """
        A tidy way to handle errors 
        """
        if result.code == 0:
            return("Stack empty.")

        elif result.code == 1:
            return("Stack overflow.")

        elif result.code == 2:
            return("Stack underflow.")
    
        elif result.code == 3:
            return('Unrecognised operator or operand "{}".'.format(\
                    result.data))

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
