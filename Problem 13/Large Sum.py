
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import numpy as np


def main():
	with open('number.txt','r') as f:
		vector=np.array([[f.readline().strip()]])		
		for line in f:
			vector=np.append(vector,[[line.strip()]],axis=0)
	# print(vector)
	theSum=0
	for i in range(0,100):
		theSum += int(vector[i][0])
	print('{:.10}'.format(str(theSum)))
	

	# vector=np.loadtxt("number.txt",dtype=flo)

if __name__ == '__main__':
	main()