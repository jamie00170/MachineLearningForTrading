import pandas.io.data as web
import datetime
import matplotlib.pyplot as plt
from compute_rolling_statistics_example import get_rolling_mean, get_rolling_std, get_bollinger_bands


def main():

	# Define date ranges
	start = datetime.datetime(2016, 1, 1)
	end = datetime.datetime(2016, 11, 10)

	# Use a DataReader to store the data in a pandas dataframe
	df = web.DataReader('IBM', 'yahoo', start, end)
	
	# Take the Close values
	ibmClose = df['Close']

	# Compute rolling mean 
	rm_IBM = get_rolling_mean(ibmClose, window=20)

	# Compute rolling std
	rstd_IBM = get_rolling_std(ibmClose, window=20)

	# compute Bollinger bands 
	upper_band, lower_band = get_bollinger_bands(rm_IBM, rstd_IBM)

	# Plot the data, retain matplotlib axis object
	ax = ibmClose.plot(title="IBM Bollinger Bands", label="IBM")

	rm_IBM.plot(label="Rolling mean", ax=ax)
	# Add the upper and lower bands to the plot
	upper_band.plot(label="upper band", ax=ax)
	lower_band.plot(label="lower band", ax=ax)

	# Add legend 
	ax.legend(loc='lower right')

	# Show the plot
	plt.show() 


if __name__ == "__main__":
	main()