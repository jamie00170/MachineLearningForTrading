import pandas as pd
import matplotlib.pyplot as plt

def main():
	df = pd.read_csv("data/IBM.csv")

	df[['Close','Adj Close']].plot()
	plt.show() 


if __name__ == "__main__":
	main()