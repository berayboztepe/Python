import numpy as np


#arange ile = parantez içine girilen sayıya kadar bir liste oluşturuluyor
a = np.arange(15)
print(a)

print("\n\n")
print("*************************")
print("\n\n")

#reshape ile = parantez içine girilen değerlere göre matris haline getirilir. 3x5 lik matris
a = a.reshape(3, 5)
print(a)

print("\n\n")
print("*************************")
print("\n\n")

#b'nin türü ne. şuan (10,) cevabını verecek. bunun anlamı 10x1'lik bir matris
#ndim ile ise kaç boyutlu olduğunu görebiliriz. b için 1 boyutlu olacağını gösterir.
b = np.arange(10)
print(b.shape)
print(b.ndim)

print("\n\n")
print("*************************")
print("\n\n")

#array ile = gönderilen listeyi dizi haline getiriyorsun(aradaki virgüller gidiyor)
c = np.array([1, 10, 6, 8])
print(c)

print("\n\n")
print("*************************")
print("\n\n")

#(1, 10) arasına 1 ve 10 dahil olmak üzere rastgele sayılar ekle(1 ile 10 arasında 50 tane sayı yerleştiriyor!)
#(1, 10, 10) yaparsak ise 1 ile 10 dahil ama eşit aralıklarla artan 10 sayılık dizi oluştur demek
d = np.linspace(1, 10)
e = np.linspace(1, 10, 10)
print(d)
print(e)

print("\n\n")
print("*************************")
print("\n\n")

#temel matris işlemleri böyle yapılabilir.
f = np.arange(5)
g = np.arange(1, 10, 2)
print(g-f)
print(f**2)
print(g*f)
print(g@f)#matris çarpımının skalerini verir. print(a.dot(b)) aynı şeyler!
print(g<5)#g'nin elemanları 5'ten küçük mü? kontrol eder.

print("\n\n")
print("*************************")
print("\n\n")

#0'lar ve 1'ler matrisi oluşturmak
#0 ile 1 arasında random sayılar oluşturmak
h = np.ones((2, 4))
i = np.zeros((2, 4))
j = np.random.random((2, 4))
print(h)
print("\n")
print(i)
print("\n")
print(j)
print("\n")
print(np.sum(h))#h'deki değerlerin toplamı, np.min(), np.max() kullanılabilir.
print("\n")
print(np.sqrt(j))

print("\n\n")
print("*************************")
print("\n\n")


k = np.array([[1, 2, 3], [4, 5, 6]])
print(k[:, 0:2])#dizide tüm satırlara bak ve 0-2(2dahil değil). sütunlar arasındaki tüm sayıları yeni listeye atayarak döndür

print("\n\n")
print("*************************")
print("\n\n")

l = np.floor(10*np.random.random((3, 4)))
print(l)#0 ile 10 arası random sayılar al. floor ile mesela 2.7 gelirse yalnız 2 olarak yaz.
print("\n")
print(l.ravel())#üretilen matrisi tek boyutlu liste haline getirme
print("\n")
print(l.T)#matrisin transpozesini alma
print("\n")
print(l.reshape(6, -1))#her türlü ilk girdiğin parametre kadar satır haline getirmek için kullanılır.

print("\n\n")
print("*************************")
print("\n\n")

m = np.floor(10*np.random.random((3, 4)))
n = np.floor(10*np.random.random((3, 4)))

print(np.vstack((m, n)))#2 diziyi dikey olarak alt alta ekliyor. sütun sayısını sabit tutmak için.
print("\n")
print(np.hstack((m, n)))#2 diziyi yatay olarak yan yana ekliyor. satır sayısını sabit tutmak için

print("\n\n")
print("*************************")
print("\n\n")

o = np.arange(10)
p = o#p'nin işaret ettiği yer ile o'nun işaret ettiği yer aynı. o yüzden p'den herhangi bir değer değişirse, o'dan da değişir!
p[1] =100
print(p)
print(o)
print("\n")
#değişmemesi için: copy() kullanılabilir
r = p.copy()
r[1] = 10
print(p)
print(r)
print("\n")
#iki diziyi de değiştirmenin diğer yolu = view()
s = p.view()
s[1] = 10
print(p)
print(s)
print("\n")
#ancak s'yi reshape edersek ana dizi reshape olmaz!!! ancak reshape'den sonra yeniden değer değiştirmeye kalkarsak ikisinde de değişir!
s = s.reshape(2, 5)
print(p)
print(s)