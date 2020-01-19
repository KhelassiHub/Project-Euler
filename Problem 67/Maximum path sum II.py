# By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
# the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
# a 15K text file containing a triangle with one-hundred rows.

# NOTE: This is a much more difficult version of Problem 18. 
# It is not possible to try every route to solve this problem, 
# as there are 2^99 altogether! If you could check one trillion (10^12) routes every second 
# it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

def main():	
	with open('triangle.txt','r') as f:
		triangle=[line.splitlines()[0].split() for line in f]
	for i in range(len(triangle)):
		for j in range(len(triangle[i])):
			triangle[i][j]=int(triangle[i][j])
	for i in range(len(triangle)-2,-1,-1):
		for j in range(len(triangle[i])):
			triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1])
		triangle.remove(triangle[i+1])
	
	print(f'le résultat est {triangle[0][0]}')

if __name__ == '__main__':
	main()