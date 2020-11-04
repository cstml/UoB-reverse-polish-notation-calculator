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
        signEx = re.compile('[=+-/*%]+')
        leterEx = re.compile('d')

        numVal = numberEx.match(val)
        signVal = signEx.match(val)
        leterVal = leterEx.match(val)
        
        if numVal != None:
            val=numVal.group()
            self.stack.append(int(val))
            return

        elif signVal!= None:
            for sign in signVal.group():
                print(sign)
                if self.check_Size() == True:
                    if sign == "+":
                        self.add()
                    elif sign == "-":
                        self.subtract()
                    elif sign == "*":
                        self.multiply()
                    elif sign == "/":
                        self.divide()

                elif sign == "=":
                    self.print_Last()

                else:
                    self.display_error(2)

        elif leterVal!= None:
            for leter in leterVal.group():
                if leter == "d":
                    for num in self.stack:
                        print(num)

        else:
            self.display_error(1)
            return

    def print_Last(self):
        print(self.stack[-1])

    def display_error(self,error_code):
        if error_code == 1 :
            print ("Wrong input error text")

        if error_code == 2 :
            print ("Stack underflow")
    
    def check_Size(self):
        if len(self.stack)>1:
            return True
        else:
            return False
        
    def add(self):
        if self.check_Size():
            self.stack[-2] = self.stack[-1] + self.stack[-2]
            self.stack.pop(-1);
            print (self.stack)

    def subtract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        return a/b

    def modulo(self,a,b):
        return a%b
