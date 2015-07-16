__author__ = 'mike_bowles'
import urllib2
import sys
import numpy as np

#read data from UCI data repo
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib2.urlopen(target_url)

#arrange data into list for labels and list of lists for attributes
xList = []
labels = []

for line in data:
	#split on coma
	row = line.strip().split(",")
	xList.append(row)

# sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
# sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])) + '\n')

nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []


#generate summary stats for column 3 (e.g.)
col = 3
colData = []
for row in xList:
	colData.append(float(row[col]))

colArray = np.array(colData)

colMean = np.mean(colArray)
colsd = np.std(colArray)

sys.stdout.write("Mean = " + '\t' + str(colMean) + '\t\t' + "Standard Deviation = " + '\t' + str(colsd) + "\n")

#calculate quantile boundaries
ntiles = 4

percentBdry = []

for i in range(ntiles + 1):
	percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")


#run again with 10 equal intervals
ntiles = 10

percentBdry = []

for i in range(ntiles + 1):
	percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

sys.stdout.write("Boundaries for 10 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")



#the last column contains categorical variables
col = 60
colData = []
for row in xList:
	colData.append(row[col])

unique = set(colData)
sys.stdout.write("Unique Label Values \n")
print(unique)

#count up number of elements having each value
catDict = dict(zip(list(unique), range(len(unique))))

catCount = [0] * 2

for elt in colData:
	catCount[catDict[elt]] += 1

sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)