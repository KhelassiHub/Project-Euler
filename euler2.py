
#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#find the sum of the even-valued terms.

def fibonaci():
	liste=list()
	liste.append(1)
	liste.append(1)
	for x in range(1,50):
		increm = liste[x]+liste[x-1]
		if increm < 4000000:
			liste.append(increm)
		if increm > 4000000:
			break
	return liste

def main():
	
	fibo=fibonaci()
	somme =0
	for val in fibo:
		if val%2==0:
			somme = somme + val
	print("le résultat exacte est 4613732, votre résultat est {}".format(somme))

if __name__ == "__main__":
    # execute only if run as a script
    main()