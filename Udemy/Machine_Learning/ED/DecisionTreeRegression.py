import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import DecisionTreeRegressor


#DecisionTree = aradığın maaş CEO'nun diye düşünelim.
#önce sana baştan soracak, aradığın software engineer mi? evet veya hayır.
#hayır ise, aradığın sr. software engineer mi? evet veya hayır.
#hayır ise derken böyle devam edece ve en son: aradığın CEO mu? evet veya hayır.
#cevap evet olacak ve sana aradığın maaş gösterilecek. Olay bundan ibaret, bu decision tree'leri grafik haline getirmek üzerine çalışıyoruz.
data = pd.read_csv('positions.csv')


levels = data.iloc[:, 1:2].values.reshape(-1, 1)#x değerleri
salary = data.iloc[:, 2:3].values.reshape(-1, 1)#y değerleri

#direkt sayıları verir. ancak mesela 8-8.5 arası 8'i, 8.6-8.9 arası 9'u verir.
regression = DecisionTreeRegressor()
regression.fit(levels, salary)

print(regression.predict([[8.6]]))

#asıl değerlerin noktalarla gösterilmesi
#iki nokta arasındaki değişimin(yani daha tam sonraki noktaya gitmeden değişim olmasının) sebebi = 8-8.5 arasının 8, 8.6- 8.9 arasının 9'u vermesinden.
plt.scatter(levels, salary, color='red')
x = np.arange(min(levels), max(levels), 0.01).reshape(-1, 1)
plt.plot(x, regression.predict(x), color='blue')
plt.show()