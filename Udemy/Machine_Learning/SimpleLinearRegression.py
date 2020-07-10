import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#LINEAR REGRESSION EXAMPLE
#Amacı = belirli bir tabloya göre(boy, kilo tablosu) değerlerden biri artıyorsa diğerinin de artması beklenir(Doğru orantı)
#bu sayede düzgün artan grafik çizilir ve düzgün artan doğru üzerinde kalan veriler bizim ilgileneceğimiz verilerdir.
#bu doğrunun altında veya üstünde kalan veriler ise hata payları içerir.
#bu kod ile rastgele girdiğimi boy değerine göre(inch) tahmini kilo değeri buluyoruz ve bunu görselleştiriyoruz.
#aynı zamanda düzgün artan doğrusunu çiziyoruz.
data = pd.read_csv('hw_25000.csv')

#boy ve kilodaki değerleri reshape ettik(regressionda kullanabilmek için****)
boy = data.Height.values.reshape(-1, 1)
kilo = data.Weight.values.reshape(-1, 1)

#bu kısımda predict ile girilen boy değerinin, oluşturduğumuz tablodaki kilo değeri ekrana yazdırılıyor.Tahmini***
regression = LinearRegression()
regression = regression.fit(boy, kilo)#fit ile height ve weight alanı oluşturuyoruz
print(regression.predict([[70]]))#bu kısımda boy değeri giriyoruz ve tabloya göre tahmini kilo değeri yazdırılıyor.

#bu kısım doğrunun çizimini sağlıyor. Doğrunun üzerindeki değerler tahmini olarak bulunan değerler. Kalan değerlerde ise hata payı var.
x = np.arange(min(data.Height), max(data.Height)).reshape(-1, 1)#min ve max x değerleri
plt.plot(x, regression.predict(x), color='red')#x'in y karşılığı regression predict olur
print("\n")
#R Square kullanımı = kullandığımız modelin ne kadar doğru olduğu.
#bire ne kadar yakınsa o kadar doğru!
#girilen bir boy değeri var ve tahmini kilo değeri döndürülüyor. ancak bu boy değerine karşılık başka kilo değerleri de var
#burada amaç bu diğer y değerlerine olan sapmayı bulmak!
print(r2_score(kilo, regression.predict(boy)))#cevap = 0.2528666917428809 yani %25 doğruluk payı var!


plt.scatter(data.Height, data.Weight)
plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.title("Linear Regression Model")
plt.show()