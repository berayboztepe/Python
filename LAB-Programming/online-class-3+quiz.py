
from sympy import Symbol, Limit, exp, pi, Integral, sqrt
from sympy import *

#formül =                   S(t1+delta) + S(t1)
#                           -------------------      bu formül ile limit alıp türev buluyoruz
#                                 delta

t = Symbol('t')
t1 = Symbol('t1')
delta_t = Symbol('delta_t')

St = 5*t**2 + 2*t + 8 #türevi alınacak denklem

St1= St.subs({t:t1})       #t gördüğümüz yere t1 yazıyoruz
St1_delta = St.subs({t:t1+delta_t})   #t gördüğümüz yere t1+delta yazıyoruz

print("Türev = ")
pprint(Limit((St1_delta - St1) / delta_t, delta_t, 0).doit()) #delta_t yaklaşırken 0'a limit aldık

print("\n\n")
print("-----------------------------")
print("\n\n")

#integral bulma formülü              1       -(x+10)^2/2
#                                  ------ * e^
#                                  kok2*pi
#grafik üzerinde alınan bir noktanın 11-12 arasında olma olasılığı

x = Symbol('X')
p = exp(-(x-10) ** 2 / 2) / sqrt(2*pi)
print("İntegral Formülü = ")
pprint(p)
print("\n\n")
integral_result = Integral(p, (x, 11, 12)).doit().evalf() #x'in üst değeri = 12, alt değeri = 11 e göre integrali
print("İntegral Sonucu = ", integral_result)

