import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#Multiple Linear Regression
#x veya y değerleri birden fazla ise
data = pd.read_csv('insurance.csv')

#yaş ve bmi'ye göre harcamaları bulmak için değerleri reshape ettik(regressionda kullanabilmek için****)
expenses = data.expenses.values.reshape(-1, 1)#y ekseni
age_bmi = data.iloc[:, [0, 2]].values#x ekseni. age ve bmi değerlerini birleştirdik

#burada istediğimiz veriler için tahminleme yapılacak
regression = LinearRegression()
regression.fit(age_bmi, expenses)
print(regression.predict([[20, 20], [20, 21], [21, 20], [21, 21]]))#20 yaş ve 20 bmi olan biri için tahmini expenses değerleri. Cevap = 5068.47110398
#yaş ve bmi arttıkça expenses de artar.


