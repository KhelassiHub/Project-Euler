
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers 
# and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.

def sumOfTheSquares(a,b):
	result=0
	for i in range(a,b):
		result += pow(i,2)
	return result
def SquaresOfTheSum(c,d):
	result=0
	for x in range(c,d):
		result += x
	return pow(result,2)

def main():
	diff = SquaresOfTheSum(1,101) - sumOfTheSquares(1,101)
	print ("the difference between the sum of the squares and the SquaresOfTheSum is {}".format(diff))

if __name__ == "__main__":
    # execute only if run as a script
    main()