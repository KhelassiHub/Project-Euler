
# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def main():
	number=100
	result=1
	for i in range(1,number+1):
		result*=i
	resultStr=str(result)
	answer=0
	for index in range(len(resultStr)):
		answer+=int(resultStr[index])
	print(f'the sum of the digits in the number 100! is {answer}')

if __name__ == '__main__':
	main()