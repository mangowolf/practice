'''Stock Trading'''

#The efficiency of the method is O(n) and takes O(1) space
def get_max_profit(stock_prices_yesterday):

	try:
		low = stock_prices_yesterday[0]
		n = len(stock_prices_yesterday)
		lowIndex = 0

		#Go through the array and find the lowest value
		for i in range(0,n-1):
			if low > stock_prices_yesterday[i]:
				low = stock_prices_yesterday[i]
				lowIndex = i

		#Set the highest value to the current lowest
		high = low
		highIndex = lowIndex

		#Go through and find the highest value after finding the lowest
		for i in range(lowIndex + 1,n-1):
			if high < stock_prices_yesterday[i]:
				high = stock_prices_yesterday[i]
				highIndex = i
		return (high - low)
	except:
		return e

stock_prices_yesterday = [10, 7, 5, 4, 3, 1]

print get_max_profit(stock_prices_yesterday)
#returns 6 (buying for $5 and selling for $11)