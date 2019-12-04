
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isPrime(n) : 
    # Special cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6			# all primes are of the form 6k ± 1
    return True

def main():
	x=2		# start from the number 2
	i=0		# indice of the prime number
	while x!=0:
		if isPrime(x)==True:
			i=i+1
		if i==10001:
			print("the 10001 prime number is {}".format(x))
			break
		x=x+1

if __name__ == "__main__":
    # execute only if run as a script
    main() 
