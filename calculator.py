import re # Regex parser

class Calculator:
    # Reverse Polish Notation Calculator Class
    def __init__(self):
        #initialise the stack on the creation of a new calculator
        self.stack=[]

    def interface(self):
        val = input()           # read the input
        while val != '.exit':   # baked in exit mechanism for interface [REMOVE]
            self.read (val)
            val = input()
            print(self.stack)

    def read(self, rawInput):
        # read the input
        # if the input is a list split it

        if not rawInput.isnumeric():
            prcInput = rawInput.split()         # split the input 
        else:
            prcInput = rawInput

        if isinstance(prcInput, list):
            for val in prcInput:
                val = self.parse(val)
        else:
            self.parse(prcInput)
        return self.stack


    def parse(self,val):

        numberEx = re.compile('[0-9]+')
        signEx = re.compile('[+-/*%]+')

        print (val)
        numVal = numberEx.match(val)
        print (numVal)
        signVal = signEx.match(val)

        if numVal != None:
            self.stack.append(numVal.group())
            return
        elif signVal!= None:
            self.stack.append(signVal.group())
            return
        else:
            self.display_error(1)
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
