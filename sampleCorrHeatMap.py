__author__ = 'Matt Morales'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")


#read rocks v mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

#calculate correlations between real-valued attributes
corMat = DataFrame(rocksVMines.corr())

#visualize correlations using heat map
plot.pcolor(corMat)
plot.show()