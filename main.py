#!/usr/bin/env python3

# Welcome to the reverse Polish Notation Calculator
# The calculator was designed on a modular Model-View-Controller structure
# to enable fast prototyping and testing of the modules


from classes.srpn_controller import SRPN_Controller

if __name__=="__main__":
    calculator = SRPN_Controller()
