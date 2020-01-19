"""
	2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
	What is the sum of the digits of the number 2^1000?
"""

def main():
	number=eval(input("Pls introduce the number followed by it's power\n"))
	power=eval(input())		# input produce a string and eval converts that string to a number
	result=pow(number,power)
	stringResult=str(result)
	sumOfTheDigits=0  # initialization
	for caratere in range(len(stringResult)):
		sumOfTheDigits+=int(stringResult[caratere])
	print(f'The sum of the digits if the number are {sumOfTheDigits}')

if __name__ == '__main__':
	main()