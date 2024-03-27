# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:38:36 2023

@author: Dell
"""

#Create a 2D Numpy Array
# Import the libraries

import numpy as np 
import matplotlib.pyplot as plt
#Consider the list a, the list contains three nested lists each of equal size.
# Create a list

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a
# Convert list to Numpy Array
# Every element is the same type

A = np.array(a)
A
# Show the numpy array dimensions

A.ndim
# Show the numpy array shape

A.shape
# Show the numpy array size

A.size
#Accessing different elements of a Numpy Array

# Access the element on the second row and third column

A[1, 2]
# Access the element on the second row and third column

A[1][2]
# Access the element on the first row and first column

A[0][0]
# Access the element on the first row and first and second columns

A[0][0:2]
# Access the element on the first and second rows and third column

A[0:2, 2]
#Basic Operations
#Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 
X
# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y
# Add X and Y

Z = X + Y
Z
#Multiplying a numpy array by a scaler is identical to multiplying a matrix by a scaler.
# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y
# Multiply Y with 2

Z = 2 * Y
Z
# Create a numpy array Y

Y = np.array([[2, 1], [1, 2]]) 
Y
# Create a numpy array X

X = np.array([[1, 0], [0, 1]]) 
X
# Multiply X with Y

Z = X * Y
Z
#We can also perform matrix multiplication with the numpy arrays A and B as follows:
    # Create a matrix A

A = np.array([[0, 1, 1], [1, 0, 1]])
A
# Create a matrix B

B = np.array([[1, 1], [1, 1], [-1, 1]])
B
#We use the numpy function dot to multiply the arrays together.
# Calculate the dot product

Z = np.dot(A,B)
Z
# Calculate the sine of Z

np.sin(Z)
#We use the numpy attribute T to calculate the transposed matrix
# Create a matrix C

C = np.array([[1,1],[2,2],[3,3]])
C
# Get the transposed of C

C.T
#########################################################
###############################################
#Write a Numpy program to get the Numpy version and show the Numpy build configuration.
import numpy as np
print(np.__version__)
print(np.show_config())
#Write a NumPy program to get help with the add function. 
import numpy as np
print(np.info(np.add))
#Write a NumPy program to test whether none of the elements of a given array are zero. 
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
##################################
#Write a NumPy program to test if any of the elements 
#of a given array are non-zero. 
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
############################################
#Write a NumPy program to test a given array 
#element-wise for finiteness (not infinity or not a number). 
import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test a given array element-wise for finiteness :")
print(np.isfinite(a))
#Write a NumPy program to test element-wise 
#for NaN of a given array.
import numpy as np
a = np.array([1, 0, np.nan, np.inf])
print("Original array")
print(a)
print("Test element-wise for NaN:")
print(np.isnan(a))

####################################
#Write a NumPy program to test element-wise for
# complex numbers, real numbers in a given array. 
#Also test if a given number is of a scalar type or not. 
import numpy as np
a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print("Original array")
print(a)
print("Checking for complex number:")
print(np.iscomplex(a))
print("Checking for real number:")
print(np.isreal(a))
print("Checking for scalar type:")
print(np.isscalar(3.1))
print(np.isscalar([3.1]))

####################################
#Write a NumPy program to compute the 
#multiplication of two given matrixes.
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result1 = np.dot(p, q)
print("Result of the said matrix multiplication:")
print(result1)
#Write a NumPy program to compute the outer product of two given vectors. 
import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]
print("original matrix:")
print(p)
print(q)
result = np.outer(p, q)
print("Outer product of the said two vectors:")
print(result)
########################################
#Write a NumPy program to compute the cross product of two given vectors.
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
###################################################
#Write a NumPy program to compute the determinant of a given square array. 
import numpy as np
from numpy import linalg as LA
a = np.array([[1, 0], [1, 2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a))
###########################################
#Write a NumPy program to compute the eigenvalues and right eigenvectors of a given square array. 
import numpy as np
m = np.mat("3 -2;1 0")
print("Original matrix:")
print("a\n", m)
w, v = np.linalg.eig(m) 
print( "Eigenvector of the said matrix",w)
print( "Eigenvalues of the said matrix",v)
###############################################
# Write a NumPy program to compute the inverse of a given matrix. 
import numpy as np
m = np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result =  np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result)
############################
#Write a NumPy program to generate five random numbers from the normal distribution.
import numpy as np
x = np.random.normal(size=5)
print(x)
###################################
#Write a NumPy program to generate six random integers between 10 and 30. 
import numpy as np
x = np.random.randint(low=10, high=30, size=6)
print(x)
#######################
#Write a NumPy program to create a 3x3x3 array with random values. 
import numpy as np
x = np.random.random((3,3,3))
print(x)
################################
# Write a NumPy program to create a 5x5 array with random values 
#and find the minimum and maximum values. 
import numpy as np
x = np.random.random((5,5))
print("Original Array:")
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)
######################################
#Write a NumPy program to get the minimum and maximum value of a given array along the second axis.
import numpy as np
x = np.arange(4).reshape((2, 2))
print("\nOriginal array:")
print(x)
print("\nMaximum value along the second axis:")
print(np.amax(x, 1))
print("Minimum value along the second axis:")
print(np.amin(x, 1))

#np.amax(x, 1): Here np.amax(x, 1) returns the maximum value along the 1st axis (rows) of x 
#which is a 2x2 array. This returns a 1D array with 2 elements 
#where each element is the maximum value of its corresponding row in the original x array. 
#np.amin(x, 1)

#np.amin(x, 1) returns the minimum value along the 1st axis (rows) of x which is a 2x2 array. 
#This returns a 1D array with 2 elements where each element is the minimum value of its 
#corresponding row in the original x array.

#########################################    
#Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(Y)
# Plot lines and/or markers to the Axes.
plt.plot(X, Y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Draw a line.')
# Display the figure.
plt.show()
##########################################
#Write a Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title.
import matplotlib.pyplot as plt
# x axis values
x = [1,2,3]
# y axis values
y = [2,4,1]
# Plot lines and/or markers to the Axes.
plt.plot(x, y)
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Sample graph!')
# Display a figure.
plt.show()
#######################################################
#Write a Python program to draw line charts of the financial data of Alphabet Inc. 
#between October 3, 2016 to October 7, 2016

import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('c:/10-python/fdata.csv')
df.plot()
plt.show()
########################################
#Write a Python program to plot two or more lines with legends, different widths and colors
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title 
plt.title('Two or more lines with different widths and colors with suitable legends ')
# Display the figure.
plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-width-3')
plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-width-5')
# show a legend on the plot
plt.legend()
plt.show()
###########################################
#Write a Python program to plot two or more lines with different styles.
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# Set the x axis label of the current axis.
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Plot lines and/or markers to the Axes.
plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='red', linewidth = 5,  label = 'line2-dashed', linestyle='dashed')
# Set a title 
plt.title("Plot with two or more lines with different styles")
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

##################################################
#Write a Python program to plot two or more lines and set the line markers
import matplotlib.pyplot as plt
# x axis values
x = [1,4,5,6,7]
# y axis values
y = [2,6,3,6,3]
# plotting the points 
plt.plot(x, y, color='red', linestyle='dashdot', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
#Set the y-limits of the current axes.
plt.ylim(1,8)
#Set the x-limits of the current axes.
plt.xlim(1,8)
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Display marker')
# function to show the plot
plt.show()
########################################
#Write a Python program to plot several lines with different format styles in one command using arrays
import numpy as np
import matplotlib.pyplot as plt

# Sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# green dashes, blue squares and red triangles
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3, 'r^')
plt.show()
###########################################
#Write a Python programming to display a bar chart of the popularity of programming Languages
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
plt.show()
###################################################
#Write a Python programming to display a horizontal bar chart of the 
#popularity of programming Languages. 
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
#####################################
#Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women.
import numpy as np
import matplotlib.pyplot as plt
# data to plot
n_groups = 5
men_means = (22, 30, 33, 30, 26)
women_means = (25, 32, 30, 35, 29)
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
rects1 = plt.bar(index, men_means, bar_width,
alpha=opacity,
color='g',
label='Men')
rects2 = plt.bar(index + bar_width, women_means, bar_width,
alpha=opacity,
color='r',
label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()
plt.tight_layout()
plt.show()
##########################################
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2) + np.cos(x)
    
#Creates just a figure and only one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')
#####################################
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))

fig, (ax1, ax2)  = plt.subplots(1, 2,sharey='row')

ax1.text(0.5, 0.5, 
              "left",
              color="green",
              fontsize=18, 
              ha='center')

ax2.text(0.5, 0.5, 
              "right",
              color="green",
              fontsize=18, 
              ha='center')

plt.show()
#############################################
f, (ax1, ax2) = plt.subplots(1, 2,sharey=True)
derivative = 2 * x * np.cos(x**2) - np.sin(x)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.plot(x, derivative)
###############################
import matplotlib.pyplot as plt
import numpy as np
gaussian_numbers = np.random.normal(size=10000)
gaussian_numbers
plt.hist(gaussian_numbers)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
#################################
