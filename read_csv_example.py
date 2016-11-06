import pandas as pd

def test_run():
	df = pd.read_csv("data/AAPL.csv")
	
	# print df.head() - prints the first 5 rows 
	# (The most recent data)

	# print df.tail() - prints the last 5 rows
	# (The oldest data)

	# prints the last 10 rows
	#print df.tail(10) 

	# print row 10 to 20
	print df[10:21]


if __name__ == "__main__":
	test_run()

