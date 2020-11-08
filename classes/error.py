#!/usr/bin/env python3

# An error carrier helper class 
# It is created by the model class and passed by the controller to the view 
# which then uses its attached information to create its view

from enum import Enum

class Error_Type(Enum):
    DEFAULTV = -1 # Default Value
    ST_EMPTY = 0
    ST_OVRFL = 1  # Stack Overflow
    ST_UNDRF = 2  # Stack Underflow
    UNRECOGN = 3  # Unrecognised Op 

class Error:
    e_type = Error_Type.DEFAULTV
    e_message = ""

    def __init__ (self, t, m=0):
        self.e_type = t
        self.e_message = m

    def __eq__(self, other):
        if not isinstance(other, Error):
            return NotImplemented
        return self.e_type == other.e_type\
                and self.e_message == other.e_message

    def __repr__(self):
        repr_string = "Error(Type: {}, Message: {})".format(\
                self.e_type, self.e_message)
        return repr_string
