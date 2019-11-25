
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def main():
	n = 600851475143
	div=2
	ans=0
	while n!=0:
		if n%div !=0:
			div=div+1
		else:
			maxfact=n
			n=n/div
			if n==1:
				print('The largest prime factor is {} '.format(maxfact))
				ans=1
				break


if __name__ == "__main__":
    # execute only if run as a script
    main()