__author__ = 'Matt_Morales'
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from random import uniform

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#read rocks versus mines data into pandas data frame
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

#change the targets to numeric values

# target =[]

# for i in range(208):
# 	#assign 1 or 0 target value based on "M" or "R" labels
# 	if rocksVMines.iat[i,60] == "M":
# 		target.append(1.0)
# 	else:
# 		target.append(0.0)

# #plot 35 attribute
# dataRow = rocksVMines.iloc[0:208, 35]
# plot.scatter(dataRow, target)

# plot.xlabel("Attribute Value")
# plot.ylabel("Target Value")

# plot.show()

###to improve the visualiztion, this version dithers the points a little and makes them transparent

target = []

for i in range(208):
	if rocksVMines.iat[i,60] == "M":
		target.append(1.0 + uniform(-0.1, 0.1))

	else:
		target.append(0.0 + uniform(-0.1, 0.1))

#plot 35th attribute with semi opaque points
dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target, alpha = 0.5, s=120)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()