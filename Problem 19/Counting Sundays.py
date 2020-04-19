# You are given the following information, but you may prefer to do some research for yourself.

#     - 1 Jan 1900 was a Monday.
#     - 7 Jan 1900 was a Sunday.
#     - Thirty days has September,
#     - April, June and November.
#     - All the rest have thirty-one,
#     - Saving February alone,
#     - Which has twenty-eight, rain or shine.
#     - And on leap years, twenty-nine.
#     - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def main():
	months={'January':31,'February':28,'March':31,'April':30,'Mai':31,'June':30,'July':31,'August':31,'September':30,
	'October':31,'November':30,'December':31}
	print('Starting from 1 January 1900 till 31 December 2000 there are 36890 days')
	numberOfDays=0
	numberOfSundays=0
	realSundayResult=0
	# if January 1 1900 was a monday then January 1 1901 was a Tuesday because 1900 has 365 days
	for Year in range(1901,2001):
		if Year%4==0 and Year%100!=0 or Year%400==0:
			months['February']=29
		else :
			months['February']=28
		for days in months.values():
			numberOfDays+=days
			if (numberOfDays+1)%7==5:	# equal to 5 because if the module is equal to 0 we would calculate 
			# the number Tuesday's that fell in the first of the month (the margin of 5 days between tuesday and 
			# Sunday is 5 days)	
				realSundayResult+=1
	for i in range(1,numberOfDays+1):
		if i%7==0:
			numberOfSundays+=1
	print(f'Strating from 1 January 19001 till 31 Ddecember 2000 there are {numberOfDays} days')
	print(f'The number of Sundays in that period of time is {numberOfSundays} Sunday')
	print(f'But the real number of Sundays that fell in the first of the month is {realSundayResult}')

if __name__ == '__main__':
	main()