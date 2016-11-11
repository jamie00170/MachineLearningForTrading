import pandas as pd 
import matplotlib.pyplot as plt
from join_data_example import get_data, plot_data

def get_rolling_mean(values, window):
	"""Return rolling mean of given values, using the given window size """
	return pd.rolling_mean(values, window=window)

def get_rolling_std(values, window):
	"""Return rolling standard deviation of given values, using the given window size """
	return pd.rolling_std(values, window=window)

def get_bollinger_bands(rm, rstd):
	"""return upper and lower Bollinger Bands """
	upper_band = rm + rstd * 2
	lower_band = rm - rstd * 2
	return upper_band, lower_band

def main():
	# Read SPY data
	dates = pd.date_range("2012-01-01", "2012-12-31")
	symbols = ['SPY']
	df = get_data(symbols, dates)

	# Compute Bollinger Bands
	# 1. Compute rolling mean using a 20 day window
	rm_SPY = get_rolling_mean(df['SPY'], window=20)

	# 2. Compute rolling standard deviation
	rstd_SPY = get_rolling_std(df['SPY'], window=20)

	# 3. Compute upper and lower bands
	upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

	# Plot SPY data, retain matplotlib axis object
	ax = df['SPY'].plot(title="SPY Bollinger Bands", label="SPY")
	# Add rolling mean to same plot
	rm_SPY.plot(label="Rolling mean", ax=ax)
	# Add the upper and lower bands to the plot
	upper_band.plot(label="upper band", ax=ax)
	lower_band.plot(label="lower band", ax=ax)

	# Add legend 
	ax.legend(loc='upper left')

	# Show the plot
	plt.show() 


if __name__ == "__main__":
	main()
