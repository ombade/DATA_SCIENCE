#Write a Numpy program to get the Numpy version and show the Numpy build configuration.
import numpy as np
print(np.__version__)
#Write a NumPy program to test whether 
#none of the elements of a given array are zero. 
import numpy as np
x = np.array([1, 2, 3, 4])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x))
x = np.array([0, 1, 2, 3])
print("Original array:")
print(x)
print("Test if none of the elements of the said array is zero:")
print(np.all(x)) 
#################################
#Write a NumPy program to test if 
#any of the elements of a given array are non-zero.  
import numpy as np
x = np.array([1, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))
x = np.array([0, 0, 0, 0])
print("Original array:")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x))
#####################################
#Write a NumPy program to test a given array 
#element-wise for finiteness (not infinity or not a number). 
import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))
#################################
#Write a NumPy program to test 
#element-wise for NaN of a given array.
import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for NaN:")
print(np.isnan(a))
###################################
'''
Write a NumPy program to create an element-wise 
comparison (greater, greater_equal, less and 
            less_equal) of two given arrays. 
'''
import numpy as np
x = np.array([3, 5])
y = np.array([2, 5])
print("Original numbers:")
print(x)
print(y)
print("Comparison - greater")
print(np.greater(x, y))
print("Comparison - greater_equal")
print(np.greater_equal(x, y))
print("Comparison - less")
print(np.less(x, y))
print("Comparison - less_equal")
print(np.less_equal(x, y))
############################
#Write a NumPy program to create a 3x3 identity matrix. 
import numpy as np
array_2D=np.identity(3)
print('3x3 matrix:')
print(array_2D)
#####################################
#Write a NumPy program to generate a random number
# between 0 and 1. 
import numpy as np
rand_num = np.random.normal(0,1,2)
print("Random number between 0 and 1:")
print(rand_num)
##################################
#Write a NumPy program to create a 
#3X4 array and iterate over it. 
import numpy as np
a = np.arange(10,22).reshape((3, 4))
print("Original array:")
print(a)
print("Each element of the array is:")
for x in np.nditer(a):
  print(x,end=" ")
  print()
####################################33
#Write a NumPy program to create a 
#vector of length 5 with values 
#evenly distributed between 10 and 50. 
import numpy as np
v = np.linspace(10, 49, 5)
#10-start point,49-end point,5-nos in vector
print("Length 10 with values evenly distributed between 5 and 50:")
print(v)
#####################################
#Write a NumPy program to create a 3x3 matrix 
#with values ranging from 2 to 10.
import numpy as np
x =  np.arange(2, 11).reshape(3,3)
print(x)
###########################
#Write a NumPy program to reverse an array
# (the first element becomes the last). 

import numpy as np
x = np.arange(12, 38)
print("Original array:")
print(x)
print("Reverse array:")
x = x[::-1]
print(x)
######################################
#Write a NumPy program to compute 
#the multiplication of two given matrices. 
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.dot(p, q)
print("Result of the said matrix multiplication:")
print(result1)
##########################################
#Write a NumPy program to compute 
#the cross product of two given vectors.
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.cross(p, q)
result2 = np.cross(q, p)
print("cross product of the said two vectors(p, q):")
print(result1)
print("cross product of the said two vectors(q, p):")
print(result2)
#################################################
#Write a NumPy program to 
#compute the determinant of a given square array. 
import numpy as np
from numpy import linalg as LA
a = np.array([[1, 0], [1, 2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))
#########################################
#Write a NumPy program to compute 
#the eigenvalues and right eigenvectors 
#of a given square array. 
import numpy as np
m = np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n", m)
w, v = np.linalg.eig(m) 
print( "Eigenvalues of the said matrix",w)
print( "Eigenvectors of the said matrix",v)
################################################
#Write a NumPy program to compute 
#the inverse of a given matrix. 
import numpy as np
print("Original matrix:")
m = np.array([[1,2],[3,4]])
print(m)
result =  np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)
#############################################
#Write a NumPy program to add, subtract, multiply, divide arguments element-wise.
import numpy as np
print("Add:")
print(np.add(1.0, 4.0))
print("Subtract:")
print(np.subtract(1.0, 4.0))
print("Multiply:")
print(np.multiply(1.0, 4.0))
print("Divide:")
print(np.divide(1.0, 4.0))