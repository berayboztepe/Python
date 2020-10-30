import pandas as pd
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
import seaborn as sns
#aggregate = toplanmış, toplu
#distribution = dağılım


data = pd.read_csv('iris_data.csv')

print(data.shape)#shows number of columns and rows
print(data.shape[0])#shows number of rows
print(len(data))#shows number of rows

print("\n\n\n")
print("******************")
print("\n\n\n")


print(data.columns)#shows names of columns
print(data.columns.tolist())#shows names of columns as a list but better
print(data.dtypes)#shows variables are float, int, object etc...


print("\n\n\n")
print("******************")
print("\n\n\n")

#if we look at csv file, every species have Iris before its name and we want to remove it
data['species'] = data.species.str.replace('Iris-', '')
#or
data['species'].apply(lambda x: x[5:])#write all of them after 5. index
print(data.head())


print("\n\n\n")
print("******************")
print("\n\n\n")

print(data.species.value_counts())#count each species



print("\n\n\n")
print("******************")
print("\n\n\n")


print(data.describe())#print counts, means, stds, min, max, %25, %50, %75 of sepal width, length, petal width, length
print("\n\n\n")


stats_df = data.describe()
stats_df.loc["range"] = stats_df.loc["max"] - stats_df.loc["min"]
print(stats_df.loc["range"])#find max - min all of the features and equal it to range(index value)
print(stats_df)#if we look at this, we will see new row called range
print("\n\n\n")



out_fields = ["mean", "25%", "50%", "75%", "range"]#specify columns that we wanna see
stats_df = stats_df.loc[out_fields]
print(stats_df)
print("\n\n\n")

stats_df.rename({'50%': 'median'}, inplace=True)#renamed 50% to median
print(stats_df)



print("\n\n\n")
print("******************")
print("\n\n\n")


#group them by mean and median
print(data.groupby('species').mean())
print("\n")
print(data.groupby('species').median())

#group them in a single table
#different is, we can product them together in np(multiplying all of them) but we cannot do that in first one
print(data.groupby('species').agg(['mean', 'median']))
print("\n\n")#or
print(data.groupby('species').agg([np.mean, np.median]))


print("\n\n\n")
print("******************")
print("\n\n\n")

#if certain fields need to be aggregated differently
agg_dict = {field: ['mean', 'median'] for field in data.columns if field != 'species'}#making a numerical dict but species column
#keys are 'mean' and 'median', values are mean and median
agg_dict['petal_length'] = 'max'#change petal length column with max
#pprint(agg_dict) to see the keys
pprint(data.groupby('species').agg(agg_dict))


print("\n\n\n")
print("******************")
print("\n\n\n")

#Make a scatter plot for sepal_length and sepal_width using pyplot, Label the axes and give the plot a title
#simple scatter plot
ax = plt.axes()#we created an empty box
ax.scatter(data.sepal_length, data.sepal_width)

ax.set(xlabel='sepal Length(cm)',
       ylabel='sepal Width(cm)',
       title='Sepal Length vs Width')
plt.show()


#Make a histogram of any one of the features. Label the axes and give the plot a title
ax = plt.axes()
ax.hist(data.sepal_length, bins=25)
ax.set(xlabel='Sepal Length(cm)',
       ylabel='Frequency',
       title='Distribution of Sepal Lengths')
plt.show()
#Alternatively we can use that as easier
ax1 = data.sepal_width.plot.hist(bins=25)
plt.show()

print("\n\n\n")
print("******************")
print("\n\n\n")




#Create a hist for each features, and then create four individual hist in a single figure overlayed, where each plots contains one feature
sns.set_context('notebook')
ax = data.plot.hist(bins=25, alpha=0.5)#gives us all four of the histograms overlayed(in a single figure)
#with alpha it seems more visible
ax.set_xlabel('Size(cm)')
plt.show()

axList = data.hist(bins=25, figsize=(8, 8))#separately 4 different boxes
#it's a (2, 2) shaped array
for ax in axList.flatten():#make it flatte(4, ) just one array
    if ax.is_last_row():#if ax[x] is the last row
        ax.set_xlabel('Size(cm)')

    if ax.is_first_row():#if ax[x] is the first row
        ax.set_ylabel('Frequency')
plt.show()



print("\n\n\n")
print("******************")
print("\n\n\n")


#Using pandas, make a boxplot for each petal and sepal measurement
data.boxplot(by='species')#gives 4 different boxplot in a single figure
plt.show()



print("\n\n\n")
print("******************")
print("\n\n\n")


#make a single plot where features are separated in the x-axis species are colored with different hues
#first reshape the data so there is only one measurment in each columns

plot_data = (data.set_index('species').stack().to_frame().reset_index().rename(columns={0: 'size', 'level_1': 'measurement'}))
#print(plot_data)

#plot the df from above using Seaborn
sns.set_context('notebook')
sns.set_style('white')
sns.set_palette('dark')
#to make them more visible

f = plt.figure(figsize=(6, 4))
sns.boxplot(x='measurement', y='size', hue='species', data=plot_data)
plt.show()



print("\n\n\n")
print("******************")
print("\n\n\n")

#make a pairplot with seaborn to examine the correlation between each of the measurements
sns.set_context('talk')
plot = sns.pairplot(data, hue='species')
plot._legend.remove()
plt.show()