from sympy import Symbol
from sympy import * #matematik işlemlerini bizim günlük hayatta kullandığımı şekilde gösterir ( kare, çarpma vb.)
from sympy import factor
from sympy import expand
import sympy.plotting as syp
import sympy as sym
import matplotlib.pyplot as plt

# x ve y değişkeni oluşturuyoruz değer vermeden(Import symbol ile)
x = Symbol('X')
y = Symbol('Y')
#print(x, y)

p = x*(x+x)
print("p = ", p)

print("\n")
print("------------------------")
print("\n")

# '*' importlandığında çarpmayı '.' olarak göstermek için pprint ile yazdırılır.
p2=(x+2)*(x+3)
pprint(p2)

print("\n")
print("------------------------")
print("\n")

#Bir ifadeyi çarpanlarına ayırıyoruz(Import Factor ile) ve çarpanlarına ayrılan ifadeyi açmak(expand ile)
expr = (x**2) - (y**2)
pprint(factor(expr))
print(expand(factor(expr)))
print("\n")
pprint(expand(factor(expr)))

print("\n")
print("------------------------")
print("\n")

#burada pprint ile üsleri '**' olarak değil ^3 olarak görüyoruz.
expr2 = x**3+3*x**2*y+3*x*y**2+y**3
factors=factor(expr2)
pprint(factors)
print("\n")
pprint(expand(factors))

print("\n")
print("------------------------")
print("\n")

#bir seri oluşturuyoruz
def series():
    x = Symbol('X')
    series = x
    n = 5 #int(input("Bir sayı girin:"))
    for i in range(2, n+1):
        series = series + (x**i) / i
    return series

pprint(series())

print("\n")
print("------------------------")
print("\n")

#değişkenlere değer verip x-y ifadelerinden kurtulma(subs ile)

expr = x*x + x*y + y*x + y*y
print("ifadenin sonucu = ", expr.subs({x:1, y:2}))

print("\n")
print("------------------------")
print("\n")
#daha önce yaptığımız fonksiyonda bu sefer x'e değer vererek cevabı elde ettik
def series2():
    x = Symbol('X')
    series = x
    n = 5 #int(input("Bir sayı girin:"))
    x_value = 10 #int(input("Bir sayı girin:"))
    for i in range(2, n+1):
        series = series + (x**i) / i
    series_value = series.subs({x:x_value})
    return series_value

pprint(series2())

print("\n")
print("------------------------")
print("\n")

#gauss fonksiyonunu formülle oluşturuyoruz
sigma = Symbol('sigma')
mu = Symbol('mu')
x = Symbol('X')

pprint(2*sym.pi*sigma)
#pprint((sym.sqrt(2*sym.pi*sigma)))

part_1 = 1/(sym.sqrt(2*sym.pi*sigma**2))
#pprint(part_1)

#print("\n\n")

part_2 = sym.exp(-1*((x-mu)**2) / (2*sigma**2))
#pprint(part_2)

print("------------------------")
print("\n")

gauss_function = part_1*part_2
pprint(gauss_function)

print("------------------------")
print("\n")
#bu fonksiyondaki sigma ve mu ifadelerine değer vererek grafik haline getiriyoruz(plot ile) sonda yazan kısımla da grafiğe isim verdik
sym.plot(gauss_function.subs({mu:1, sigma:3}), (x, -100, 100), title='gauss_distribution')

print("\n")
print("------------------------")
print("\n")

#bu işlemi for döngüsü ile yapmak istersek(evalf ile matematiksel hale getirdik)
for value in range(-5, 5):
    y = gauss_function.subs({mu:1, sigma:3, x:value}).evalf()
    print(value, y)

print("\n")
print("------------------------")
print("\n")

#burada da grafik haline getirdik(plot ile)

x__values = []
y__values = []
for value in range(-100, 100):
    y = gauss_function.subs({mu:1, sigma:3, x:value}).evalf()
    x__values.append(value)
    y__values.append(y)

plt.plot(x__values, y__values)#grafiğe  atadık
plt.show()#grafiği konsolda gösterdik
