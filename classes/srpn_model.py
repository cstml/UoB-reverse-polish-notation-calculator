# SRPN Model Class

import re
from classes.result import Result
from classes.result import Result_Type as RT
from classes.error import Error_Type as ERROR
from classes.error import Error


class SRPN_Model:
    
    TP_CM = '='
    SD_CM = 'd'
    RA_CM = 'r'
    AD_CM = '+'
    MAX_UP = 2147483647
    MAX_DN = -2147483648
    
    stack = []
    result_list = []
    
    random_stack = []
    random_stack_it = 0

    def __init__ (self):
        self.random_stack_it = 0
        self.stack = []
        self.random_stack.append(1804289383)
        self.random_stack.append(846930886)
        self.random_stack.append(1681692777)
        self.random_stack.append(1714636915)
        self.random_stack.append(1957747793)
        self.random_stack.append(424238335)
        self.random_stack.append(719885386)
        self.random_stack.append(1649760492)
        self.random_stack.append(596516649)
        self.random_stack.append(1189641421)
        self.random_stack.append(1025202362)
        self.random_stack.append(1350490027)
        self.random_stack.append(783368690)
        self.random_stack.append(1102520059)
        self.random_stack.append(2044897763)
        self.random_stack.append(1967513926)
        self.random_stack.append(1365180540)
        self.random_stack.append(1540383426)
        self.random_stack.append(304089172)
        self.random_stack.append(1303455736)
        self.random_stack.append(35005211)
        self.random_stack.append(521595368)

    def stack_ok(self, op):
        """
        Defines operations on the stack that help other methods to take
        decisions
        """
        if op == 'Insert':
            if len(self.stack) < 26 :
                return True
            else:
                return False

        elif op == 'Operation' :
            if len(self.stack) <= 1 :
                return False
            else :
                return True

        elif op == 'Operation2' :
            if len(self.stack) < 1 :
                return False
            else :
                return True

        elif op == 'stack empty?':
            if len(self.stack) == 0:
                return True
            else:
                return False

    def operation_ok(self, op, div = ""):
        if op == "/" and div == "":
            if self.stack[-1] == 0:
                return False
            else:
                return True

        if op == "/" :
            if self.stack[-1] == 0:
                return False
            else:
                return True

        else:
            return True


    def process_rp_r(self, string):
        """ Introduces spaces between r's and d's based on what is surrounding
        them 
        """

        for i in range(10): # [TO DO] the regex sometimes skips some good cases
                            # to revisit whe I have time
            string = re.sub(r'([0-9])(r)',r'\1 \2',string)
            string = re.sub(r'(r)(r)',r'\1 \2',string)
            string = re.sub(r'(d)(r)',r'\1 \2',string)

            string = re.sub(r'(r)([0-9])',r'\1 \2',string)
            string = re.sub(r'(r)(d)',r'\1 \2',string)

            string = re.sub(r'([0-9])(d)',r'\1 \2',string)
            string = re.sub(r'(d)([0-9])',r'\1 \2',string)

            string = re.sub(r'(d)',r' \1 ',string)
            string = re.sub(r'\s+(d)\s+',r' \1 ',string)
            string = re.sub(r'\s+(d)\s+$',r' \1',string)
            string = re.sub(r'^\s+(d)\s+',r'\1 ',string)
            string = re.sub(r'^\s+(d)\s+$',r'\1',string)


        return string

    def replace_r(self, string):
        """ replace r with randon number from queue
        """
        while re.findall(r'(r)',string):
            string = re.sub(r'r', str(self.random_stack[self.random_stack_it]),\
                        string,\
                        1)
            self.random_stack_it += 1
            if self.random_stack_it == len(self.random_stack):
                self.random_stack = 0
        return string
    
    def process_sp_math_ops(self, string):
        """Split mathematical strings
        """
        rgx_eqs  = r'([-+*/%^]?[-]?[1-9][0-9]*([-+*/%^][-]?[1-9][0-9]*)+)'
        rgx_eqs_r = r' \1 '
        string = re.sub(rgx_eqs, rgx_eqs_r, string)
        return string

    def process_sp_double_signs(self,strig):
        """ Split signs which are not math expr
        """

    def octal_to_decimal(self,string):
        """ Octal conversion
        """
        if string[0] == '-':
            sign = -1
            string = string[1:]
        else:
            sign = 1

        octal = int(string)
        octal = str(octal)
        power = 0
        noctal = 0 
        for i in octal[::-1]:
            dig = int(i)
            noctal += dig * pow(8,power)
            power += 1
        return str(noctal*sign)

    def octal_transform(self,string):
        """transforms all the octal numbers in the string into integer numbers"
        """
        octa_rx = r'(((?<=[+/%*^])|(?<=\s)|(?<=^))[-]?0+[1-9][0-9]*)'
        while re.search(octa_rx,string):
            inst = next(re.finditer(octa_rx,string))
            start = inst.start()
            end = inst.end()
            number = inst.group()
            conversion = self.octal_to_decimal(number)
            string=string[:start] + conversion + string[end:]
        return string


    def process(self, rw_data):
        """ Split the string into substrings based on spaces 
        """
        rw_data = str(rw_data) # be sure it is a string
        rw_data = self.process_rp_r(rw_data)
        rw_data = self.replace_r(rw_data)
        rw_data = self.process_sp_math_ops(rw_data)
        rw_data = self.octal_transform(rw_data)
        data =  rw_data.split() # split it 
        return data

    def operation2(self, op, element):
        """ similar to normal operation but it happens when we have a sign
        before the number
        """
        op_dict = { "+" : (lambda x, y : x + y),\
                    "-" : (lambda x, y : x - y),\
                    "/" : (lambda x, y : x // y),\
                    "%" : (lambda x, y : x % y),\
                    "*" : (lambda x, y : x * y),\
                    "^" : (lambda x, y : pow(x,y))}

        if self.stack_ok("Operation2"):
            if self.operation_ok(op, element):
                self.stack[-1] = self.saturate(op_dict[op](\
                                                    self.stack[-1],\
                                                    element))

            elif op == "/":
                return Result(RT.ER, Error(ERROR.DIV0))

            return Result(RT.OP, self.stack[-1])

        elif self.stack_ok("stack empty?"):
            return Result(RT.ER, Error(ERROR.ST_UNDRF,2))

        else:
            return Result(RT.ER, Error(ERROR.ST_UNDRF))

    def operation(self, op):
        op_dict = { "+" : (lambda x, y : x + y),\
                    "-" : (lambda x, y : x - y),\
                    "/" : (lambda x, y : x // y),\
                    "%" : (lambda x, y : x % y),\
                    "*" : (lambda x, y : x * y),\
                    "^" : (lambda x, y : pow(x,y))}

        if self.stack_ok("Operation"):
            if self.operation_ok(op):
                self.stack[-2] = self.saturate(op_dict[op](\
                                                    self.stack[-2],\
                                                    self.stack[-1]))
                self.stack.pop(-1)

            elif op == "/":
                return Result(RT.ER, Error(ERROR.DIV0))


            return Result(RT.OP, self.stack[-1])

        else:
            return Result(RT.ER, Error(ERROR.ST_UNDRF))



    def action(self, action):
        """
        Defines the return for for 
        """
        if self.stack_ok("stack empty?"):
            actions = { "d" : Result(RT.DT, -2147483648),\
                    "=" : Result(RT.ER, Error(ERROR.ST_EMPTY))}
        else:
            actions = { "d" : Result(RT.DS, self.stack),\
                    "=" : Result(RT.DT, self.stack[-1])}
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
        expr = '^[-]?[0-9]+$'
        return self.reg_match(data,expr)

    def is_op(self,data):
        """
        returns True if element is an opperation
        """
        expr = '^[-+/%^*]$'
        return self.reg_match(data,expr)

    def is_action(self,data):
        """ verifies if element is action
        """
        expr = '[d=]'
        return self.reg_match(data,expr)

    def is_eval(self, data):
        """ checks if the element is a simple mathematical evaluation
        """
        expr  = '^([-]?[1-9][0-9]*([-+*/%^][-]?[1-9][0-9]*)+)'
        return self.reg_match(data,expr)

    def is_special_eval(self, data):
        """ checks if the element is a simple mathematical evaluation
        """
        expr  = '^([+*/%^]?[-]?[1-9][0-9]*([-+*/%^][-]?[1-9][0-9]*)*)'
        return self.reg_match(data,expr)

    def evaluate(self, data):
        """ transforms a simple mathematical evaluation into an insertable
        number
        """
        data = eval(data)
        result = self.insert_data(data)
        return(result)

    def sp_eval(self, data):
        """ executes a simple mathematical evaluation unto the top of the stack
        """
        op = data[0]
        data = eval(data[1:])
        result = self.operation2(op,data)
        return(result)

    def saturate(self, number):
        """ saturates the number either up or down
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
        """ inserts data into the stack and returns a Result containing the
        last number inserted and code 2
        """
        if self.stack_ok("Insert"):
            data = self.saturate(data)
            self.stack.append(data)
            return Result(RT.IN,data)

        else: # stack overflow
            return Result(RT.ER,Error(ERROR.ST_UNDRF))

    def create_list(self, element):
        try:
                if self.is_number(element): # check if it is a number
                    # print("is number")
                    element = int(element)
                    result = self.insert_data(element)
                    self.prepare_response(result)

                elif self.is_op(element):   # check if it is an operation
                    self.prepare_response(self.operation(element))

                elif self.is_action(element): # check if it is an action
                    #print("is action")
                    self.prepare_response(self.action(element))

                elif self.is_eval(element): # check if it is a simple evaluation
                    #print("is eval")
                    self.prepare_response(self.evaluate(element))

                elif self.is_special_eval(element): 
                    response = self.sp_eval(element)
                    self.prepare_response(response)
                    if response.code == RT.ER and \
                            response.data == Error(ERROR.ST_UNDRF,2):
                        self.prepare_response(self.evaluate(element[1:]))

                else:
                    for letter in element:
                        self.prepare_response(\
                                Result(RT.ER, Error(ERROR.UNRECOGN, letter)))

        except Exception as e:
            print(e)

    def take_in(self, rw_data):
        """
        takes in the data from the controller
        sends it to be processed 
        reads through each element of the processed_data
        creates the list of results
        """
        self.init_result_list()
        processed_data = self.process(rw_data)
        if isinstance(processed_data,list):
            for element in processed_data:
                self.create_list(element)
        else: 
            element = processed_data
            self.create_list(element)
        return self.result_list

        

    

