"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:
012   	0123   ABC
021     0132   ACB
102     0213   BAC
120     0231   BCA
201     0312   CAB
210     0321   CBA
        1023
        1032
        1203
        1230
        1302
        1320
        2013
        2031
        2103
        2130
        2301
        2310
        3012
        3021
        3102
        3120
        3201
        3210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from itertools import permutations

# def permut(lista,indexD,indexF):
# 	if indexD==indexF:
# 		print(lista)
# 	for i in range(indexD,indexF+1):
# 		lista[indexD],lista[i]=lista[i],lista[indexD]
# 		permut(lista,indexD+1,indexF)
# 		lista[indexD],lista[i]=lista[i],lista[indexD]

def main():
	result=list(permutations([0,1,2,3,4,5,6,7,8,9]))
	print(result[999999])
	# ex=[0,1,2]
	# permut(ex,0,2)

if __name__ == '__main__':
	main()