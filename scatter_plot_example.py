import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from join_data_example import get_data, plot_data
from compute_daily_returns import compute_daily_returns

def main():

	# Read data
	dates = pd.date_range("2009-01-01", "2012-12-31")
	symbols = ['SPY', 'IBM', 'GLD']
	df = get_data(symbols, dates)

	# Compute daily returns
	daily_returns = compute_daily_returns(df)

	# Scatterplot SPY vs IBM
	daily_returns.plot(kind="scatter", x="SPY", y="IBM")
	beta_IBM, alpha_IBM = np.polyfit(daily_returns['SPY'], daily_returns['IBM'], 1)
	print "beta_IBM: ", beta_IBM
	print "alpha_IBM: ", alpha_IBM
	# for every point calculate the line: ma + b
	plt.plot(daily_returns['SPY'], beta_IBM *daily_returns['SPY'] + alpha_IBM, "-", color="r")
	plt.show()

	# Scatterplot SPY vs GLD
	daily_returns.plot(kind="scatter", x="SPY", y="GLD")
	beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
	plt.plot(daily_returns['SPY'], beta_GLD *daily_returns['SPY'] + alpha_GLD, "-", color="r")
	plt.show()

	# Calculate correlation coefficient
	print daily_returns.corr(method="pearson")

if __name__ == "__main__":
	main()