class Result:
    code = -1
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
