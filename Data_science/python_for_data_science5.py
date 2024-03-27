# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:05:27 2023

@author: Dell
"""

import matplotlib.pyplot as plt
plt.plot([1, 3, 2, 4])

plt.show()
##################################
#Multiline plots
import matplotlib.pyplot as plt
x = range(1, 5)
plt.plot(x, [xi*1.5 for xi in x])

plt.plot(x, [xi*3.0 for xi in x])

plt.plot(x, [xi/3.0 for xi in x])

plt.show()
####################################
#Note how Matplotlib automatically 
#chooses different colors 
#for each line—green for 
#the first line, blue for the second line, 
#and red for the third one (from top to bottom).
########################################
#Grid, axes, and labels
#Adding a grid
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 5)
plt.plot(x, x*1.5, x, x*3.0, x, x/3.0)
plt.grid(True)
plt.show()
################################
#Handling axes
import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(1, 5) 
plt.plot(x, x*1.5, x, x*3.0, x, x/3.0) 
 
plt.axis() # shows the current axis limits values

plt.axis([0, 5, -1, 13]) # set new axes limits
# [xmin,xmax, ymin, ymax]
#[0, 5, -1, 13] 
plt.show()
#####################################
#Adding labels
import matplotlib.pyplot as plt 
plt.plot([1, 3, 2, 4])
 
plt.xlabel('This is the X axis') 
 
plt.ylabel('This is the Y axis') 
 
plt.show()
#####################################
#Adding a title
import matplotlib.pyplot as plt 
plt.plot([1, 3, 2, 4])

plt.title('Simple plot') 
 
plt.show()
#Matplotlib provides a simple function, plt.title(), to add a title to an image
##################################
#Adding a legend
import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(1, 5)
plt.plot(x, x*1.5, label='Normal') 
 
plt.plot(x, x*3.0, label='Fast') 
 
plt.plot(x, x/3.0, label='Slow') 
 
plt.legend() 
 
plt.show()
#############################
#Control colors
import matplotlib.pyplot as plt 
import numpy as np 
y = np.arange(1, 3) 
plt.plot(y, 'y');
plt.plot(y+1, 'm');
plt.plot(y+2, 'c');
plt.show()
##########################
'''Color abbreviation
Color Name
b     blue
c     cyan
g     green
k     black
m     magenta
r     red
w     white
y     yellow
'''
#Specifying styles in multiline plots
import matplotlib.pyplot as plt 
import numpy as np 
y = np.arange(1, 3) 
plt.plot(y, 'y', y+1, 'm', y+2, 'c');
plt.show()
######################################
#Control line styles
import matplotlib.pyplot as plt 
import numpy as np 
y = np.arange(1, 3) 
plt.plot(y, '--', y+1, '-.', y+2, ':');
plt.show()
##################################
'''
Style abbreviation Style
- solid line
-- dashed line
-. dash-dot line
: dotted line

'''
#Control marker styles
'''
Marker abbreviation Marker style
. Point marker
, Pixel marker
o Circle marker
v Triangle down 
marker
^ Triangle up marker
< Triangle left marker
> Triangle right 
marker
1 Tripod down 
marker
2 Tripod up marker
3 Tripod left marker
4 Tripod right marker
s Square marker
p Pentagon marker
* Star marker
h Hexagon marker
H Rotated hexagon 
marker
+ Plus marker
x Cross (x) marker
D Diamond marker
d Thin diamond 
marker
| Vertical line (vline 
symbol) marker
'''
import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1, 3, 0.2)
plt.plot(y, 'x', y+0.5, 'o', y+1, 'D', y+1.5, '^', y+2, 's');
plt.show()
#########################################
#Histogram charts
import matplotlib.pyplot as plt 
import numpy as np 
y = np.random.randn(1000)
plt.hist(y);
plt.show()
####################
import matplotlib.pyplot as plt
plt.bar([1, 2, 3], [3, 2, 5]);
plt.show()
'''
The bar() function is used to generate bar charts in Matplotlib. 
The function expects two lists of values: 
the X coordinates that are the positions of the bar's left margin
and the heights of the bars:

 As we can see  the left margin of the bars start at the
points specified in the first list, 
while their heights are the values of the second list.   
    
'''

#Scatter plots
'''
Bivariate analysis
Scatter plots display values for two sets of data.
 The data visualization is done
as a collection of points not connected by lines. 
Each of them has its coordinates
determined by the value of the variables 
(one variable determines the X position,
the other the Y position).
'''
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y)
plt.show()
##################################################
size = 50*np.random.randn(1000)
colors = np.random.rand(1000)
plt.scatter(x, y, s=size, c=colors);
plt.show()
#######################
#Adding text
import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)
plt.text(-0.5, -0.25, 'Brackmard minimum')
plt.plot(X, Y, c = 'k')
plt.show()
##########################################
#How to use Seaborn for Data Visualization
#pip install seaborn
import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#Seaborn has 18 in-built datasets, 
#that can be found using the following command.
sns.get_dataset_names()
df = sns.load_dataset('titanic')
df.head()
#Count plot
'''
A count plot is helpful when dealing with 
categorical values. It is used to plot the frequency 
of the different categories. 
The column sex contains categorical data in the titanic
 data, i.e., male and female.

'''
sns.countplot(x='sex',data=df)
#x - The name of the column.
#data - The dataframe.
sns.countplot(x='sex', hue = 'survived', data = df,
palette = 'Set1')
sns.countplot(x='sex', hue = 'survived', data = df,
palette = 'Set2')
sns.countplot(x='sex', hue = 'survived', data = df,
palette = 'Set3')

#hue - The name of the categorical column to split the bars.

#palette - The color palette to be used. 
##############################################
#KDE Plot
#A Kernel Density Estimate (KDE) Plot is used 
#to plot the distribution of continuous data.
sns.kdeplot(x = 'age' , data = df , color = 'black')

    

   # x - The name of the column.
   ##data - The dataframe.
    #color - The color of the graph. You can find a list of colors here.
#Distribution plot
sns.displot(x = 'age',kde=True,bins = 6 , data =df)


    #kde - It is set to False by default. However, if you wish to plot a KDE graph on top of the bars, you can set it to True.

   # bins - The number of bins/bars. 
   #The lower the number, wider the bars and wider the intervals.
sns.displot(x ='age',kde=True,bins = 5 ,
hue = df['survived'] , palette = 'Set1', data=df)
#Scatter plot
#For this plot and the plots below,
# we will be working with the iris dataset. 
#The iris dataset contains data related 
#to flower’s petal size (petal length and petal width)
# and sepal size (sepal length and sepal width).
#These features are used to classify the type of iris
# (Setosa, Versicolour, and Virginica).

#First, we will need to load the iris dataset.
df = sns.load_dataset('iris')
df.head()
#Scatter plots help understand co-relation between data,
sns.scatterplot(x='sepal_length', y ='petal_length' ,
data = df , hue = 'species')
'''
In the plot above we can observe that an iris flower 
with a sepal length < 6cm and petal length < 2cm 
is most likely of type setosa. 
Although there is no distinct boundary present between 
the versicolor dots and virginica dots, 
an iris flower with petal length between 2cm and 5cm 
is most likely of type versicolor, 
while iris flowers with petal length > 5cm 
are most likely of type virginica.

'''
#Joint plot
#A Joint Plot is also used to plot the correlation between data.
sns.jointplot(x='sepal_length' , y ='petal_length',
data = df , kind = 'reg')

sns.jointplot(x='sepal_length' , y ='petal_length',
data = df , kind = 'hist')

sns.jointplot(x='sepal_length' , y ='petal_length',
data = df , kind = 'kde')

'''
    kind - The kind of plot to be plotted. 
    It can be one of the following.

'scatter', 'hist', 'hex', 'kde', 'reg', 'resid'
'''
#Pair plots
sns.pairplot(df)
###########################################
#A heat map can be used to visualize confusion, matrices, and correlation.
corr = df.corr()
sns.heatmap(corr)
########################################
#Visualizing the Pokemon dataset
import pandas as pd
pokemon_df = pd.read_csv('c:/10-python/pokemon.csv')
pokemon_df.head()
plt.figure(figsize=(15,8))
sns.countplot(x = 'type1' , data = pokemon_df,
hue = 'is_legendary')
#Relation between Attack and Defense
sns.pairplot(x_vars=['attack' , 'defense','sp_attack','sp_defense'] ,
y_vars=['attack' , 'defense','sp_attack','sp_defense'] ,
data = pokemon_df)
#Relation between Height and Weight
sns.jointplot(x = 'weight_kg', y = 'height_m',
data = pokemon_df,hue = 'is_legendary')
#Based on the graph above, we can conclude that 
#height and weight of a Pokemon do not have 
#any correlation.