import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt
import sys
from compute_rolling_statistics_example import get_rolling_mean, get_rolling_std, get_bollinger_bands


def main():

	# Define date ranges
	start = datetime.datetime(2016, 1, 1)
	end = datetime.datetime(2016, 11, 10)

	# Default ticker
	tickerSymbol = "IBM"

	# Use provided ticker if supplied via command line arg
	if (len(sys.argv) > 0):
		tickerSymbol = str(sys.argv[1]) 
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