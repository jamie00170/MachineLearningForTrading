import pandas as pd
import matplotlib.pyplot as plt

from join_data_example import get_data, plot_data
from compute_daily_returns import compute_daily_returns


def main():
	# Read Data
	dates = pd.date_range('2009-01-01', '2012-12-31')
	symbols = ['SPY']
	df = get_data(symbols, dates)
	plot_data(df)

	# Compute Daily returns
	daily_returns = compute_daily_returns(df)
	plot_data(daily_returns, title="Daily Returns", y_label="Daily returns", )

	# Plot histogram
	daily_returns.hist(bins=20) 

	mean = daily_returns['SPY'].mean()
	# print "mean: ", mean
	std = daily_returns['SPY'].std()
	# print "std: ", std

	# plot the mean on the histogram
	plt.axvline(mean, color="w", linestyle='dashed', linewidth=2)
	plt.axvline(std, color="r", linestyle='dashed', linewidth=2)
	plt.axvline(-std, color="r", linestyle='dashed', linewidth=2)
	plt.show()

	# Compute kurtosis
	print daily_returns.kurtosis() 

if __name__ == "__main__":
	main()