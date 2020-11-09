#!/usr/bin/env python3

# SRPN Calculator 
# view module

from classes.result import Result 
from classes.error import Error_Type as ER

class SRPN_View:

    def disp_error(self, result):
        """
        An Error handler. Unpacks the result and returns the 
        needed display for the controller to show the user
        """
        if result.data.e_type == ER.ST_EMPTY:
            return("Stack empty.")

        elif result.data.e_type == ER.ST_OVRFL:
            return("Stack overflow.")

        elif result.data.e_type == ER.ST_UNDRF:
            return("Stack underflow.")
    
        elif result.data.e_type == ER.UNRECOGN:
            return('Unrecognised operator or operand "{}".'\
                    .format(result.data.e_message))

        elif result.data.e_type == ER.DIV0:
            return("Divide by 0.")

    def disp_wlcm(self):
        """
        Returns the message the calculator displays at instantiation
        """
        welcome_message = "You can now start interacting with the SRPN calculator"
        return (welcome_message)


    def disp_top(self, result):
        """
        Get the last element if there is one
        If the stack is under display the error code
        """
        return result.data

    def disp_stack(self, result):
        """
        Create a String of the numbers to be displayed
        """
        out_string = ""
        for number in result.data:
            out_string += str(number) + "\n"
        out_string = out_string[:-1]
        return out_string
