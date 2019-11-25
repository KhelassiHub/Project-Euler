
#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def god_s_will():
	max = 0
	for a in range(1,999):
		for b in range(1,999):
			result = a*b
			result_str = str(result)
			if result_str == result_str[::-1] :
				print(f"palindrome : {result_str}")
				if max < result :
					max = result
					max_a = a
					max_b = b

	print (max,a,b)

if __name__ == "__main__":
    # execute only if run as a script
    god_s_will()
    #main()