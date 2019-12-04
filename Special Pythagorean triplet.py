
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt
def main():
	for i in range(1,500):
		l=i*i 				# just to optimize the time
		for x in range(i+1,500):
			y= sqrt(l+x*x)
			result=i+x+y
			if result==1000 and i<x:
				print("{}+{}+{}=1000 their product is {}".format(i,x,y,i*x*y))
				break
if __name__== "__main__":
    # execute only if run as a script
	main() 
