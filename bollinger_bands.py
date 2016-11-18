import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt
import sys
import argparse
from compute_rolling_statistics_example import get_rolling_mean, get_rolling_std, get_bollinger_bands


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("ticker", help="The Ticker symbol of the stock you wish to graph.", type=str)
	parser.add_argument("-sd", "--startdate", help="The date you want the price of the stock to start from. " + \
		" N.B. date should be of the format ddmmyyyy")
	args = parser.parse_args()

	if (len(sys.argv) > 1):
		tickerSymbol = args.ticker
	else:
		print "Must provide a ticker symbol"
		sys.exit(1)

	if args.startdate:
		start_day = int(args.startdate[0:2])
		start_month = int(args.startdate[2:4])
		start_year = int(args.startdate[4:])
		

	# Define date ranges
	start = datetime.datetime(start_year, start_month, start_day)
	end = datetime.datetime(2016, 11, 17) 
		
	try: 
		# Use a DataReader to store the data in a pandas dataframe
		df = web.DataReader(tickerSymbol, 'yahoo', start, end)
		
		# Take the Close values
		stockClose = df['Close']

		# Compute rolling mean 
		rm_Stock = get_rolling_mean(stockClose, window=20)

		# Compute rolling std
		rstd_Stock = get_rolling_std(stockClose, window=20)

		# compute Bollinger bands 
		upper_band, lower_band = get_bollinger_bands(rm_Stock, rstd_Stock)

		# Plot the data, retain matplotlib axis object
		ax = stockClose.plot(title=tickerSymbol + "Bollinger Bands", label=tickerSymbol)

		rm_Stock.plot(label="Rolling mean", ax=ax)
		# Add the upper and lower bands to the plot
		upper_band.plot(label="upper band", ax=ax)
		lower_band.plot(label="lower band", ax=ax)

		# Add legend 
		ax.legend(loc='lower right')

		# Show the plot
		plt.show() 
	except:
		print "Can't find data for ", tickerSymbol


if __name__ == "__main__":
	main()