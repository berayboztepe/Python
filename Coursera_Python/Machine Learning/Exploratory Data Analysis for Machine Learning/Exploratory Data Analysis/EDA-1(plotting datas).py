#******************************************Visualization*********************************************
#feature = özellik
#tick = işaret
#correlation = ilişki
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

path = 'iris_data.csv'
data = pd.read_csv(path)


#Basic Scatter plots with pyplot
plt.plot(data.sepal_length, data.sepal_width, ls='', marker='o')
plt.title("Basic Scatter Plot of Sepal Width, Length")
plt.show()
#to find relationship between sepal_lenght and sepal_width
#ls = line style, '' = no lines
#marker=o, we want circular dot, if we want x, marker=x, etc...







#Scatter plots with multiple layers
plt.plot(data.sepal_length, data.sepal_width, ls='', marker='o', label='sepal')
plt.plot(data.petal_length, data.petal_width, ls='', marker='o', label='petal')
plt.legend()#will show which color is petal, which color is sepal on the graph
plt.title("Scatter Plots with multiple layers")
plt.show()
#plot them in a different color with label






#Histograms
plt.hist(data.sepal_length, bins=25)
plt.title("Histogram of Sepal Length")
plt.show()
#creates a hist with 25 column





#Customizing Plots
#This will make a horizontal graph and we want the values 0-9, and will look 10 sepal_width values
fig, ax = plt.subplots()
ax.barh(np.arange(10), data.sepal_width.iloc[:10])
#Set position of ticks and tick labels
ax.set_yticks(np.arange(0.4, 10.4, 1.0)) #this will allow each tick to be in the middle
ax.set_yticklabels(np.arange(1,11)) #give 1-10 to y labels
ax.set(xlabel='xlabel', ylabel='ylabel', title='Title') #give name to title and x,y labels
plt.title("Customized Horizontal Plots")
plt.show()







#Customizing Plots by Group
data.groupby('species').mean().plot(color=['red', 'blue', 'black', 'green'], fontsize=10.0, figsize=(4, 4))
plt.title("Customized Plots by Groups")
plt.show()
#take means of petal width, length and sepal width, length, we have spesific color to each one
#fontsize for font, figure size for the figure







#Pair plots for features
#Seaborn plot, feature correlations
sns.pairplot(data, hue='species', height=3)
plt.title("Correlations Between Features")
plt.show()
#hue is relationship between species broken down color
#compare sepal length to sepal width, petal length, petal width
#        sepal width to sepal lenght, petal length, petal width
#        petal length to sepal width, sepal length, petal width
#        petal width to sepal lenght, petal length, sepal width





#Seaborn hexbin plot
sns.jointplot(x=data['sepal_length'], y=data['sepal_width'], kind='hex')
plt.show()
#darker hexagons mean, there are more values than ligther hexagons
#and we can also see histograms in it






#Facet grid
#we want to break them into the categories and plot them as histograms
#Seaborn plot, first plot statement
plot = sns.FacetGrid(data, col='species', margin_titles=True)
#margin_titles = means we have titles for each
#show sepal width of all the species in different categories
plot.map(plt.hist, 'sepal_width', color='green')
plt.show()

#Second plot statement
plot = sns.FacetGrid(data, col='species', margin_titles=True)
plot.map(plt.hist, 'sepal_length', color='blue')
plt.show()