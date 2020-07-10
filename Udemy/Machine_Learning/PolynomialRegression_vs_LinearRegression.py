import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#Simple Linear and Ploynomial
data = pd.read_csv('positions.csv')

#burada level sistemi var. bu level sistemine göre(1-10) kişinin leveline göre alacağı tahmini maaş
levels = data.iloc[:, 1].values.reshape(-1, 1)#x ekseni
salary = data.iloc[:, 2].values.reshape(-1, 1)#y ekseni

#burada istediğimiz veriler için tahminleme yapılacak. girilen level değerine göre maaş
regression = LinearRegression()
regression.fit(levels, salary)
print("Salary = ", regression.predict([[8.3]]))#8.3 levelinde olan birinin alacağı maaş, 9'a çok daha yakın çıkıyor.
#bu yüzden bu model çok yanlış cevap verdiği için bu modeli kullanmamalıyız.
print(data.loc[int(8.3-1), ["Position"]])


#bu grafiğe bakarsak kırmızı noktalar, o leveldeki kişinin alması gereken maaşı ifade ediyor.
#regression ile çizdiğimizde ise bu yönteme göre ne kadar maaş alacağı hesaplanıyor ve grafik haline getiriliyor.
#yani 8.3 levelindeki bir kişiye bakarsak, kırmızı nokta ile çizilen doğru arasında ne kadar büyük bir fark olduğu anlaşılıyor.
#Bu yüzden bu modeli kullanmamız yanlış olur
#Levellere göre alınması gereken maaşları gösteren nokta grafiği
plt.scatter(levels, salary, color='red')
#Simple Linear Regressiona göre alınması gereken maaşı gösteren grafik
plt.plot(levels, regression.predict(levels), color='green')
plt.show()
print("\n\n")
#*************************************************************************************************************************************
#POLYNOMIAL REGRESSION!
#eğer verilerin artış hızı aynı değilse(y'ler arasındaki fark) düzgün artmayacağı veya düzgün azalmayacağı için polinomal regression kullanılabilir.
regression1 = PolynomialFeatures(degree=6)#6. dereceden polinom
levelsPoly = regression1.fit_transform(levels)#elimizdeki levels değerlerini polinoma uygulanacak hale getir!
regression2 = LinearRegression()
regression2.fit(levelsPoly, salary)

print(regression2.predict(regression1.fit_transform([[8.3]])))#8.3'ün de polinom karşılığını bulmamız gerekiyor.
plt.scatter(levels, salary, color='red')
plt.plot(levels, regression2.predict(levelsPoly))
plt.show()