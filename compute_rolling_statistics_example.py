import pandas as pd 
import matplotlib.pyplot as plt
from join_data_example import get_data, plot_data

def main():
	# Read SPY data
	dates = pd.date_range("2012-01-01", "2012-12-31")
	symbols = ['SPY']
	df = get_data(symbols, dates)

	# Plot SPY data, retain matplotlib axis object
	ax = df['SPY'].plot(title="SPY rolling mean", label="SPY")

	# Compute rolling mean using a 20 day window
	rm_SPY = pd.rolling_mean(df['SPY'], window=20)

	# Add rolling mean to same plot
	rm_SPY.plot(label="Rolling mean", ax=ax)

	# Add legend 
	ax.legend(loc='upper left')

	# Show the plot
	plt.show() 


if __name__ == "__main__":
	main()
