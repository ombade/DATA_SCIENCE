# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 08:20:59 2023

@author: Dell
"""

#Write a Python program to draw a line with suitable label in the x axis, y axis and a title. 
import matplotlib.pyplot as plt
X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
'''
This is equivqlent to-
 i in range(1,50):
    print(i, end = ' ')

'''
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
######################################################################################################################################################################################################################
#Write a Python program to draw a line 
#using given axis values with suitable 
#label in the x axis , y axis and a title. 
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
#####################################################################################################################################################################
#Write a Python program to plot two or more lines 
#on same plot with suitable legends of each line. 
import matplotlib.pyplot as plt
# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]

# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]

# plotting the line 1 points 
plt.plot(x1, y1, label = "line 1")
# plotting the line 2 points 
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
# Set a title of the current axes.
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()
########################################
#Write a Python program to plot two or more 
#lines with legends, different widths and colors. 
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
########################################
#Write a Python program to plot two or more lines
# with different styles. 
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
################################################
#Write a Python program to plot two or more lines
# and set the line markers. 
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
######################################
#Write a Python programming to display 
#a bar chart of the popularity of programming Languages. 
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.show()
###############################################3
'''
Write a Python programming to display a horizontal bar chart of the popularity of programming Languages.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

'''
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.show()
#########################################################
#Write a Python programming to display 
#a bar chart of the popularity of programming Languages.
# Use uniform color. 
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0))

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.show()
######################################
#Write a Python programming to display 
#a bar chart of the popularity of programming Languages.
# Use different color for each bar. 
import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.show()
###################################################
#constants
#Import golden constant from the scipy   
import scipy
print("sciPy -golden ratio  Value = %.18f"%scipy.constants.golden)


#fourier transform
from matplotlib import pyplot as plt
import numpy as np 
import seaborn as sns
sns.set_style("darkgrid")
#Frequency in terms of Hertz
fre  = 10
#Sample rate
fre_samp = 100
t = np.linspace(0, 2, 2 * fre_samp, endpoint = False )
a = np.sin(fre  * 2 * np.pi * t)
plt.plot(t, a)
plt.xlabel('Time (s)')
plt.ylabel('Signal amplitude')
plt.show()
#############################

#finding integration
from numpy import exp  
f= lambda x:exp(-x**2)  
'''
def add(a,b,c):
    sum=a+b+c
    return sum
print(add(4,5,6))
add=lambda a,b,c:a+b+c
add(4,5,6)
######################
def mul(a,b,c):
    multi=a*b*c
    return multi
print(mul(6,7,8))
mul=lambda a,b,c:a*b*c
mul(6,7,8)
##################

'''
import scipy 
i = scipy.integrate.quad(f, 0, 1)  
#integratin of f from 0 to 1
print(i)  

###############################
#Finding a determinant of a square matrix  
#importing the scipy and numpy packages
from scipy import linalg
import numpy as np
  
#Declaring the numpy array
A = np.array([[1,2,9],[3,4,8],[7,8,4]])
#Passing the values to the det function
x = linalg.det(A)
  
#printing the result
print('Determinant of \n{} \n is {}'.format(A,x))
####################################



import scipy.misc
import matplotlib.pyplot as plt
face = scipy.misc.face()#returns an image of raccoon
#display image using matplotlib
plt.imshow(face)
plt.show()

##################
#croping
import scipy.misc
import matplotlib.pyplot as plt
face = scipy.misc.face()#returns an image of raccoon
lx,ly,channels= face.shape
# Cropping
crop_face = face[int(lx/4):int(-lx/4), int(ly/4):int(-ly/4)]
plt.imshow(crop_face)
plt.show()
##################################################################################################################################################################
#Blurring or Smoothing  Images using ndimage
from scipy import ndimage,misc
import matplotlib.pyplot as plt
 
face = scipy.misc.face(gray=True)
blurred_face = ndimage.gaussian_filter(face, sigma=3)
very_blurred = ndimage.gaussian_filter(face, sigma=5)
 
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.imshow(face, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(132)
plt.imshow(very_blurred, cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(133)
plt.imshow(blurred_face, cmap=plt.cm.gray)
plt.axis('off')
 #################################################
 
plt.subplots_adjust(wspace=0, hspace=0., top=0.99, bottom=0.01,
                    left=0.01, right=0.99)
 
plt.show()