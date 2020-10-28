import re

class Calculator:
    def __init__(self):
        self.stack=[]

    def interface(self):
        val = input()
        self.read (val)

    def read(self, val):
        val = self.parse(val)
        if val != None:
            self.stack.append(val)
        else:
            self.display_error(1)
        return self.stack


    def parse(self,val):
        parse = re.compile('([0-9]+)')
        val = parse.match(val)
        if val != None:
            return val.group()
        return

    def display_error(self,error_code):
        if error_code == 1 :
            print ("Wrong input error text")

    def add(a,b):
        return a+b

    def subtract(a,b):
        return a-b

    def multiply(a,b):
        return a*b

if __name__=="__main__":
    calculator = Calculator()
    calculator.interface()
        
