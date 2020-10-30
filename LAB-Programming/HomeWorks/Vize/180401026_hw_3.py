from sympy import *
import sympy as sym
import matplotlib.pyplot as plt

num = 180401026
l = Symbol('lambda')#verilen sabit aralıkta ortaya çıkma sayısının beklenen değeri
k = Symbol('k')#istenen olasılık adedi

mod = sym.Mod(num, 4) #sympy kütüphanesinde mod almak için kullanılır
#print(mod)

#Poisson_Distrubution olduğu anlamına gelir.
#Possion Dağılımı = Belli bir sabit zaman birim aralığında meydana gelme sayısının olasılığını ifade eder.Nadir gerçekleşen olaylar için kullanılır.
#örnek olarak bir internet sitesine 2 saatte tıklanma sayısı 6 olsun.
#k = 6, lambda = 2


poissoneq = ((l**k) * (sym.exp(-l)))/ sym.factorial(k)#formülün bulunması. exp = e üzeri demek. factorial ile faktoryel aldık.
print("Formul aşağıdaki gibidir...\n")
pprint(poissoneq)#formülün yazılması


#sympy ile grafik
def sympy_graph():
    sym.plot(poissoneq.subs({l:2}), (k, 0, 6), title = 'Poisson Distrubition')#0-6 arası gözüküyor


#matplotlib ile grafik
def matlib_graph():
    x__values = []
    y__values = []

    print("Formülde atadığımız k değeri ve çıkan sonuçlar şu şekildedir..\n")
    for value in range(7):
        y = poissoneq.subs({l:2, k:value}).evalf()
        print(value, y)

    for i in range(7):
        y = poissoneq.subs({k:i, l:2}).evalf()# buradan x'e karşılık gelen y değerlerini buluruz
        x__values.append(i)
        y__values.append(y)


    plt.plot(x__values, y__values)#listelediğimiz değerleri grafiğe  atadık
    plt.show()#grafiği konsolda gösterdik


print("\n")
sympy_graph()
print("\n")
matlib_graph()


