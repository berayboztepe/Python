import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor


#RandomForest = bu regressionda diyelim 1000 tane örnek data seçiyorsun ve decision tree hesaplıyorsun.
# bu decision treelerin verilerinin toplamına göre grafik oluşturuluyor.
#random olacağı için her seferinde farklı çıkar!
data = pd.read_csv('positions.csv')


levels = data.iloc[:, 1:2].values.reshape(-1, 1)#x değerleri
salary = data.iloc[:, 2].values#y değerleri tek boyutlu array olarak isteniyor. o yüzden reshape yapmamalıyız!


regression = RandomForestRegressor(n_estimators=10)#kaç datalık decision tree çalıştırılacağı. data fazlalığına göre değişir.
#regression = RandomForestRegressor(n_estimators=10000, random_state=0) yaptığımız zaman her seferinde aynı değer bulunur.
#random_state'yi 1 yaparsak değer değişir ama her seferinde yine aynı değer bulunur random_state değeri değiştikçe göreceğimiz değer de değişir
#ancak her çalıştırmada aynı değer yazılır!
regression.fit(levels, salary)

print(regression.predict([[8.3]]))

