'''Build a dataframe in pandas'''
import pandas as pd

def main():
	# Define date range
	start_date = '2010-01-22'
	end_date = '2010-01-26'
	
	# create an array of datetime index objects for each date in range
	dates = pd.date_range(start_date, end_date)
	
	# Create an empty dataframe
	df1 = pd.DataFrame(index=dates)

	# Read SPY data into temporary dataframe, using date as the index column
	# which allows a join with our created dataframe
	dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True,
						usecols=['Date', 'Adj Close'], na_values=['nan'])
	
	# Join the two dataframes, uses a left join (only retain rows that are in df1)
	df1 = df1.join(dfSPY)

	# Drop NaN values i.e weekend dates
	df1 = df1.dropna()

	print df1

if __name__ == "__main__":
	main()
