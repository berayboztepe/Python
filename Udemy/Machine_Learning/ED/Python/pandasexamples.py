import pandas as pd
import numpy as np

#veri tipi verilmediği sürece float olur.
"""s = pd.Series()
print(s)"""

#bu sefer de dtype = object olur. görselleştirme açısından pandas indexleme yapar.
data = np.array(["beray", "emre", "biröl"])
s1 = pd.Series(data)
print(s1)
s1 = pd.Series(data, index = [5, 6, 7])#. bunu yaparsak indexler parantez içi verilen sayılar olur.





#---------------------------------------------------------------------------------------------------------------------------
print("\n\n")
print("*****************")
print("\n\n")
#mesela dersler ve aldığı not olarak da güzel görselleştirme açısından yazdırılabilir.
data2 = {"matematik" : 70, "fizik" : 80, "beden eğitimi": 100}
s2 = pd.Series(data2, index = ["fizik", "matematik", "beden eğitimi"])
print(s2)
#s2'yi tanımlarken index kullanıyorsak, yerlerini farklı yazsak bile o stringlerin karşısına o stringlerin gösterdiği sayı değeri yazılır

print("\n\n")
print("*****************")
print("\n\n")
#---------------------------------------------------------------------------------------------------------------------------





#bu hata vermez, aksine 1e de 2ye de 5 değerini yazar
s3 = pd.Series(5, index=[1, 2])
print(s3)

print("\n\n")
print("*****************")
print("\n\n")





#---------------------------------------------------------------------------------------------------------------------------
#dataframe = series'lere benzer ancak burada coloum sistemi devreye girer.
#column değerleri ile tablolama haline getirilir gibi düşünülebilir veya excelde çalışılıyormuş gibi***
data = [10, 20, 30, 40, 50]
df = pd.DataFrame(data)
print(df)

print("\n\n")
print("*****************")
print("\n\n")
#---------------------------------------------------------------------------------------------------------------------------




data2 = [["Emre", 20, "Çanakkale"], ["Ali", 20, "Ankara"], ["Beray", 20, "Çanakkale"]]
df1 = pd.DataFrame(data2)
print(df1)
print("\n")
df2 = pd.DataFrame(data2, columns=["Isim", "Yaş", "Şehir"])
print(df2)
#, index=["1.Eleman", "2.Eleman", "3.Eleman"] eklenerek indexteki değerler de değiştirlebilir.

# vereceği çıktı =            isim  yaş      şehir
#                   1.Eleman   Emre   20  Çanakkale
#                   2.Eleman    Ali   20     Ankara
#                   3.Eleman  Beray   20  Çanakkale

print("\n\n")
print("*****************")
print("\n\n")
#---------------------------------------------------------------------------------------------------------------------------





#sözlük yapılırken ayrıca column ataması yapılmasına gerek kalmaz
data3 = {"Isim":["Emre", "Beray", "Boztepe"],
         "Yaş": [20, 30, 40],
         "Şehir":["Çanakkale", "Ankara", "Izmir"]}
df3 = pd.DataFrame(data3)
print(df3)
print("\n")
print(df3["Isim"])#sadece isimleri ve o isimlerin veri tiplerini verir. Spesifik


#spesifik column silme
            # #del df3["Şehir"]
            # df3.pop("Şehir")#aynı şey
            # print("\n")
            # print(df3)


print("\n")
#parantez içerisinde belirtilen kişinin bilgileri yazılır. (loc[] ile)
#iloc[] ise parantez içerisinde belirtilen sayıyı index olarak alır ve o indexteki bilgileri yazar
print(df3.loc[1])
print(df3.iloc[1])


print("\n\n")
print("*****************")
print("\n\n")

#2 aynı column tiplerini içeren verilerin birbirine appendlenmesi
df4 = df3.append(df2)
print(df4)
print("\n\n")

#aynı column olmadan da yapılabilir. bu sefer yeni columnlar ve yeni indexler eklenir(index isimleri aynı olsa bile yeni index olarak eklenir)
#yeni eklenen column eğer df'lerden birinde yok ise NaN değerini alır yani:
#     Isim   Yaş      Şehir      0     1          2
# 0   Emre  20.0  Çanakkale    NaN   NaN        NaN
# 1    Ali  20.0     Ankara    NaN   NaN        NaN
# 2  Beray  20.0  Çanakkale    NaN   NaN        NaN
# 0    NaN   NaN        NaN   Emre  20.0  Çanakkale
# 1    NaN   NaN        NaN    Ali  20.0     Ankara
# 2    NaN   NaN        NaN  Beray  20.0  Çanakkale
#alttaki örneğin çözümü

df5 = df2.append(df1)
print(df5)
#---------------------------------------------------------------------------------------------------------------------------






#çok karışık ve büyük df varken en baştaki verilere ulaşmak için head() kullanılabilir. ancak sadece ilk 5 veriyi yazar.
#tail() ise son 5 veriyi verir.
print("\n\n")
print(df4.head())
print("\n")
print(df4.tail())

print("\n\n")
print("*****************")
print("\n\n")
#---------------------------------------------------------------------------------------------------------------------------







#csv dosyasının okunması
notlar = pd.read_csv("grades.csv")
print(notlar)

notlar.columns = ["Isim", "Soyisim", "SSN", "Test1", "Test2", "Test3", "Test4", "Final", "Grade"]
print("\n\n")
print("*****************")
print("\n\n")

print(notlar["Grade"])#spesifik column'u bulma
print("\n")

print(notlar.loc[:, "Test1":"Test4"])#herkesin 4 testinin sonucunun bulunması(kısa yol). Test4 dahil!!!!
print(notlar.loc[:, ["Isim", "Final"]])#yalnızca isim ve final columnlarının bulunması(spesifik)
print("\n\n")
print("*****************")
print("\n\n")
#---------------------------------------------------------------------------------------------------------------------------







#filter işlemleri
films = pd.read_csv("imdb_1000.csv")
print(films.iloc[976])

print(films[films['star_rating'] > 8.5][['title', 'star_rating']])#star rating'i verilen sayıdan büyük filmlerin isimlerini ve ratingini yazdır
print(films[(films['star_rating'] > 8.5) & (films['star_rating'] < 9)][['title', 'star_rating']])#yalnızca 8.5-9 arasını yazdırmak için
print(films.query('star_rating >= 8.5')[['title', 'star_rating']])#üstteki ile aynı anlamda

print(films.star_rating.mean())#ortalaması
print(films.groupby('genre').star_rating.mean())#türlere göre star ratinglerin oranı
print("\n\n")
print("*****************")
print("\n\n")

#---------------------------------------------------------------------------------------------------------------------------







#mesela content_rating ile çalışmak istemiyoruz, o zaman:
#axis = 0 satırları sil demek, axis = 1 sütunları sil demek
print(films.drop("content_rating", axis=1).columns)
print("\n")
rowstodrop = [1, 4, 5]
print(films.drop(rowstodrop, axis=0).head())#belirtilen indekslerin gösterdiği satırlar düşer
print("\n")
print(films.mean())#tüm sayısal verilerin ortalamasını verir.
print("\n\n")
print("*****************")
print("\n\n")
#---------------------------------------------------------------------------------------------------------------------------





url = "http://bit.ly/uforeports"
data = pd.read_csv(url)#datayı url'den çekme

print(data.isnull().head())#boş data durumunu öğrenme
print("\n")
#datan.notnull() tam tersi!

print(data[data.City.isnull()])#şehir ismi boş olan verileri yazdırma
print("\n\n")
print("*****************")
print("\n\n")
#---------------------------------------------------------------------------------------------------------------------------





# dropna ile verilerin içindeki uyumsuzlukları uçururuz.
# satırlardan herhangi birinde null varsa, dropna ile atarız.
print(data.shape)#18241 data
data = data.dropna()
print(data.shape)#2486 data

data = data.dropna(subset=['City', 'Colors Reported'], how="any")
print(data.shape)
# how = any ise herhangi satırda null varsa siler.
# how = all ise tüm satırların null olması gerekir.
print("\n\n")
print("*****************")
print("\n\n")
#---------------------------------------------------------------------------------------------------------------------------






print(data['Shape Reported'].fillna('Belirsiz', inplace=True))#eğer null ise NaN yerine belirsiz yaz.
print(data['Shape Reported'].value_counts(dropna=False))#hangi shapeden ne kadar data var

# STRING ISLEMLERI
print(data.City.str.upper().head())
print(data.City.str.contains('Holyoke').head(100))#şehirler arasından arama yapma. varsa true döndür
print(data.City.str.replace('I', 'İ'))#I harfini İ ile değiştirmek
print("\n\n")
print("*****************")
print("\n\n")
# ---------------------------------------------------------------------------------------------------------------------------





data1 = {
        'id':[1, 2, 3, 4],
        'ad':['emre', 'emel', 'cemre', 'ümit'],
        'soyad':['boztepe', 'boztepe', 'boztepe', 'boztepe']

}

data2 = {
    'id': [1, 6, 3, 5],
    'sipariş': ['kahve', 'laptop', 'waffle makinesi', 'şampuan'],
    'fiyat': [10, 10000, 750, 22]

}

data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)

print(data1)
print("\n")
print(data2)

print(pd.merge(data1, data2, on='id', how='inner'))
print("\n")
#merge ile 2 veriyi id'ye göre(spesifik) düzenliyoruz. innerjoin'de ile ise eşleşen 2 datayı(spesifik)yan yana getiriyoruz
#leftjoin. data1'de olup data2'de olmayanları da getirir. rightjoinde tam tersi. mesela market verilerinde 1 ve 3 ürün satın almış iken
#2 ve 4 ürün satın almamıştır, bunu bulabiliriz.(left joinde)

print(pd.merge(data1, data2, on='id', how='left'))
print("\n")

