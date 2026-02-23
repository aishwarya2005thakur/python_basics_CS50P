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

import numpy as np 
array1 = np.array([6, 7, 8, 10, 13]) 
array2 = np.array([6, 7, 8, 10, 13], dtype=np.int32) 
print(array1.itemsize)   
print(array2.itemsize)   

import numpy as np 
array1 = np.array([6, 7, 8]) 
array2 = np.array([[1, 2, 3],[6, 7, 8]]) 
print("\nData of array1 is: ",array1.data) 
print("Data of array2 is: ",array2.data) 