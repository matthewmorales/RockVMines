__author__ = 'Matthew Morales'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

#print head and tale of data frame
print "***HEAD***"
print (rocksVMines.head())
print "***TAIL***"
print (rocksVMines.tail())

#print summary of data frame
summary = rocksVMines.describe()

print "***SUMMARY***"

print(summary)