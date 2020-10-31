import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
#outlier = aykırı
#skew = çarpıklık, eğrilik
#trajectory = yörünge
#quantity = miktar
#interaction = etkileşim
#dependent = bağımlı

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 100)

df = pd.read_csv('AmesHousing.csv')

print(df.info())#provide us column names, how many non-null values each of the columns have and dtype(int, float or object etc.)
#fe, in Alley, we have many missing datas(198 non-null)


#df['Gr Liv Area'].hist()#we look at specific column and we see there are some outliers in this column.
#plt.show()


print("\n\n\n")
print("****************")
print("\n\n\n")



df = df.loc[df['Gr Liv Area'] <= 4000, :]
print("Number of rows in the data = ", df.shape[0])
print("Number of columns in the data = ", df.shape[1])
data = df.copy()
print("\n\n")


print(df.head())#if we look, we will see first 2 columns(order and PID)
print(len(df.PID.unique()))#shows unique values in that df. if unique number equals to number of rows, that means every single value is a unique value
#that's not gonna give us a predictive value becaues every single value is unique, it can't learn anything
# so we drop these 2 columns

df.drop(['Order', 'PID'], axis=1, inplace=True)
#if we do axis = 1, we say the place of column that we want to drop. otherwise it looks every single column
#inplace = True means we change df

print("\n\n\n")
print("****************")
print("\n\n\n")



#let's get into some feature transformations

print(df.select_dtypes('number'))#shows only numerical datas. it can be number, int, float(numerical) or object etc.
num_cols = df.select_dtypes('number').columns#equal to our variable num_cols


#let's take a look skews. 0 = no skew, 0+ = right skew, 0- = left skew
#above 0.75 means heavily skewing

skew_limit = 0.75
skew_vals = df[num_cols].skew()
print(skew_vals)
print("\n\n")

#skew only above limits
#most scewed on the top, least skewed above 0.75 on the bottom
skew_cols = skew_vals[abs(skew_vals) > skew_limit].sort_values(ascending=False)#ascending false means sort them shortest to largest
print(skew_cols)

print("\n\n\n")
print("****************")
print("\n\n\n")


#take a look transformed and non transformed data
#and transform it more normally distributed column
#log1p = when our input value is so small, using log1p will give more accurate result than np.log
#x is so small that when real-valued input, 1 + x == 1. if we calculate it with log, it will give result of 0
#but log1p will give more accurate result
#first choose a field

field = 'SalePrice'

#Create two subplots and a figure. plt.subplots = 2 plots in a single figure

fig, (axbefore, axafter) = plt.subplots(1, 2, figsize=(10, 5))

#Create a histogram on the "ax_before" subplot

df[field].hist(ax=axbefore)

#Apply a log tranformation (numpy syntax) to this column

df[field].apply(np.log1p).hist(ax=axafter)

axbefore.set(title='before np.log1p', ylabel='frequency', xlabel='value')
axafter.set(title='after np.log1p', ylabel='frequency', xlabel='value')
fig.suptitle('Field "{}"'.format(field))#set super title called SalePrice
#plt.show()

print("\n\n\n")
print("****************")
print("\n\n\n")

#do a skewed transformation

for col in skew_cols.index.values:
    if col == "SalePrice":
        continue
    df[col] = df[col].apply(np.log1p)

print("\n\n\n")
print("****************")
print("\n\n\n")


#let's go back to the copied data and look how many values are missing

print(data.isnull().sum().sort_values())#to see how many data is missing, sum them and sort them from lowest to largest
print("\n\n")
smaller_df = df.loc[:, ['Lot Area', 'Overall Qual', 'Overall Cond', 'Year Built', 'Year Remod/Add', 'Gr Liv Area',
                       'Full Bath', 'Bedroom AbvGr', 'Fireplaces', 'Garage Cars', 'SalePrice']]

print(smaller_df.describe())

print("\n\n")

print(smaller_df.info())#if we look, we will see there is only one value that is null

smaller_df = smaller_df.fillna(0)#now that null value became 0


#let's generate visuals to better understand the target and feature-target relationships with pairplot
#it helps to find if there is a linear relationships between variables and target column, we'd want to do transformations with the transform variable and our target variable
#sns.pairplot(smaller_df, plot_kws=dict(alpha=.1, edgecolor='none'))
#plt.show()

print("\n\n\n")


#suppose our target variable is the SalePrice, we can set up separate variables for features and  target

x = smaller_df.loc[:, ['Lot Area', 'Overall Qual', 'Overall Cond', 'Year Built', 'Year Remod/Add', 'Gr Liv Area',
                       'Full Bath', 'Bedroom AbvGr', 'Fireplaces', 'Garage Cars']]

y = smaller_df['SalePrice']


#let's add polynomial features. we saw earlier in relationships between them, in second and sixth column, we see upward trajectory that is
#not linear.

x2 = x.copy()

x2['OQ2'] = x2['Overall Qual'] ** 2
x2['GLA2'] = x2['Gr Liv Area'] ** 2


#Each feature is treated as an independent quantity. However, there may be interaction terms, in which the impact of one feature may dependent on
#the current value of a different feature
#fe, there may be a higher premium for increasing overall qual for houses that were built more recently(overall qual x year built)
#fe, to get at something like quality per square foot we could divide overall qual / lot area

x3 = x2.copy()
x3['OQ_x_YB'] = x3['Overall Qual'] * x3['Year Built']
x3['OQ_/_LA'] = x3['Overall Qual'] / x3['Lot Area']



#how to input categorical variables as numerical features
#One-Hot Encoding
#before going straight to dummy variables, it's a good idea to check category counts to make sure all categories have reasonable representation

print(df['House Style'].value_counts())

print(pd.get_dummies(df))#we have 82 columns, if we run that we will have 303 columns and for every single column that is a object
#it will come up with a dummy variable(fe we have sale condition as object, there will be sale condition partial, sale condition normal etc.
#so on and so forth as specific values(each object column is 0 or 1))

print("\n\n\n")
#it only shows house style. 1Story has its own column now and beacuse of representing the original column, these new columns can only take 1s and 0s.
print(pd.get_dummies(df['House Style'], drop_first=True).head())

print("\n\n\n")
#we look at neighborhood columns. there may be another column that we want to transform into a one-hot coding.
#there is a couple different values that have low counts and we want to group these ones to thier own categories
nbh_counts = df.Neighborhood.value_counts()
print(nbh_counts)
print("\n\n\n")

other_nbhs = list(nbh_counts[nbh_counts <= 8].index)
print(other_nbhs)

print("\n\n\n")
x4 = x3.copy()
x4['Neighborhood'] = df['Neighborhood'].replace(other_nbhs, 'Other')#we replace that has 3 low counts of columns as Other
print(x4.Neighborhood.value_counts())

