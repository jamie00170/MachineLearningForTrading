import numpy as np


def main():
	# List to 1D array
	print np.array([1, 3, 4])

	# List of tuples to 2D array
	print np.array([(2, 3, 4), (5, 6, 7)])

	# Empty array
	print np.empty(5)

	# Empty 2D array
	print np.empty((5, 4))

	# Create a 2D array full of 1s
	print np.ones((5, 4))

	# Specifying the data type, float by default
	print np.ones((5, 4), dtype=np.int)

	# an array of zeros
	print np.zeros((10, 10), dtype=np.int)

	# generate an array full of random numbers. uniformly sampled from [0.0, 1.0)
	print np.random.random((5, 4))

	# Sample numbers from a Gussian distribution
	print np.random.normal(size=(2, 3)) # "Standard normal" (mean, s.d. = 1)

	# Random integers 
	print np.random.randint(10) # an int in [0, 10)
	print np.random.randint(0, 10) # explicit as above
	print np.random.randint(0, 10, size=5) # 5 rand ints as an array
	print np.random.randint(0, 10, size=(2, 3)) # 2x3 array of rand ints

	a = np.random.randint(0, 10, size=(5, 4))
	print "Array, a: \n", a
	print a.shape # returns (5, 4)
	print a.shape[0] #no. of rows
	print a.shape[1] #no. of columns

	print len(a.shape) # returns dimension of array

	print a.size # returns num of elements in a 

	print a.dtype # returns the data type of elements in a

	# Sum of all elements 
	print "Sum of all elements: ", a.sum()

	#Iterate over rows, to compute sum of each column
	print "Sum of each column: \n", a.sum(axis=0)

	#Iterate over columns to compute sum of each row
	print "Sum of each row :\n", a.sum(axis=1)

	print "Minimum of each column: \n", a.min(axis=0)
	print "Maximum of each row:\n", a.max(axis=1)
	print "Mean of all elements: ", a.mean() 

if __name__ == "__main__":
	main()