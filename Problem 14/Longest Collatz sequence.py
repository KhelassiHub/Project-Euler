"""
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting is finish at 1.
Which starting i, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from tqdm import tqdm

def main():
	indice=1
	for number in tqdm(range(1,1000000)):
		index=1
		i=number
		while True:
			if i%2==0:
				i=i/2
				index+=1
			elif i%2==1:
				i=i*3+1
				index+=1
			if i==1:
				break
		if indice < index:
			indice = index
			x=number
	print('Number {} chain length {}'.format(x,indice))
	
if __name__ == '__main__':
	main()