import pandas as pd
import matplotlib.pyplot as plt

from join_data_example import get_data, plot_data
from compute_daily_returns import compute_daily_returns

def main():
	# Read Data
	dates = pd.date_range('2009-01-01', '2012-12-31')
	symbols = ['SPY', 'IBM']
	df = get_data(symbols, dates)
	# plot_data(df)

	# Compute Daily returns
	daily_returns = compute_daily_returns(df)
	plot_data(daily_returns, title="Daily Returns", y_label="Daily returns")

	daily_returns['SPY'].hist(bins=20, label="SPY")
	daily_returns['IBM'].hist(bins=20, label="IBM")
	plt.legend(loc="upper right")
	plt.show()

if __name__ == "__main__":
	main()