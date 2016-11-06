import pandas as pd

def get_max_close(symbol):
	"""Return the maximum closing value for the stock which
	   corressponds to the symbol given, note the range of 
	   dates is defined by the csv file for the stock"""

	# read in the data as a dataframe
	df = pd.read_csv("data/{}.csv".format(symbol))

	#compute the max
	max_close = df['Close'].max()

	return max_close 

def get_mean_volume(symbol):
	"""Return the mean volume traded in a day for the stock which
	   corressponds to the symbol given, note the range of 
	   dates is defined by the csv file for the stock"""
	df = pd.read_csv("data/{}.csv".format(symbol))

	mean_volume = df['Volume'].mean()

	return mean_volume


def main():
	# print the max closing price and mean volume 
	# of the sepcified symbols
	for symbol in ['AAPL', 'IBM']:
		print "Max close"
		print symbol, get_max_close(symbol)

		print "Mean volume"
		print symbol, get_mean_volume(symbol)


if __name__ == "__main__":
	main()
