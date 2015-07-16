__author__ = 'Matthew Morales'
import numpy as np
import pylab
import scipy.stats as stats
import urllib2
import sys

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

type = [0] * 3
colCounts = []

#generate summary stats for column 3
col = 3
colData = []
for row in xList:
	colData.append(float(row[col]))

stats.probplot(colData, dist="norm", plot=pylab)

pylab.show()