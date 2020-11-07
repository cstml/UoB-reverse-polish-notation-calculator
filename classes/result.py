#!/usr/bin/env python3
from enum import Enum

class Result_Type(Enum):
    DF = -1 # Default Value
    DT = 0  # Display Top
    DS = 1  # Display Stack
    IN = 2  # Insertion Succesfull
    ER = 3
    OP = 5

class Result:
    code = Result_Type.DF
    data = -1

    def __init__ (self, code, data):
        self.code = code
        self.data = data

    def __eq__(self, other):
        if not isinstance(other, Result):
            return NotImplemented
        return self.code == other.code and self.data == other.data

    def __repr__(self):
        repr_string = "Result(code: {}, data: {})".format(\
                self.code,self.data)
        return repr_string

