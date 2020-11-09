#!/usr/bin/env python3

from enum import Enum

class Result_Type(Enum):
    """
    Enum holding the types of Results that the operations in the model can have
    helps the controller recognise what to do with the information it receives 
    """
    DF = -1 # Default Value
    DT = 0  # Display Top
    DS = 1  # Display Stack
    IN = 2  # Insertion Succesfull
    ER = 3  # Error 
    OP = 5  # Operation
    DO_NOTHING = 6 # does nothing - for testing comments commenter

class Result:
    """
    The main vehicle of communication wthin the SRPN calculator. It is formed 
    of:
        - code : Result_Type    lets the controller what type of information it 
                                is receiving
        - data : any            is a carrier of data. Depending on the 
                                Result_Type this can be a string, a list or 
                                an Error
    """
    code = Result_Type.DF
    data = -1

    def __init__ (self, code = Result_Type.DF, data = 0):
        """
        initialiser of response
        by default the values are initialised with:
            
            code = Result_Type.DF, 
            data = 0
        """
        self.code = code
        self.data = data

    def __eq__(self, other):
        """
        defines a methhod for the default equality comparisson
        and is used in the unit testing to compare the expected results to
        the ones received
        """
        if not isinstance(other, Result):
            return NotImplemented
        return self.code == other.code and self.data == other.data

    def __repr__(self):
        """
        The standard representation of the Result is
            Result(code: self.code, data: self.data)
        """
        repr_string = "Result(code: {}, data: {})".format(\
                self.code,self.data)
        return repr_string
