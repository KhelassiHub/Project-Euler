"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""
def LetterCount(num):
	OnesTeens={0:'',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',
	11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',
	19:'Nineteen'}
	tens={10:'ten',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
	hundreds={100:'oneHundred',200:'twoHundred',300:'threeHundred',400:'fourHundred',500:'fiveHundred',600:'sixHundred',
	700:'sevenHundred',800:'eightHundred',900:'nineHundred'}
	stringNumber=str(num)
	if num < 100:
		if num in OnesTeens:
			return OnesTeens[num]
		elif num in tens:
			return tens[num]
		else :
			res = tens[int(stringNumber[0])*10]+OnesTeens[int(stringNumber[1])]
			return res
	elif num >= 100 and num < 1000:
		if num in hundreds:
			return hundreds[num]
		else :
			res = OnesTeens[int(stringNumber[0])]+'HundredAnd'+LetterCount(int(stringNumber[1:]))
			return res
	elif num==1000:
		return 'OneThousand'
def main():
	
	total=0
	for i in range(1,1001):
		total+=len(LetterCount(i))
	print(f'there are in total {total} used')
if __name__ == '__main__':
	main()