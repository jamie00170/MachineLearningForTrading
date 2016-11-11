'''Build a dataframe in pandas'''
import pandas as pd
import os 
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir='data'):
	return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
	
	df = pd.DataFrame(index=dates)
	# use spy as reference 
	if 'SPY' not in symbols:
		symbols.insert(0, "SPY")

	for symbol in symbols:
		df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
							   parse_dates=True, usecols=['Date', 'Adj Close'],
							   na_values=['nan'])

		# rename to prevent clash
		df_temp = df_temp.rename(columns={'Adj Close':symbol})

		df = df.join(df_temp) 

	df = df.dropna()
	return df

def plot_data(df, title="Stock prices", x_label='Date', y_label="Price"):
	'''Plot stock prices given a dataframe'''
	ax = df.plot(title=title, fontsize=2)
	ax.set_xlabel(x_label)
	ax.set_ylabel(y_label)

	plt.show() # must be called to show plot

def normalize_data(df):
	""" Normalize stock prices using the first row of the dataframe"""
	return df/df.ix[0,:]	

def main():
	# Define date range
	start_date = '2010-01-01'
	end_date = '2010-12-31'
	
	# create an array of datetime index objects for each date in range
	dates = pd.date_range(start_date, end_date)
	
	symbols = ["SPY", "IBM", "GLD", "AAPL"]

	df = get_data(symbols, dates)

	# Slice by row
	#print df.ix['2010-01-01': '2010-01-31']

	# Slice by column
	#print df['AAPL']
	#print df[['IBM', 'GLD']]

	# Slice by row and column
	#print df.ix['2010-01-01': '2010-01-31', ['AAPL', 'IBM']]

	# normalize the data if required 
	#df = normalize_data(df)

	plot_data(df)

	# Compute global statistics for each stock
	# mean for each stock
	print df.mean() 
	# median for each stock - middle value
	print df.median() 
	# standard deviation for each stock, high std indicates high variation
	print df.std() 

if __name__ == "__main__":
	main()
