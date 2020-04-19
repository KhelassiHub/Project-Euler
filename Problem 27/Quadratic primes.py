# Euler discovered the remarkable quadratic formula:
# n²+n+41

# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
# . However, when n=40,40²+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41²+41+41

# is clearly divisible by 41.

# The incredible formula n²−79n+1601
# was discovered, which produces 80 primes for the consecutive values 0≤n≤79
# . The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:
#     n²+an+b

# , where |a|<1000 and |b|≤1000

# where |n|
# is the modulus/absolute value of n
# e.g. |11|=11 and |−4|=4

# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number 
# of primes for consecutive values of n, starting with n=0.
from tqdm import tqdm

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
	coefficients=(0,0)
	longestSequence=0
	for a in tqdm(range(-999,1000)):
		for b in range(-1000,1001):
			n=0
			formula=n*n+a*n+b
			while isPrime(formula)==True:
				n=n+1
				formula=n*n+a*n+b
			if longestSequence<=n:
				longestSequence=n
				coefficients=(a,b)
	print(coefficients,longestSequence,coefficients[0]*coefficients[1])
			
if __name__ == '__main__':
	main()