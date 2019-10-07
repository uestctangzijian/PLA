About how to run：
1) open CMD.

2) cd to the content which py files in.
	cd C:\Users\T5\PycharmProjects\PLA	
	
3) run DataEmit program.
	python DataEmit.py [0,-1,1] 5 4 
	
	if no error occur, mean successful.
	then you can open 'train.txt' to see the result.
	The output file may look like the following:
	-67.9 95.1 1.0
	-86.0 62.3 1.0
	60.0 66.2 1.0
	35.1 28.1 -1.0
	82.5 -59.0 -1.0
	-65.8 91.2 1.0
	-96.8 55.9 1.0
	0.6 -70.3 -1.0
	80.1 -49.6 -1.0
	PS: -1 mean '-', +1 mean '+'.
	
4) run PLA program
	python PLA.py train.txt
	then pop-up a window that display the plot,
	after close the window, the CMD will output the weight vector. eg.[[  -3.  -108.7  135.1]]
	
About environment:
	python version: python 3.6
	IDE: pycharm 2018.3.3
	OS: win10
	packages used: numpy, matplotlib, sys

	
	