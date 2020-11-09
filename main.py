#!/usr/bin/env python3

# Welcome to the reverse Polish Notation Calculator
# The calculator was designed on a modular Model-View-Controller structure
# to enable fast prototyping and testing of the modules

# This also allows for each module of the calculator to be able to be 
# developed in a sepparate manner - thus the view module could be changed
# tested and refactored without altering the calculator's model methods 
# In the same manner the model could be transported to a different program


from srpn_controller import SRPN_Controller

if __name__=="__main__":
    calculator = SRPN_Controller()
