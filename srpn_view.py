# Main VIEW


class SRPN_View:

    def disp_error(self, code):
        """
        A tidy way to handle errors 
        """
        if code == 0:
            return("Stack empty.")

        elif code == 1:
            return("Stack overflow.")

        elif code == 2:
            return("Stack underflow.")
    

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
