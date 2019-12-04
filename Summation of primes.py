
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def isPrime(n) : 
    # Special cases 
    if (n <= 1) : 
        return False
    elif (n <= 3) : 
        return True  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    elif (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6			# all primes are of the form 6k ± 1
    return True

def main():
	somme=0
	for x in range(1,2000000):
		if isPrime(x)==True:
			somme+=x
	print("The sum is equal to {}".format(somme))
if __name__ == "__main__":
	main()
