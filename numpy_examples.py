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

	# Acessing elements
	a = np.random.rand(5, 4)
	print "Array: \n", a

	# Access element at position (3, 2)
	element = a[3, 2]

	# Elements from the second to third columns in the first row
	print a[0, 1:3]

	# Elements from the top corner
	print a[0:2, 0:2]

	# Array before modification
	print "Array before modification: \n", a

	# Assinging a value to a specific location
	a[0, 0] = 1
	print "\n Modified Array with single value: \n", a

	# Assigning a single value to an entire row
	a[1,:] = 2
	print "\n Modified with a replaced row: \n", a 

	# Assigning a list to a column in an array
	a[:, 3] = [1, 2, 3, 4, 5]
	print "\n Modified with a replaced column: \n", a

	# Boolean Index Arrays
	a = np.array([(20, 25, 10, 23, 26, 32, 10, 5, 0), (0, 2, 50, 20, 0, 1, 28, 5, 0)])
	print a

	#Calculating mean 
	mean = a.mean()
	print mean

	# masking - all values less than the mean are removed
	print a[a<mean]

	# Arithmetic Operations
	# Multiply a by 2
	print "\n Multiply a by 2:\n", 2 * a

	# Divide by 2
	print "\n Divide a by 2:\n", a / 2.0

	# Create a new array b
	b = np.array([(100, 200, 300, 400, 500), (1, 2, 3, 4, 5)])
	print "\n Original array b:\n", b

	# Add the two arrays
	print "\nAdd a + b:\n", a + b



if __name__ == "__main__":
	main()