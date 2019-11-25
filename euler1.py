
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def main():
	a=0
	for x in range(3,1000):
		if x%3==0 or x%5==0:
			a = a + x
	print('la somme est {}'.format(a))

if __name__ == "__main__":
    # execute only if run as a script
    main()