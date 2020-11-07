# SRPN Model Class

import re
from classes.result import Result

class Error:
    e_type = ""
    e_message = ""

    def __init__ (sef,t,m=0):
        self.e_type = t
        self.e_message = m

class SRPN_Model:
    
    TP_CM = '='
    SD_CM = 'd'
    RA_CM = 'r'
    AD_CM = '+'
    MAX_UP = 2147483647
    MAX_DN = -2147483648
    
    stack = []
    result_list = []
    
    random_stack = [1804289383,\
                    846930886,\
                    1681692777,\
                    1714636915,\
                    1957747793,\
                    424238335,\
                    719885386,\
                    1649760492,\
                    596516649,\
                    1189641421,\
                    1025202362,\
                    1350490027,\
                    783368690,\
                    1102520059,\
                    2044897763,\
                    1967513926,\
                    1365180540,\
                    1540383426,\
                    304089172,\
                    1303455736,\
                    35005211,\
                    521595368]
    random_stack_it = 0

    def __init__ (self):
        self.random_stack_it=0;

    def stack_ok(self,op):
        if op == 'Insert':
            if len(self.stack) < 26 :
                return True
            else:
                return False

        if op == 'Operation' :
            if len(self.stack) <= 1 :
                return False
            else :
                return True

    def operation(self,op):
        op_dict = { "+" : (lambda x, y : x + y),\
                    "-" : (lambda x, y : x - y),\
                    "/" : (lambda x, y : x / y),\
                    "%" : (lambda x, y : x % y),\
                    "*" : (lambda x, y : x * y),\
                    "^" : (lambda x, y : pow(x,y))}

        if self.stack_ok("Operation"):
            self.stack[-2] = self.saturate(op_dict[op](\
                                                self.stack[-1],\
                                                self.stack[-2]))
            pop_el = self.stack[-1]
            self.stack.pop(-1)
            return Result(5,pop_el)
        else:
            return Result(3,Error(2))

    def process(self, rw_data):
        """
        Split the string into substrings
        """
        data =  rw_data.split()
        return data

    def action(self, action):
        actions = { "d" : Result(1,self.stack),\
                    "=" : Result(0,self.stack[-1])}
        return actions[action]

    def init_result_list(self):
        """
        Initialise the result list
        """
        self.result_list = []       # initialise the list of results 
        return 0

    def prepare_response(self, result):
        """
        Appends each result to the list
        """
        self.result_list.append(result)
        return 0

    def reg_match(self,data,expr):
        number_rx = re.compile(expr)
        if number_rx.match(data) != None:
            return True
        else:
            return False

    def is_number(self, data):
        """
        returns True if element is a number
        and false if it is anything else
        """
        expr = '[-]?[0-9]+'
        return self.reg_match(data,expr)

    def is_op(self,data):
        """
        returns True if element is an opperation
        """
        expr = '[-+/%^*]'
        return self.reg_match(data,expr)

    def is_action(self,data):
        """
        verifies if element is action
        """
        expr = '[d=]'
        return self.reg_match(data,expr)

    def take_in(self, rw_data):
        """
        takes in the data from the controller
        sends it to be processed 
        reads through each element of the processed_data
        creates the list of results
        """
        self.init_result_list()
        processed_data = self.process(rw_data)
        print(processed_data)
        try:
            for element in processed_data:
                if self.is_number(element): # check if it is a number
                    element = int(element)
                    result = self.insert_data(element)
                    self.prepare_response(result)

                elif self.is_op(element):   # check if it is an operation
                    self.prepare_response(self.operation(element))

                elif self.is_action(element): # check if it is an action
                    print("is action")
                    self.prepare_response(self.action(element))

                else:
                    self.prepare_response(\
                            Result(\
                                3, Error(3,element)))

        except Exception as e:
            print(e)

        finally:
            return self.result_list

    def saturate(self, number):
        """
        saturates the number either up or down
        based on the maximum number
        if the number is within the range it is returned
        """
        if number > self.MAX_UP:
            return self.MAX_UP
        elif number < self.MAX_DN:
            return self.MAX_DN
        else:
            return number

    def insert_data(self, data):
        """
        inserts data into the stack and 
        returns a Result containing 
        the last number inserted and code 2
        """
        if self.stack_ok("Insert"):
            data = self.saturate(data)
            self.stack.append(data)
            return Result(2,data)

        else: # stack overflow
            return Result(3,1)
        

    

