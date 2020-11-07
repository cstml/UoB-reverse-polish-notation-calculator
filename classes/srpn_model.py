# SRPN Model Class

import re

from result import Result

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
        if op == 'Add' :
            if len(self.stack) <= 1 :
                return False
            else :
                return True

    def addition(self):
        if self.stack_ok("Add"):
            self.stack[-2]+=self.stack[-1]
            self.stack[-2] = self.saturate(self.stack[-2])
            pop_el = self.stack[-1]
            self.stack.pop(-1)
            return Result(5,pop_el)
        else:
            return Result(3,2)

    def process(self, rw_data):
        """
        Process the data and split it 
        """
        data =  rw_data.split()
        return data


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
                if element.isnumeric():
                    if self.stack_ok('Insert'):
                        element = int(element)
                        result = self.insert_data(element)
                        self.prepare_response(result)

                    else: # stack overflow
                        result = Result(3,1)
                        self.prepare_response(result)

                elif data == "+":
                    result = self.addition()
                    self.prepare_response(result)

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

        data = self.saturate(data)
        self.stack.append(data)
        result = Result(2,data)
        return result

        

    

