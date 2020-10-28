.PHONY : run test debug

test:
	python3 test.py

run : 
	python3 main.py

debug:
	python3 -m pdb main.py
