import pandas as pd 
import matplotlib.pyplot as plt
from join_data_example import get_data, plot_data

def compute_daily_returns(df):
	"""Compute and return the daily return values."""
	daily_returns = (df / df.shift(1)) - 1
	daily_returns.ix[0, :] = 0 # set value to 0 for row 0 since no previous day to calucluate from
	return daily_returns

def main():
	# Read a month of data
	dates = pd.date_range('2012-07-01', '2012-07-31')
	symbols = ['SPY', 'GLD']
	df = get_data(symbols, dates)
	plot_data(df)

	# Compute daily returns 
	daily_returns = compute_daily_returns(df)
	plot_data(daily_returns, title="Daily returns", y_label="Daily returns")


if __name__ == "__main__":
	main()