#!/usr/bin/sh

.PHONY : run test debug 

run : 
	python3 main.py

test:
	python3 test.py

debug:
	python3 -m pdb main.py
