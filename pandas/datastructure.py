# learning pandas and numpy 

# data types in pandas :
# series : list of data / 1D array , used for data analysis , cleaning , exploring and manipulating data
# dataframes : same as series but stores multi dimentional values - key and value pair (Hash map) / dirctionary 
#              heterogeneous data storage -> row + column 
#              2D and 3D array values  


import pandas as pd 
a = [1, 7, 2] 
myvar = pd.Series(a) 
print(myvar)

print(myvar[0])

a = [1, 7, 2] 
myvar = pd.Series(a, index = ["x", "y", "z"]) 
print(myvar) 