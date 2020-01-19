
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def primeFact(number):			#returns a list that contains the prime factors of the given number
	primeListe=list()
	while number!= 0 :
		if number%2 == 0:
			number = number/2
			primeListe.append(2)
		elif number%3 == 0:
			number = number/3
			primeListe.append(3)
		elif number%5 == 0:
			number = number/5
			primeListe.append(5)
		elif number%7 == 0:
			number = number/7
			primeListe.append(7)
		elif number%11 == 0:
			number = number/11
			primeListe.append(11)
		elif number%13 == 0:
			number = number/13
			primeListe.append(13)
		elif number%17 == 0:
			number = number/17
			primeListe.append(17)
		elif number%19 == 0:
			number = number/19
			primeListe.append(19)
		else:
			break	
	return primeListe

def main():
	dividers=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	number_PrimeFactors=dict()				#dictionnary that contains the number with it's list of prime factors
	primeListe=[2,3,5,7,11,13,17,19]
	occurenceTimes=[]					#list that contains the number of occurences of the prime factor
	for x in dividers:
		number_PrimeFactors[x]=primeFact(x)
		for occurence in primeListe:
			occurenceTimes.append(number_PrimeFactors[x].count(occurence))
	result=1
	n=0
	for premierTerme in range(0,8):
		result=result*pow(primeListe[n],max(occurenceTimes[premierTerme::8]))
		n+=1
	print('The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}'.format(result))
	
if __name__ == "__main__":
    # execute only if run as a script
    main() 


#	2 = 2
#	3 = 3
#	4 = 2*2
#	5 = 5
#	6 = 2*3
#	7 = 7
#	8 = 2*2*2
#	9 = 3*3
#	10 = 2*5
#	2^(occurence of two)*3^(occurence of three)*5^(occurence of five)*7^(occurence of seven)
#		2*2*2*2*3*3*5*7	= 2520
