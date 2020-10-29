.PHONY : run test debug

test:
	python3 test.py

optimised : 
	python3 -o main.py

run : 
	python3 main.py

debug:
	python3 -m pdb main.py
